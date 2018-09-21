"""
Although many modern mail clients use a “Trash folder” model for working 
with deleted messages, the messages are not usually moved into an actual 
folder. Instead, their flags are updated to add \Deleted. The operation 
for “emptying” the trash is implemented through the EXPUNGE command. 
This example script finds the archived messages with “Lorem ipsum” in the 
subject, sets the deleted flag, then shows that the messages are still 
present in the folder by querying the server again.
"""


import imaplib
import imaplib_connect
from imaplib_list_parse import parse_list_response

with imaplib_connect.open_connection() as c:
    c.select('Example.Today')

    # What ids are in the mailbox?
    typ, [msg_ids] = c.search(None, 'ALL')
    print('Starting messages:', msg_ids)

    # Find the message(s)
    typ, [msg_ids] = c.search(
        None,
        '(SUBJECT "subject goes here")',
    )
    msg_ids = ','.join(msg_ids.decode('utf-8').split(' '))
    print('Matching messages:', msg_ids)

    # What are the current flags?
    typ, response = c.fetch(msg_ids, '(FLAGS)')
    print('Flags before:', response)

    # Change the Deleted flag
    typ, response = c.store(msg_ids, '+FLAGS', r'(\Deleted)')

    # What are the flags now?
    typ, response = c.fetch(msg_ids, '(FLAGS)')
    print('Flags after:', response)

    # Really delete the message.
    typ, response = c.expunge()
    print('Expunged:', response)

    # What ids are left in the mailbox?
    typ, [msg_ids] = c.search(None, 'ALL')
    print('Remaining messages:', msg_ids)

	
	
"""
Explicitly calling expunge() removes the messages, but calling close() 
has the same effect. The difference is the client is not notified about 
the deletions when close() is called.
"""


"""
EXPECTED OUTPUT:

Response code: OK
Server response: b'(\\HasChildren) "." Example'
Parsed response: ('\\HasChildren', '.', 'Example')
Server response: b'(\\HasNoChildren) "." Example.Today'
Parsed response: ('\\HasNoChildren', '.', 'Example.Today')
Server response: b'(\\HasNoChildren) "." Example.2016'
Parsed response: ('\\HasNoChildren', '.', 'Example.2016')
Server response: b'(\\HasNoChildren) "." Archive'
Parsed response: ('\\HasNoChildren', '.', 'Archive')
Server response: b'(\\HasNoChildren) "." "Deleted Messages"'
Parsed response: ('\\HasNoChildren', '.', 'Deleted Messages')
Server response: b'(\\HasNoChildren) "." INBOX'
Parsed response: ('\\HasNoChildren', '.', 'INBOX')
Starting messages: b'1 2'
Matching messages: 1,2
Flags before: [b'1 (FLAGS (\\Seen))', b'2 (FLAGS (\\Seen))']
Flags after: [b'1 (FLAGS (\\Deleted \\Seen))', b'2 (FLAGS (\\Del
eted \\Seen))']
Expunged: [b'2', b'1']
Remaining messages: b''
"""