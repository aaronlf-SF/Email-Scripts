"""
The example account has several mailboxes in a hierarchy:

- INBOX
- Deleted Messages
- Archive
- Example
	- 2016
"""

"""After selecting the mailbox, use search() to retrieve the IDs of messages in the mailbox.
"""


import imaplib
import imaplib_connect

print()

with imaplib_connect.open_connection() as c:
    typ, mbox_data = c.list()
    for line in mbox_data:
        flags, delimiter, mbox_name = parse_list_response(line)
        c.select('"{}"'.format(mbox_name), readonly=True)
        typ, msg_ids = c.search(None, 'ALL')
        print(mbox_name, typ, msg_ids)
		

"""
Message IDs are assigned by the server, and are implementation dependent. The IMAP4 protocol 
makes a distinction between sequential IDs for messages at a given point in time during a 
transaction and UID identifiers for messages, but not all servers implement both.
"""

"""
EXPECTED OUTPUT:

Response code: OK
Server response: b'(\\HasChildren) "." Example'
Parsed response: ('\\HasChildren', '.', 'Example')
Server response: b'(\\HasNoChildren) "." Example.2016'
Parsed response: ('\\HasNoChildren', '.', 'Example.2016')
Server response: b'(\\HasNoChildren) "." Archive'
Parsed response: ('\\HasNoChildren', '.', 'Archive')
Server response: b'(\\HasNoChildren) "." "Deleted Messages"'
Parsed response: ('\\HasNoChildren', '.', 'Deleted Messages')
Server response: b'(\\HasNoChildren) "." INBOX'
Parsed response: ('\\HasNoChildren', '.', 'INBOX')

Example OK [b'']
Example.2016 OK [b'1']
Archive OK [b'']
Deleted Messages OK [b'']
INBOX OK [b'1']


In this case, INBOX and Example.2016 each have a different message with id 1. The other mailboxes are empty.
"""