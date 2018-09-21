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
    typ, data = c.select('Does-Not-Exist')
    print(typ, data)
	
	
"""	
The data contains an error message describing the problem.


EXPECTED OUTPUT:

NO [b"Mailbox doesn't exist: Does-Not-Exist"]
"""