# Stored XSS on feedback page

Go to the feedback page and type this in the message:

`/><script>alert(1);</script>`

The javascript will now run for anyone who visits that page which can be very dangerous.

# Mitigation

Sanitize user input, there are tons of libraries for this.

Flag: 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e
