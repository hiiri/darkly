## Open redirect

Scrolling to the bottom of the main page with the social media links, we can inspect the links to see that the redirection is done server side, for example the Facebook link url is "http://{ip}/index.php?page=redirect&site=facebook". The user is then redirected to "https://www.facebook.com/42born2code/" by the server.
We get the flag by replacing "&site=facebook" by something else like "&site=google.com"

# Exploiting the vulnerability

An attacker could use this vulnerability in a phishing attack. An example would be sending a user an email with a link from a legitimate website but which redirects to a malicious website. Mobile browsers often only show the domain and not the parameters in the URL which makes this attack very effective on mobile users.

The attacker would send a link like this: "www.legitwebsite.com/login?redirect=malicious.com"
The user would first be sent to the real "legitwebsite.com" website. But after logging in they will be sent to the attacker's website which could be modeled to look like the real one and input their credit card details etc.

# Fixing
There are multiple ways to fix this vulnerability depending on your application's complexity.
1. Never take redirections as parameters from the URL
2. If you need to redirect based on a parameter, have a list of redirections that are allowed (example: ['/profile', '/edit_profile', '/home'])
3. You can also append the redirect to a base url - instead of redirecting to "malicious.com", the application would always append to its url "www.legitwebsite.com/" + {redirect} which would result in "www.legitwebsite.com/profile" or in a malicious case "www.legitwebsite.com/malicious.com" which would result in an error and the user would not be redirected to a different website.
