# Request header spoofing

Click "© BornToSec" at the bottom of the page, it opens a page with an albatross with a hash in the url, it decrypts to "TAMERE", well this is just a funny prank by 42.

Inspect element to see comments with hints:

"You must cumming from : "https://www.nsa.gov/" to go to the next step"
"Let's use this browser : "ft_bornToSec". It will help you a lot."

So we need to set the first one as referer and the second one as our user agent for our HTTP GET request.

curl --referer https://www.nsa.gov/ http://{10.12.179.218}/\?page\=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c --user-agent "ft_bornToSec" -s | grep flag

# Mitigation

If your application is dependent on referer and user agent it is a good idea to validate that the information is indeed true. Verify the origin of headers and use CSRF (Cross-Site Request Forgery) tokens for requests that cause actions on your site and validate them in your backend.

Flag: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

