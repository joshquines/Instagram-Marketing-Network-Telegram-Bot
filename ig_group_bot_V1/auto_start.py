from main import *

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
htrue = defaultdict(list)

class autostart(webapp2.RequestHandler):
    def get(self):
        for p in chatList:
            chat_id = p
            def reply3(msg=None, img=None):
                if msg:
                    resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                        'chat_id': str(chat_id),
                        'text': msg.encode('utf-8'),
                        #'disable_web_page_preview': 'true',
                        #'reply_to_message_id': str(message_id),
        })).read()
            htrue[chat_id].append('H')
            a = len(herelist[chat_id])
            while a > 0:
                herelist[chat_id].pop()
            a -= 1
            a = len(mainlist[chat_id])
            while a > 0:
                mainlist[chat_id].pop()
                a -= 1
            a = len(list1[chat_id])
            while a > 0:
                list1[chat_id].pop()
                a -= 1
            a = len(list2[chat_id])
            while a > 0:
                list2[chat_id].pop()
                a -= 1
            a = len(list3[chat_id])
            while a > 0:
                list3[chat_id].pop()
                a -= 1
            a = len(list4[chat_id])
            while a > 0:
                list4[chat_id].pop()
                a -= 1
            a = len(list5[chat_id])
            while a > 0:
                list5[chat_id].pop()
                a -= 1
            a = len(list6[chat_id])
            while a > 0:
                list6[chat_id].pop()
                a -= 1
            a = len(list7[chat_id])
            while a > 0:
                list7[chat_id].pop()
                a -= 1
            a = len(list8[chat_id])
            while a > 0:
                list8[chat_id].pop()
                a -= 1
            a = len(list9[chat_id])
            while a > 0:
                list9[chat_id].pop()
                a -= 1
            a = len(list10[chat_id])
            while a > 0:
                list10[chat_id].pop()
                a -= 1
            a = len(list11[chat_id])
            while a > 0:
                list11[chat_id].pop()
                a -= 1
            a = len(list12[chat_id])
            while a > 0:
                list12[chat_id].pop()
                a -= 1  
            reply3('%s Round Is Starting. Drop your @usernames now\nList will drop in 20 minutes\n%sIf you can\'t make this round but you entered, just enter /remove @username', excl)  

app = webapp2.WSGIApplication([
    ('/auto_start', autostart),
], debug=True)