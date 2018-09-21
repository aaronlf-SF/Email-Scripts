import imaplib, email, os


user = 'user email'
password = 'password'
imap_url = 'imap.gmail.com'
attachment_dir = 'attachment directory'

# ----------------------------------------------------------------------

	
def auth(user,password,imap_url):
    '''signs in to email via IMAP
    '''
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    return con
	

# ----------------------------------------------------------------------


def get_body(msg):
    '''extracts the body from the email
    '''
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)


# ----------------------------------------------------------------------


def search_emails(key,value,con):
    '''search for a particular email
    '''
    result, data  = con.search(None,key,'"{}"'.format(value))
    return data #returns a bytes array in the form [b'1 2 3']
	
def get_emails(result_bytes): #result_bytes is the output from search()
    '''extracts emails from byte array
    '''
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs


# ----------------------------------------------------------------------


def get_attachments(msg):
    '''allows you to download attachments
    '''
    for part in msg.walk():
        if part.get_content_maintype()=='multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(attachment_dir, fileName)
            with open(filePath,'wb') as f:
                f.write(part.get_payload(decode=True))
			print(fileName)

# ----------------------------------------------------------------------

	
if __name__ == "__main__":
	con = auth(user,password,imap_url)
	con.select('INBOX')
	
    """
	DO STUFF HERE
    """
	
	con.close()
	con.logout()
	
	
# ----------------------------------------------------------------------