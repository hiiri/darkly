# Web crawling

The file robots.txt is often used on webpages to tell web crawlers how they should access or disallow them from parts of the website,
for example to hide irrelevant results from Google search or prevent the server from overloading from crawlers loading content.

http://{ip}/robots.txt shows there are /whatever and /.hidden directories on the website

/.hidden subdirectory

There are tons of random looking links and clicking through them shows they all have a README with a message. It's unrealistic to do this manually so we can write a program to recursively crawl all links.

Running the program crawler.py for a while we find a string that looks like it could be a hash but I could not find any matches for it so I am assuming it is the flag.

http://{ip}/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README

Flag: 99dde1d35d1fdd283924d84e6d9f1d820