Cookie md5 admin true

Flag: df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
---

http://10.13.199.248/?page=survey change vote value to 99999

Flag: 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa
---

http://10.13.199.248/index.php?page=recover inspect element change reset email to own

Flag: 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0
---

Xss on feedback page

`/><script>alert(1);</script>`

Flag: 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e
---
robots.txt
The file robots.txt is often used on webpages to tell web crawlers how they should access or disallow them from parts of the website,
for example to hide irrelevant results from Google search or prevent the server from overloading from crawlers loading content.

http://{ip}/robots.txt shows there are /whatever and /.hidden directories on the website

dirbuster {ip}/whatever/ directory
http://10.12.179.218/whatever/ has "htpasswd" file 
htpasswd file contents: "root:8621ffdbc5698829397d97767ac13db3"
username root, password is md5 encrypted and decrypts to "dragon"
password doesn't work on the login but trying out subdirectories we find {ip}/admin
login on {ip}/admin

Flag: d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
---
robots.txt 2
/whatever subdirectory

---

request header spoofing
click "© BornToSec" at the bottom of the page, it opens a page with an albatross with a hash in the url, it decrypts to "TAMERE".
inspect element to see comments with hints
"You must cumming from : "https://www.nsa.gov/" to go to the next step"
"Let's use this browser : "ft_bornToSec". It will help you a lot."
curl --referer https://www.nsa.gov/ http://10.12.179.218/\?page\=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c --user-agent "ft_bornToSec" -s | grep flag

Flag: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
---

Directory traversal

Following many of the links there is a pattern of a url with a parameter "?page=" for example: http://{ip}/?page=survey
Trying to add http://{ip}/?page=../ we see interesting alert messages with each added ../ which seems like a sign there is a directory we can access using this.
One of the messages is "You can DO it !!!  :]" and after trying out the common files an attacker would try to access we finally get 
http://{ip}/?page=../../../../../../../etc/passwd which gives the flag.

Flag: b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 

---
Unrestricted file upload of a malicious type
The "Add Image" page does not let you upload files unless they have a .jpg extension.
Looking at the request there is the filename and Content-Type. When a .jpg file is uploaded, it has the Content-Type of image/jpeg. 
However when sending a request with another file extension in the filename but still with Content-Type: image/jpeg we are allowed to upload whatever files we want, 
for example javascript that might then be executed on another user's browser when they view it. Doing this gives us the flag.

Flag: 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
---

Image link XSS
There is an image link on the main page: http://{ip}/?page=media&src=nsa
Changing the src parameter we get a wrong answer page but what's interesting is that with for example &src=test123 the html will contain an object tag with our data: 

![](./object_tag/Ressources/object_tag.png)

By encoding javascript into the url using base64 we can get the flag:

`<script>alert(1);</script>` 

base64-> `PHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4=`

http://{ip}/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4=

Flag: 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d
---

Members SQL injection

Trying out different inputs we can find out information about the SQL server used, in this case by just inputting an apostrophe ' we find out the site is usingg MySQL which can aid us in constructing queries.

Trying `1 OR 1=1` works and displays all users. The query might look something like this on the server:

`SELECT name FROM members WHERE id = 1 OR 1=1`

Since 1=1 is always true, it returns all the data in the table.
Trying different inputs we can get information from the error messages.

`1 union select 1,2,3 from user -- -`
>Table 'Member_Sql_Injection.user' doesn't exist

The table is called Member_Sql_Injection

Trying 
`1 or 1=1 ORDER BY 1--`, 

`1 or 1=1 ORDER BY 2--` and 

`1 or 1=1 ORDER BY 3--` 
>Unknown column '3' in 'order clause'

There are only 2 columns, first name and last name. 