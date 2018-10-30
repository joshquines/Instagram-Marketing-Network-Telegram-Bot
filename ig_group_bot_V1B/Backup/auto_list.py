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

# standard app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2

class autolist(webapp2.RequestHandler):
	def post(self):
	    for p in chatList:
	        chat_id = p
	        def reply2(msg=None, img=None):
	            if msg:
	                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
	                    'chat_id': str(chat_id),
	                    'text': msg.encode('utf-8'),
	                    'disable_web_page_preview': 'true',
	                    #'reply_to_message_id': str(message_id),
	                })).read() 
	        xu = len(list1[chat_id])
	        if xu > 0:
	            list_one = "\n".join(list1[chat_id])
	            #bot_talk('this is list 1')
	            reply2("LIST 1")
	            reply2(list_one)
	        xu = len(list2[chat_id])
	        if xu > 0:
	            list_two = "\n".join(list2[chat_id])
	            reply2("LIST 2")
	            reply2(list_two)
	        xu = len(list3[chat_id])
	        if xu > 0:
	            list_three = "\n".join(list3[chat_id])
	            reply2("LIST 3")
	            reply2(list_three)
	        xu = len(list4[chat_id])
	        if xu > 0:
	            list_four = "\n".join(list4[chat_id])
	            reply2("LIST 4")
	            reply2(list_four)
	        xu = len(list5[chat_id])
	        if xu > 0:
	            list_five = "\n".join(list5[chat_id])
	            reply2("LIST 5")
	            reply2(list_five)
	        xu = len(list6[chat_id])
	        if xu > 0:
	            list_six = "\n".join(list6[chat_id])
	            reply2("LIST 6")
	            reply2(list_six)
	        xu = len(list7[chat_id])
	        if xu > 0:
	            list_seven = "\n".join(list7[chat_id])
	            reply2("LIST 7")
	            reply2(list_seven)
	        xu = len(list8[chat_id])
	        if xu > 0:
	            list_eight = "\n".join(list8[chat_id])
	            reply2("LIST 8")
	            reply2(list_eight)
	        xu = len(list9[chat_id])
	        if xu > 0:
	            list_nine = "\n".join(list9[chat_id])
	            reply2("LIST 9")
	            reply2(list_nine)
	        xu = len(list10[chat_id])
	        if xu > 0:
	            list_ten = "\n".join(list10[chat_id])
	            reply2("LIST 10")
	            reply2(list_ten)
	        xu = len(list11[chat_id])
	        if xu > 0:
	            list_eleven = "\n".join(list11[chat_id])
	            reply2("LIST 11")
	            reply2(list_eleven)
	        xu = len(list12[chat_id])
	        if xu > 0:
	            list_twelve = "\n".join(list12[chat_id])
	            reply2("LIST 12")
	            reply2(list_twelve)
	        xu = len(list13[chat_id])
	        if xu > 0:
	            list_thirteen = "\n".join(list13[chat_id])
	            reply2("LIST 13")
	            reply2(list_thirteen)
	        xu = len(list14[chat_id])
	        if xu > 0:
	            list_fourteen = "\n".join(list14[chat_id])
	            reply2("LIST 14")
	            reply2(list_fourteen)
	        xu = len(list15[chat_id])
	        if xu > 0:
	            list_fifteen = "\n".join(list15[chat_id])
	            reply2("LIST 15")
	            reply2(list_fifteen)
