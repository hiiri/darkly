# Directory traversal

Following many of the links there is a pattern of a url with a parameter "?page=" for example: http://{ip}/?page=survey
Trying to add http://{ip}/?page=../ we see interesting alert messages with each added ../ which seems like a sign there is a directory we can access using this.
One of the messages is "You can DO it !!!  :]" and after trying out common files an attacker would try to access we finally get 
http://{ip}/?page=../../../../../../../etc/passwd which gives the flag.


# Mitigation
In this case we could access arbitrary files on the server because the site treated the requests like someone traversing a filesystem. This can be fixed by not using urls to accept arbitrary input but instead having a set of allowed URLs, surrounding user input with your own path code or using indexes for content instead of their paths.

Flag: b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 
