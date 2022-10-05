# Sensitive data on password reset page

The section for resetting a password contains the email that the reset email would be sent to in the HTML. Right click the submit button, inspect element and change it to your own email, then submit to get the flag.

http://10.13.199.248/index.php?page=recover

# Mitigation

Do sensitive actions like this server side and don't put sensitive data in your source code.

Flag: 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0
