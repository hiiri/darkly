# Bad session handling

The website sets a cookie for checking if the user is an administrator.
By changing the cookie we get the flag. While this is a simplified example, cookies can be stolen and therefore someone might be able to hijack a user's session without needing their password.

Here the cookie "I_am_admin" is "false" encrypted with md5.
https://md5decrypt.net/en
Encrypt "true", replace the cookie and we get the flag after refreshing.

# Mitigation
Use random, unique session ids with expire times for user session management. If you need to return admin specific data, handle the check server side, not with a cookie. If a cookie contains sensitive data, encrypt it properly.

Flag: df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
