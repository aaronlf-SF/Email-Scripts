"""
The example account has several mailboxes in a hierarchy:

- INBOX
- Deleted Messages
- Archive
- Example
	- 2016
"""

import imaplib
import imaplib_connect

with imaplib_connect.open_connection() as c:
    typ, data = c.select('INBOX')
    print(typ, data)
    num_msgs = int(data[0])
    print('There are {} messages in INBOX'.format(num_msgs))
	

"""
The response data contains the total number of messages in the mailbox.


EXPECTED OUTPUT:

OK [b'1']
There are 1 messages in INBOX
"""