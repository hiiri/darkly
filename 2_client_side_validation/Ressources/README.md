# Client side validation

The website's survey is only checking input client-side, on the user's browser.
We can either edit the packets sent to the server to send any value we want but in this case we can just edit the HTML to ignore the validation.


http://{ip}/?page=survey 

Open a <select> tag and change vote value to a big number, then select that option.

# Mitigation
Validate user input server side. In this case, votes outside of 1-10 should not be allowed.

Flag: 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa
