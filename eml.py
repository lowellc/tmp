#!/usr/bin/env python2.7
#shamelessly copied from stackoverflow by lowellc
#Extracts raw.eml to guid.ksh, guid.html, and attachments.

import email
import mimetypes
import uuid
from emaildata.attachment import Attachment
import sys

if len(sys.argv) == 1: 
    print "Please supply a raw email, typically ending in .eml..."
    exit(1)

eml = sys.argv[1]

message = email.message_from_file(open(eml))
for content, filename, mimetype, message in Attachment.extract(message, False):
    if not filename:
        filename = str(uuid.uuid1()) + (mimetypes.guess_extension(mimetype) or '.txt')
    print filename
    with open(filename, 'w') as stream:
        stream.write(content)
    # If message is not None then it is an instance of email.message.Message
    if message:
        print "The file {0} is a message with attachments.".format(filename)
