import imaplib

from imaplib_connect import open_connection

with open_connection() as c:
    typ, data = c.list(pattern='*Example*')

print('Response code:', typ)

for line in data:
    print('Server response:', line)
#In this case, both Example and Example.2016 are included in the response.


"""
EXPECTED OUTPUT:

Response code: OK
Server response: b'(\\HasChildren) "." Example'
Server response: b'(\\HasNoChildren) "." Example.2016'
"""