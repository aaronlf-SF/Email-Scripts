"""
As illustrated earlier, the client can ask the server for individual parts of the 
message separately. It is also possible to retrieve the entire message as an RFC 822 
formatted mail message and parse it with classes from the email module.
"""


import imaplib
import email
import email.parser

import imaplib_connect


with imaplib_connect.open_connection() as c:
    c.select('INBOX', readonly=True)

    typ, msg_data = c.fetch('1', '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            email_parser = email.parser.BytesFeedParser()
            email_parser.feed(response_part[1])
            msg = email_parser.close()
            for header in ['subject', 'to', 'from']:
                print('{:^8}: {}'.format(
                    header.upper(), msg[header]))

"""
The parser in the email module make it very easy to access and manipulate messages. 
This example prints just a few of the headers for each message.
"""


"""
EXPECTED OUTPUT:

SUBJECT : PyMOTW Example message 2
   TO   : Doug Hellmann <doug@doughellmann.com>
  FROM  : Doug Hellmann <doug@doughellmann.com>
 """