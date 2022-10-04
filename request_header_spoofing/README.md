# Request header spoofing

click "© BornToSec" at the bottom of the page, it opens a page with an albatross with a hash in the url, it decrypts to "TAMERE", well this is just a funny prank by 42.

inspect element to see comments with hints:

"You must cumming from : "https://www.nsa.gov/" to go to the next step"
"Let's use this browser : "ft_bornToSec". It will help you a lot."

curl --referer https://www.nsa.gov/ http://10.12.179.218/\?page\=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c --user-agent "ft_bornToSec" -s | grep flag

Flag: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

---