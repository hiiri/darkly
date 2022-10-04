# Unrestricted file upload of a malicious type

The "Add Image" page does not let you upload files unless they have a .jpg extension.
Looking at the request there is the filename and Content-Type. When a .jpg file is uploaded, it has the Content-Type of image/jpeg. 
However when sending a request with another file extension in the filename but still with Content-Type: image/jpeg we are allowed to upload whatever files we want, 
for example javascript that might then be executed on another user's browser when they view it. Doing this gives us the flag.

Flag: 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8