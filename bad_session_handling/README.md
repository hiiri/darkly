# Bad session handling

The website sets a cookie for testing if the user is an administrator.
By changing the cookie we get the flag. While this is a simplified example, cookies can be stolen and therefore someone might be able to highjack a user's session without needing their password.

Here the cookie is encoded using

Cookie md5 admin true

Flag: df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
