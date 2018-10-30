

import StringIO
import json
import logging
import random
import urllib
import urllib2
from auto_start import *
from auto_leech import *
from auto_list import *
from auto_h import *
from auto_hlist import *
from collections import defaultdict

# for sending images
from PIL import Image
import multipart
excl =  u"\u203C"
# standard app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2
from main import *

class leech(webapp2.RequestHandler):
    def get(self):
        for p in chatList:
            chat_id = p
            def reply4(msg=None, img=None):
                if msg:
                    resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                        'chat_id': str(chat_id),
                        'text': msg.encode('utf-8'),
                        #'disable_web_page_preview': 'true',
                        #'reply_to_message_id': str(message_id),
        })).read()
            p = len(mainlist[chat_id])
            if p > 0:
                leechers = "\n".join(mainlist[chat_id])
                reply('%s Still missing engagement from:\n', excl)
                reply(leechers)
            else:
                reply4('No Leechers!')

app = webapp2.WSGIApplication([
    ('/auto_leech', leech),
], debug=True)