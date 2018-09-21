"""
The response from the FETCH command starts with the flags, then indicates that there 
are 595 bytes of header data. The client constructs a tuple with the response for the 
message, and then closes the sequence with a single string containing the right 
parenthesis (“)”) the server sends at the end of the fetch response. Because of this 
formatting, it may be easier to fetch different pieces of information separately, or 
to recombine the response and parse it in the client.
"""

import imaplib
import pprint
import imaplib_connect

with imaplib_connect.open_connection() as c:
    c.select('INBOX', readonly=True)

    print('HEADER:')
    typ, msg_data = c.fetch('1', '(BODY.PEEK[HEADER])')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            print(response_part[1])

    print('\nBODY TEXT:')
    typ, msg_data = c.fetch('1', '(BODY.PEEK[TEXT])')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            print(response_part[1])

    print('\nFLAGS:')
    typ, msg_data = c.fetch('1', '(FLAGS)')
    for response_part in msg_data:
        print(response_part)
        print(imaplib.ParseFlags(response_part))


"""
Fetching values separately has the added benefit of making it easy to use ParseFlags() to 
parse the flags from the response.
"""


"""
EXPECTED OUTPUT:

HEADER:
b'Return-Path: <doug@doughellmann.com>\r\nReceived: from compute
4.internal (compute4.nyi.internal [10.202.2.44])\r\n\t by sloti2
6t01 (Cyrus 3.0.0-beta1-git-fastmail-12410) with LMTPA;\r\n\t Su
n, 06 Mar 2016 16:16:03 -0500\r\nX-Sieve: CMU Sieve 2.4\r\nX-Spa
m-known-sender: yes, fadd1cf2-dc3a-4984-a08b-02cef3cf1221="doug"
,\r\n  ea349ad0-9299-47b5-b632-6ff1e394cc7d="both hellfly"\r\nX-
Spam-score: 0.0\r\nX-Spam-hits: ALL_TRUSTED -1, BAYES_00 -1.9, L
ANGUAGES unknown, BAYES_USED global,\r\n  SA_VERSION 3.3.2\r\nX-
Spam-source: IP=\'127.0.0.1\', Host=\'unk\', Country=\'unk\', Fr
omHeader=\'com\',\r\n  MailFrom=\'com\'\r\nX-Spam-charsets: plai
n=\'us-ascii\'\r\nX-Resolved-to: doughellmann@fastmail.fm\r\nX-D
elivered-to: doug@doughellmann.com\r\nX-Mail-from: doug@doughell
mann.com\r\nReceived: from mx5 ([10.202.2.204])\r\n  by compute4
.internal (LMTPProxy); Sun, 06 Mar 2016 16:16:03 -0500\r\nReceiv
ed: from mx5.nyi.internal (localhost [127.0.0.1])\r\n\tby mx5.ny
i.internal (Postfix) with ESMTP id 47CBA280DB3\r\n\tfor <doug@do
ughellmann.com>; Sun,  6 Mar 2016 16:16:03 -0500 (EST)\r\nReceiv
ed: from mx5.nyi.internal (localhost [127.0.0.1])\r\n    by mx5.
nyi.internal (Authentication Milter) with ESMTP\r\n    id A71788
6846E.30BA4280D81;\r\n    Sun, 6 Mar 2016 16:16:03 -0500\r\nAuth
entication-Results: mx5.nyi.internal;\r\n    dkim=pass (1024-bit
 rsa key) header.d=messagingengine.com header.i=@messagingengine
.com header.b=Jrsm+pCo;\r\n    x-local-ip=pass\r\nReceived: from
 mailout.nyi.internal (gateway1.nyi.internal [10.202.2.221])\r\n
\t(using TLSv1.2 with cipher ECDHE-RSA-AES256-GCM-SHA384 (256/25
6 bits))\r\n\t(No client certificate requested)\r\n\tby mx5.nyi.
internal (Postfix) with ESMTPS id 30BA4280D81\r\n\tfor <doug@dou
ghellmann.com>; Sun,  6 Mar 2016 16:16:03 -0500 (EST)\r\nReceive
d: from compute2.internal (compute2.nyi.internal [10.202.2.42])\
r\n\tby mailout.nyi.internal (Postfix) with ESMTP id 1740420D0A\
r\n\tfor <doug@doughellmann.com>; Sun,  6 Mar 2016 16:16:03 -050
0 (EST)\r\nReceived: from frontend2 ([10.202.2.161])\r\n  by com
pute2.internal (MEProxy); Sun, 06 Mar 2016 16:16:03 -0500\r\nDKI
M-Signature: v=1; a=rsa-sha1; c=relaxed/relaxed; d=\r\n\tmessagi
ngengine.com; h=content-transfer-encoding:content-type\r\n\t:dat
e:from:message-id:mime-version:subject:to:x-sasl-enc\r\n\t:x-sas
l-enc; s=smtpout; bh=P98NTsEo015suwJ4gk71knAWLa4=; b=Jrsm+\r\n\t
pCovRIoQIRyp8Fl0L6JHOI8sbZy2obx7O28JF2iTlTWmX33Rhlq9403XRklwN3JA
\r\n\t7KSPqMTp30Qdx6yIUaADwQqlO+QMuQq/QxBHdjeebmdhgVfjhqxrzTbSMw
w/ZNhL\r\n\tYwv/QM/oDHbXiLSUlB3Qrg+9wsE/0jU/EOisiU=\r\nX-Sasl-en
c: 8ZJ+4ZRE8AGPzdLRWQFivGymJb8pa4G9JGcb7k4xKn+I 1457298962\r\nRe
ceived: from [192.168.1.14] (75-137-1-34.dhcp.nwnn.ga.charter.co
m [75.137.1.34])\r\n\tby mail.messagingengine.com (Postfix) with
 ESMTPA id C0B366801CD\r\n\tfor <doug@doughellmann.com>; Sun,  6
 Mar 2016 16:16:02 -0500 (EST)\r\nFrom: Doug Hellmann <doug@doug
hellmann.com>\r\nContent-Type: text/plain; charset=us-ascii\r\nC
ontent-Transfer-Encoding: 7bit\r\nSubject: PyMOTW Example messag
e 2\r\nMessage-Id: <00ABCD46-DADA-4912-A451-D27165BC3A2F@doughel
lmann.com>\r\nDate: Sun, 6 Mar 2016 16:16:02 -0500\r\nTo: Doug H
ellmann <doug@doughellmann.com>\r\nMime-Version: 1.0 (Mac OS X M
ail 9.2 \\(3112\\))\r\nX-Mailer: Apple Mail (2.3112)\r\n\r\n'

BODY TEXT:
b'This is the second example message.\r\n'

FLAGS:
b'1 (FLAGS ())'
()
"""