"""
The example account has several mailboxes in a hierarchy:

- INBOX
- Deleted Messages
- Archive
- Example
	- 2016
There is one unread message in the INBOX folder, and one read message in Example/2016.
"""


import imaplib

from imaplib_connect import open_connection


with open_connection() as c:
    typ, data = c.list(directory='Example')

print('Response code:', typ)

for line in data:
    print('Server response:', line)
The parent and subfolder are returned.


"""
EXPECTED OUTPUT:

Response code: OK
Server response: b'(\\HasChildren) "." Example'
Server response: b'(\\HasNoChildren) "." Example.2016'

Alternately, to list folders matching a pattern, pass the pattern argument.
"""
