# Sensitive data accessible on server

The server has a htpasswd file which contains root credentials and this file is publically accessible.

The file robots.txt is often used on webpages to tell web crawlers how they should access or disallow them from parts of the website,
for example to hide irrelevant results from Google search or prevent the server from overloading from crawlers loading content.

http://{ip}/robots.txt shows there are /whatever and /.hidden directories on the website

http://10.12.179.218/whatever/ has "htpasswd" file 
htpasswd file contents: "root:8621ffdbc5698829397d97767ac13db3"
username root, password is md5 encrypted and decrypts to "dragon"
password doesn't work on the login but trying out subdirectories we find {ip}/admin
login on {ip}/admin

Flag: d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
