"""
The identifiers returned by search() are used to retrieve the contents, or partial contents, 
of messages for further processing using the fetch() method. It takes two arguments, the 
message IDs to fetch and the portion(s) of the message to retrieve.

The message_ids argument is a comma separated list of ids (e.g., "1", "1,2") or ID ranges 
(e.g., 1:2). The message_parts argument is an IMAP list of message segment names. As with 
search criteria for search(), the IMAP protocol specifies named message segments so clients 
can efficiently retrieve only the parts of the message they actually need. For example, to 
retrieve the headers of the messages in a mailbox, use fetch() with the argument BODY.PEEK[HEADER].

Note:
	Another way to fetch the headers is BODY[HEADERS], but that form has a side-effect 
	of implicitly marking the message as read, which is undesirable in many cases.
"""

import imaplib
import pprint
import imaplib_connect

imaplib.Debug = 4
with imaplib_connect.open_connection() as c:
    c.select('INBOX', readonly=True)
    typ, msg_data = c.fetch('1', '(BODY.PEEK[HEADER] FLAGS)')
    pprint.pprint(msg_data)

"""
The return value of fetch() has been partially parsed so it is somewhat harder to work 
with than the return value of list(). Turning on debugging shows the complete interaction 
between the client and server to understand why this is so.
"""


"""
 EXPECTED OUTPUT:

  19:40.68 imaplib version 2.58
  19:40.68 new IMAP4 connection, tag=b'IIEN'
  19:40.70 < b'* OK [CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN
-REFERRALS ID ENABLE IDLE AUTH=PLAIN] Dovecot (Ubuntu) ready.'
  19:40.70 > b'IIEN0 CAPABILITY'
  19:40.73 < b'* CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REF
ERRALS ID ENABLE IDLE AUTH=PLAIN'
  19:40.73 < b'IIEN0 OK Pre-login capabilities listed, post-logi
n capabilities have more.'
  19:40.73 CAPABILITIES: ('IMAP4REV1', 'LITERAL+', 'SASL-IR', 'L
OGIN-REFERRALS', 'ID', 'ENABLE', 'IDLE', 'AUTH=PLAIN')
  19:40.73 > b'IIEN1 LOGIN example "TMFw00fpymotw"'
  19:40.79 < b'* CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REF
ERRALS ID ENABLE IDLE SORT SORT=DISPLAY THREAD=REFERENCES THREAD
=REFS THREAD=ORDEREDSUBJECT MULTIAPPEND URL-PARTIAL CATENATE UNS
ELECT CHILDREN NAMESPACE UIDPLUS LIST-EXTENDED I18NLEVEL=1 CONDS
TORE QRESYNC ESEARCH ESORT SEARCHRES WITHIN CONTEXT=SEARCH LIST-
STATUS SPECIAL-USE BINARY MOVE'
  19:40.79 < b'IIEN1 OK Logged in'
  19:40.79 > b'IIEN2 EXAMINE INBOX'
  19:40.82 < b'* FLAGS (\\Answered \\Flagged \\Deleted \\Seen \\
Draft)'
  19:40.82 < b'* OK [PERMANENTFLAGS ()] Read-only mailbox.'
  19:40.82 < b'* 2 EXISTS'
  19:40.82 < b'* 0 RECENT'
  19:40.82 < b'* OK [UNSEEN 1] First unseen.'
  19:40.82 < b'* OK [UIDVALIDITY 1457297769] UIDs valid'
  19:40.82 < b'* OK [UIDNEXT 6] Predicted next UID'
  19:40.82 < b'* OK [HIGHESTMODSEQ 20] Highest'
  19:40.82 < b'IIEN2 OK [READ-ONLY] Examine completed (0.000 sec
s).'
  19:40.82 > b'IIEN3 FETCH 1 (BODY.PEEK[HEADER] FLAGS)'
  19:40.86 < b'* 1 FETCH (FLAGS () BODY[HEADER] {3108}'
  19:40.86 read literal size 3108
  19:40.86 < b')'
  19:40.89 < b'IIEN3 OK Fetch completed.'
  19:40.89 > b'IIEN4 LOGOUT'
  19:40.93 < b'* BYE Logging out'
  19:40.93 BYE response: b'Logging out'
[(b'1 (FLAGS () BODY[HEADER] {3108}',
  b'Return-Path: <doug@doughellmann.com>\r\nReceived: from compu
te4.internal ('
  b'compute4.nyi.internal [10.202.2.44])\r\n\t by sloti26t01 (Cy
rus 3.0.0-beta1'
  b'-git-fastmail-12410) with LMTPA;\r\n\t Sun, 06 Mar 2016 16:1
6:03 -0500\r'
  b'\nX-Sieve: CMU Sieve 2.4\r\nX-Spam-known-sender: yes, fadd1c
f2-dc3a-4984-a0'
  b'8b-02cef3cf1221="doug",\r\n  ea349ad0-9299-47b5-b632-6ff1e39
4cc7d="both he'
  b'llfly"\r\nX-Spam-score: 0.0\r\nX-Spam-hits: ALL_TRUSTED -1,
BAYES_00 -1.'
  b'9, LANGUAGES unknown, BAYES_USED global,\r\n  SA_VERSION 3.3
.2\r\nX-Spam'
  b"-source: IP='127.0.0.1', Host='unk', Country='unk', FromHead
er='com',\r\n "
  b" MailFrom='com'\r\nX-Spam-charsets: plain='us-ascii'\r\nX-Re
solved-to: d"
  b'oughellmann@fastmail.fm\r\nX-Delivered-to: doug@doughellmann
.com\r\nX-Ma'
  b'il-from: doug@doughellmann.com\r\nReceived: from mx5 ([10.20
2.2.204])\r'
  b'\n  by compute4.internal (LMTPProxy); Sun, 06 Mar 2016 16:16
:03 -0500\r\nRe'
  b'ceived: from mx5.nyi.internal (localhost [127.0.0.1])\r\n\tb
y mx5.nyi.inter'
  b'nal (Postfix) with ESMTP id 47CBA280DB3\r\n\tfor <doug@dough
ellmann.com>; S'
  b'un,  6 Mar 2016 16:16:03 -0500 (EST)\r\nReceived: from mx5.n
yi.internal (l'
  b'ocalhost [127.0.0.1])\r\n    by mx5.nyi.internal (Authentica
tion Milter) w'
  b'ith ESMTP\r\n    id A717886846E.30BA4280D81;\r\n    Sun, 6 M
ar 2016 16:1'
  b'6:03 -0500\r\nAuthentication-Results: mx5.nyi.internal;\r\n
   dkim=pass'
  b' (1024-bit rsa key) header.d=messagingengine.com header.i=@m
essagingengi'
  b'ne.com header.b=Jrsm+pCo;\r\n    x-local-ip=pass\r\nReceived
: from mailo'
  b'ut.nyi.internal (gateway1.nyi.internal [10.202.2.221])\r\n\t
(using TLSv1.2 '
  b'with cipher ECDHE-RSA-AES256-GCM-SHA384 (256/256 bits))\r\n\
t(No client cer'
  b'tificate requested)\r\n\tby mx5.nyi.internal (Postfix) with
ESMTPS id 30BA4'
  b'280D81\r\n\tfor <doug@doughellmann.com>; Sun,  6 Mar 2016 16
:16:03 -0500 (E'
  b'ST)\r\nReceived: from compute2.internal (compute2.nyi.intern
al [10.202.2.4'
  b'2])\r\n\tby mailout.nyi.internal (Postfix) with ESMTP id 174
0420D0A\r\n\tf'
  b'or <doug@doughellmann.com>; Sun,  6 Mar 2016 16:16:03 -0500
(EST)\r\nRecei'
  b'ved: from frontend2 ([10.202.2.161])\r\n  by compute2.intern
al (MEProxy); '
  b'Sun, 06 Mar 2016 16:16:03 -0500\r\nDKIM-Signature: v=1; a=rs
a-sha1; c=rela'
  b'xed/relaxed; d=\r\n\tmessagingengine.com; h=content-transfer
-encoding:conte'
  b'nt-type\r\n\t:date:from:message-id:mime-version:subject:to:x
-sasl-enc\r\n'
  b'\t:x-sasl-enc; s=smtpout; bh=P98NTsEo015suwJ4gk71knAWLa4=; b
=Jrsm+\r\n\t'
  b'pCovRIoQIRyp8Fl0L6JHOI8sbZy2obx7O28JF2iTlTWmX33Rhlq9403XRklw
N3JA\r\n\t7KSPq'
  b'MTp30Qdx6yIUaADwQqlO+QMuQq/QxBHdjeebmdhgVfjhqxrzTbSMww/ZNhL\
r\n\tYwv/QM/oDH'
  b'bXiLSUlB3Qrg+9wsE/0jU/EOisiU=\r\nX-Sasl-enc: 8ZJ+4ZRE8AGPzdL
RWQFivGymJb8pa'
  b'4G9JGcb7k4xKn+I 1457298962\r\nReceived: from [192.168.1.14]
(75-137-1-34.d'
  b'hcp.nwnn.ga.charter.com [75.137.1.34])\r\n\tby mail.messagin
gengine.com (Po'
  b'stfix) with ESMTPA id C0B366801CD\r\n\tfor <doug@doughellman
n.com>; Sun,  6'
  b' Mar 2016 16:16:02 -0500 (EST)\r\nFrom: Doug Hellmann <doug@
doughellmann.c'
  b'om>\r\nContent-Type: text/plain; charset=us-ascii\r\nContent
-Transfer-En'
  b'coding: 7bit\r\nSubject: PyMOTW Example message 2\r\nMessage
-Id: <00ABCD'
  b'46-DADA-4912-A451-D27165BC3A2F@doughellmann.com>\r\nDate: Su
n, 6 Mar 2016 '
  b'16:16:02 -0500\r\nTo: Doug Hellmann <doug@doughellmann.com>\
r\nMime-Vers'
  b'ion: 1.0 (Mac OS X Mail 9.2 \\(3112\\))\r\nX-Mailer: Apple M
ail (2.3112)'
  b'\r\n\r\n'),
 b')']
"""