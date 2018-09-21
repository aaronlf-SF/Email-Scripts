"""
Once a message is on the server, it can be moved or copied without downloading 
it using move() or copy(). These methods operate on message id ranges, just as 
fetch() does.
"""


import imaplib
import imaplib_connect

def search_emails(key,value,con):
    '''search for a particular email
    '''
    result, data  = con.search(None,key,'"{}"'.format(value))
    return result,data #returns a bytes array in the form [b'1 2 3']
	
with imaplib_connect.open_connection() as c:
    # Find the "SEEN" messages in INBOX
    c.select('INBOX')
    typ, [response] = search_emails('FROM','person@emaildomain.com',c)
    if typ != 'OK':
        raise RuntimeError(response)
    msg_ids = ','.join(response.decode('utf-8').split(' '))

    # Create a new mailbox, "Example.Today"
    typ, create_response = c.create('Example/Today') # Folder named 'Example' must exist first
    print('CREATED Example/Today:', create_response)

    # Copy the messages
    print('COPYING:', msg_ids)
    c.copy(msg_ids, 'Example/Today')

    # Look at the results
    c.select('Example/Today')
    typ, [response] = c.search(None, 'ALL')
    print('COPIED:', response)
	

"""
This example script creates a new mailbox under Example and copies the read messages 
from INBOX into it.
"""
"""
EXPECTED OUTPUT:

CREATED Example.Today: [b'Completed']
COPYING: 2
COPIED: b'1'
"""


"""
Running the same script again shows the importance to checking return codes. Instead of 
raising an exception, the call to create() to make the new mailbox reports that the mailbox 
already exists.
"""
"""
EXPECTED OUTPUT:

CREATED Example.Today: [b'[ALREADYEXISTS] Mailbox already exists
']
COPYING: 2
COPIED: b'1 2'
"""

