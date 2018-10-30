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

TOKEN = '283356090:AAEGeLiDfyPjexQeRS2g-NacPuJljlX8r-0'

BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

mainlist = defaultdict(list)
list1 = defaultdict(list)
list2 = defaultdict(list)
list3 = defaultdict(list)
list4 = defaultdict(list)
list5 = defaultdict(list)
list6 = defaultdict(list)
list7 = defaultdict(list)
list8 = defaultdict(list)
list9 = defaultdict(list)
list10 = defaultdict(list)
list11 = defaultdict(list)
list12 = defaultdict(list)
list13 = defaultdict(list)
list14 = defaultdict(list)
list15 = defaultdict(list)
donelist = defaultdict(list)
leechlist = defaultdict(list)
fromlist = defaultdict(list)
telelist = defaultdict(list)
blacklist = []
herelist = defaultdict(list)
x = 0

def bot_talk(msg=None, img=None):
    if msg:
        for p in chatList:
            chat_id = p 
            resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                'chat_id': str(chat_id),
                'text': msg.encode('utf-8'),
                'disable_web_page_preview': 'true',
                #'reply_to_message_id': str(message_id),
            })).read()


class autostart(webapp2.RequestHandler):
    def post(self):
        for p in chatList:
            chat_id = p
            def reply3(msg=None, img=None):
                if msg:
                    resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                        'chat_id': str(chat_id),
                        'text': msg.encode('utf-8'),
                        'disable_web_page_preview': 'true',
                        #'reply_to_message_id': str(message_id),
        })).read()
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
            reply3('Round Is Starting. Drop your @usernames now\n    add NC for no comment eg: @username NC')  




# ================================

class EnableStatus(ndb.Model):
    # key name: str(chat_id)
    enabled = ndb.BooleanProperty(indexed=False, default=False)


# ================================

def setEnabled(chat_id, yes):
    es = EnableStatus.get_or_insert(str(chat_id))
    es.enabled = yes
    es.put()

def getEnabled(chat_id):
    es = EnableStatus.get_by_id(str(chat_id))
    if es:
        return es.enabled
    return False


# ================================

class MeHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getMe'))))


class GetUpdatesHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getUpdates'))))


class SetWebhookHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        url = self.request.get('url')
        if url:
            self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'setWebhook', urllib.urlencode({'url': url})))))


class WebhookHandler(webapp2.RequestHandler):
    def post(self):
        urlfetch.set_default_fetch_deadline(60)
        body = json.loads(self.request.body)
        logging.info('request body:')
        logging.info(body)
        self.response.write(json.dumps(body))

        update_id = body['update_id']
        try:
            message = body['message']
        except:
            message = body['edited_message']
        message_id = message.get('message_id')
        #us_id = message['id']
        date = message.get('date')
        text = message.get('text')
        us_idr = message.get('from')
        us_id = us_idr['first_name']
        chat = message['chat']
        chat_id = chat['id']
        excl = u'uE252'

        if not text:
            logging.info('no text')
            return

        def reply(msg=None, img=None):
            if msg:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                    'chat_id': str(chat_id),
                    'text': msg.encode('utf-8'),
                    'disable_web_page_preview': 'true',
                    #'reply_to_message_id': str(message_id),
                })).read()
            elif img:
                resp = multipart.post_multipart(BASE_URL + 'sendPhoto', [
                    ('chat_id', str(chat_id)),
                    ('reply_to_message_id', str(message_id)),
                ], [
                    ('photo', 'image.jpg', img),
                ])
            else:
                logging.error('no msg or img specified')
                resp = None

            logging.info('send response:')
            logging.info(resp)
        if text == ('/triggertest'):
            reply('trigger test is working.')
            reply('ROUND IS STARTING:\nEnter: \n    @lowercase for likes only\n@CAPITALS for likes and comments (4+ words) \nFor multiple usernames, enter them separately \nList will drop in around 20 minutes.')
        if text.startswith('/'):
            if text == '/start':
                reply('Bot enabled')
                setEnabled(chat_id, True)
            elif text == '/stop':
                reply('Bot disabled')
                setEnabled(chat_id, False)
            elif text == '/justdo':
                reply('i really did shit')
            elif text == "/startround":
                reply('Round Is Starting. Drop your @usernames now\n    add NC for no comment eg: @username NC\n    NC also means you will not receive comment\n\nIF USING MULTIPLE ACCOUNTS, DROP SEPARATELY\n\nComments must be 4+ words') 
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
                while a > 0:
                    list13[chat_id].pop()
                    a -= 1
                while a > 0:
                    list14[chat_id].pop()
                    a -= 1
                while a > 0:
                    list15[chat_id].pop()
                    a -= 1
                a = len(fromlist[chat_id])
                while a > 0:
                    fromlist[chat_id].pop()
                    a -= 1
            elif text == "/list":
                reply('When done, say D @username.\n    If you added NC, include the NC eg: D @username NC\n\nMust enter usernames separate lines\nIf you engaged with a different account, say D @droppedIG then reply to that comment with \'engaged with @engageIG\'\nFailure to follow these rules may result in a ban')
                xu = len(mainlist[chat_id])
                if xu < 15:
                    list_one = "\n".join(list1[chat_id])
                    reply("LIST 1")
                    reply(list_one)
                elif xu < 30:
                    list_one = "\n".join(list1[chat_id])
                    reply("LIST 1")
                    reply(list_one)                    
                    list_two = "\n".join(list2[chat_id])
                    reply("LIST 2")
                    reply(list_two)
                elif xu < 45:
                    list_one = "\n".join(list1[chat_id])
                    reply("LIST 1")
                    reply(list_one)                    
                    list_two = "\n".join(list2[chat_id])
                    reply("LIST 2")                    
                    list_three = "\n".join(list3[chat_id])
                    reply("LIST 3")
                    reply(list_three)
                elif xu < 60:
                    list_one = "\n".join(list1[chat_id])
                    reply("LIST 1")
                    reply(list_one)                    
                    list_two = "\n".join(list2[chat_id])
                    reply("LIST 2")                    
                    list_three = "\n".join(list3[chat_id])
                    reply("LIST 3")
                    reply(list_three)                    
                    list_four = "\n".join(list4[chat_id])
                    reply("LIST 4")
                    reply(list_four)
                elif xu < 75:
                    list_one = "\n".join(list1[chat_id])
                    reply("LIST 1")
                    reply(list_one)                    
                    list_two = "\n".join(list2[chat_id])
                    reply("LIST 2")                    
                    list_three = "\n".join(list3[chat_id])
                    reply("LIST 3")
                    reply(list_three)  
                    list_four = "\n".join(list4[chat_id])
                    reply("LIST 4")
                    reply(list_four)                                      
                    list_five = "\n".join(list5[chat_id])
                    reply("LIST 5")
                    reply(list_five)
                elif xu < 90:
                    list_one = "\n".join(list1[chat_id])
                    reply("LIST 1")
                    reply(list_one)                    
                    list_two = "\n".join(list2[chat_id])
                    reply("LIST 2")                    
                    list_three = "\n".join(list3[chat_id])
                    reply("LIST 3")
                    reply(list_three) 
                    list_four = "\n".join(list4[chat_id])
                    reply("LIST 4")
                    reply(list_four)                                       
                    list_five = "\n".join(list5[chat_id])
                    reply("LIST 5")                   
                    list_six = "\n".join(list6[chat_id])
                    reply("LIST 6")
                    reply(list_six)
                elif xu < 105:
                    list_one = "\n".join(list1[chat_id])
                    reply("LIST 1")
                    reply(list_one)                    
                    list_two = "\n".join(list2[chat_id])
                    reply("LIST 2")                    
                    list_three = "\n".join(list3[chat_id])
                    reply("LIST 3")
                    reply(list_three) 
                    list_four = "\n".join(list4[chat_id])
                    reply("LIST 4")
                    reply(list_four)                                       
                    list_five = "\n".join(list5[chat_id])
                    reply("LIST 5")                   
                    list_six = "\n".join(list6[chat_id])
                    reply("LIST 6")
                    reply(list_six)                    
                    list_seven = "\n".join(list7[chat_id])
                    reply("LIST 7")
                    reply(list_seven)
                elif xu < 120:
                    list_one = "\n".join(list1[chat_id])
                    reply("LIST 1")
                    reply(list_one)                    
                    list_two = "\n".join(list2[chat_id])
                    reply("LIST 2")                    
                    list_three = "\n".join(list3[chat_id])
                    reply("LIST 3")
                    reply(list_three) 
                    list_four = "\n".join(list4[chat_id])
                    reply("LIST 4")
                    reply(list_four)                                       
                    list_five = "\n".join(list5[chat_id])
                    reply("LIST 5")                   
                    list_six = "\n".join(list6[chat_id])
                    reply("LIST 6")
                    reply(list_six)                    
                    list_seven = "\n".join(list7[chat_id])
                    reply("LIST 7")                    
                    list_eight = "\n".join(list8[chat_id])
                    reply("LIST 8")
                    reply(list_eight)
                elif xu < 135:
                    list_one = "\n".join(list1[chat_id])
                    reply("LIST 1")
                    reply(list_one)                    
                    list_two = "\n".join(list2[chat_id])
                    reply("LIST 2")                    
                    list_three = "\n".join(list3[chat_id])
                    reply("LIST 3")
                    reply(list_three)
                    list_four = "\n".join(list4[chat_id])
                    reply("LIST 4")
                    reply(list_four)                                        
                    list_five = "\n".join(list5[chat_id])
                    reply("LIST 5")                   
                    list_six = "\n".join(list6[chat_id])
                    reply("LIST 6")
                    reply(list_six)                    
                    list_seven = "\n".join(list7[chat_id])
                    reply("LIST 7")                    
                    list_eight = "\n".join(list8[chat_id])
                    reply("LIST 8")
                    reply(list_eight)                    
                    list_nine = "\n".join(list9[chat_id])
                    reply("LIST 9")
                    reply(list_nine)
                elif xu < 150:
                    list_one = "\n".join(list1[chat_id])
                    reply("LIST 1")
                    reply(list_one)                    
                    list_two = "\n".join(list2[chat_id])
                    reply("LIST 2")                    
                    list_three = "\n".join(list3[chat_id])
                    reply("LIST 3")
                    reply(list_three) 
                    list_four = "\n".join(list4[chat_id])
                    reply("LIST 4")
                    reply(list_four)                                       
                    list_five = "\n".join(list5[chat_id])
                    reply("LIST 5")                   
                    list_six = "\n".join(list6[chat_id])
                    reply("LIST 6")
                    reply(list_six)                    
                    list_seven = "\n".join(list7[chat_id])
                    reply("LIST 7")                    
                    list_eight = "\n".join(list8[chat_id])
                    reply("LIST 8")
                    reply(list_eight)                    
                    list_nine = "\n".join(list9[chat_id])
                    reply("LIST 9")
                    reply(list_nine)                    
                    list_ten = "\n".join(list10[chat_id])
                    reply("LIST 10")
                    reply(list_ten)
                elif xu < 165:
                    list_one = "\n".join(list1[chat_id])
                    reply("LIST 1")
                    reply(list_one)                    
                    list_two = "\n".join(list2[chat_id])
                    reply("LIST 2")                    
                    list_three = "\n".join(list3[chat_id])
                    reply("LIST 3")
                    reply(list_three) 
                    list_four = "\n".join(list4[chat_id])
                    reply("LIST 4")
                    reply(list_four)                                       
                    list_five = "\n".join(list5[chat_id])
                    reply("LIST 5")                   
                    list_six = "\n".join(list6[chat_id])
                    reply("LIST 6")
                    reply(list_six)                    
                    list_seven = "\n".join(list7[chat_id])
                    reply("LIST 7")                    
                    list_eight = "\n".join(list8[chat_id])
                    reply("LIST 8")
                    reply(list_eight)                    
                    list_nine = "\n".join(list9[chat_id])
                    reply("LIST 9")
                    reply(list_nine)                    
                    list_ten = "\n".join(list10[chat_id])
                    reply("LIST 10")
                    reply(list_ten)
                    list_eleven = "\n".join(list11[chat_id])
                    reply("LIST 11")
                    reply(list_eleven)
                elif xu < 180:
                    list_one = "\n".join(list1[chat_id])
                    reply("LIST 1")
                    reply(list_one)                    
                    list_two = "\n".join(list2[chat_id])
                    reply("LIST 2")                    
                    list_three = "\n".join(list3[chat_id])
                    reply("LIST 3")
                    reply(list_three)   
                    list_four = "\n".join(list4[chat_id])
                    reply("LIST 4")
                    reply(list_four)                                     
                    list_five = "\n".join(list5[chat_id])
                    reply("LIST 5")                   
                    list_six = "\n".join(list6[chat_id])
                    reply("LIST 6")
                    reply(list_six)                    
                    list_seven = "\n".join(list7[chat_id])
                    reply("LIST 7")                    
                    list_eight = "\n".join(list8[chat_id])
                    reply("LIST 8")
                    reply(list_eight)                    
                    list_nine = "\n".join(list9[chat_id])
                    reply("LIST 9")
                    reply(list_nine)                    
                    list_ten = "\n".join(list10[chat_id])
                    reply("LIST 10")
                    reply(list_ten)
                    list_eleven = "\n".join(list11[chat_id])
                    reply("LIST 11")
                    reply(list_eleven)                    
                    list_twelve = "\n".join(list12[chat_id])
                    reply("LIST 12")
                    reply(list_twelve)
                elif xu < 195:
                    list_one = "\n".join(list1[chat_id])
                    reply("LIST 1")
                    reply(list_one)                    
                    list_two = "\n".join(list2[chat_id])
                    reply("LIST 2")                    
                    list_three = "\n".join(list3[chat_id])
                    reply("LIST 3")
                    reply(list_three) 
                    list_four = "\n".join(list4[chat_id])
                    reply("LIST 4")
                    reply(list_four)                                       
                    list_five = "\n".join(list5[chat_id])
                    reply("LIST 5")                   
                    list_six = "\n".join(list6[chat_id])
                    reply("LIST 6")
                    reply(list_six)                    
                    list_seven = "\n".join(list7[chat_id])
                    reply("LIST 7")                    
                    list_eight = "\n".join(list8[chat_id])
                    reply("LIST 8")
                    reply(list_eight)                    
                    list_nine = "\n".join(list9[chat_id])
                    reply("LIST 9")
                    reply(list_nine)                    
                    list_ten = "\n".join(list10[chat_id])
                    reply("LIST 10")
                    reply(list_ten)
                    list_eleven = "\n".join(list11[chat_id])
                    reply("LIST 11")
                    reply(list_eleven)                    
                    list_twelve = "\n".join(list12[chat_id])
                    reply("LIST 12")                    
                    list_thirteen = "\n".join(list13[chat_id])
                    reply("LIST 13")
                    reply(list_thirteen)
                elif xu < 210:
                    list_one = "\n".join(list1[chat_id])
                    reply("LIST 1")
                    reply(list_one)                    
                    list_two = "\n".join(list2[chat_id])
                    reply("LIST 2")                    
                    list_three = "\n".join(list3[chat_id])
                    reply("LIST 3")
                    reply(list_three) 
                    list_four = "\n".join(list4[chat_id])
                    reply("LIST 4")
                    reply(list_four)                                       
                    list_five = "\n".join(list5[chat_id])
                    reply("LIST 5")                   
                    list_six = "\n".join(list6[chat_id])
                    reply("LIST 6")
                    reply(list_six)                    
                    list_seven = "\n".join(list7[chat_id])
                    reply("LIST 7")                    
                    list_eight = "\n".join(list8[chat_id])
                    reply("LIST 8")
                    reply(list_eight)                    
                    list_nine = "\n".join(list9[chat_id])
                    reply("LIST 9")
                    reply(list_nine)                    
                    list_ten = "\n".join(list10[chat_id])
                    reply("LIST 10")
                    reply(list_ten)
                    list_eleven = "\n".join(list11[chat_id])
                    reply("LIST 11")
                    reply(list_eleven)                    
                    list_twelve = "\n".join(list12[chat_id])
                    reply("LIST 12")                    
                    list_thirteen = "\n".join(list13[chat_id])
                    reply("LIST 13")
                    reply(list_thirteen)                    
                    list_fourteen = "\n".join(list14[chat_id])
                    reply("LIST 14")
                    reply(list_fourteen)
                elif xu < 250:
                    list_one = "\n".join(list1[chat_id])
                    reply("LIST 1")
                    reply(list_one)                    
                    list_two = "\n".join(list2[chat_id])
                    reply("LIST 2")                    
                    list_three = "\n".join(list3[chat_id])
                    reply("LIST 3")
                    reply(list_three) 
                    list_four = "\n".join(list4[chat_id])
                    reply("LIST 4")
                    reply(list_four)                                       
                    list_five = "\n".join(list5[chat_id])
                    reply("LIST 5")                   
                    list_six = "\n".join(list6[chat_id])
                    reply("LIST 6")
                    reply(list_six)                    
                    list_seven = "\n".join(list7[chat_id])
                    reply("LIST 7")                    
                    list_eight = "\n".join(list8[chat_id])
                    reply("LIST 8")
                    reply(list_eight)                    
                    list_nine = "\n".join(list9[chat_id])
                    reply("LIST 9")
                    reply(list_nine)                    
                    list_ten = "\n".join(list10[chat_id])
                    reply("LIST 10")
                    reply(list_ten)
                    list_eleven = "\n".join(list11[chat_id])
                    reply("LIST 11")
                    reply(list_eleven)                    
                    list_twelve = "\n".join(list12[chat_id])
                    reply("LIST 12")                    
                    list_thirteen = "\n".join(list13[chat_id])
                    reply("LIST 13")
                    reply(list_thirteen)                    
                    list_fourteen = "\n".join(list14[chat_id])
                    reply("LIST 14")                    
                    list_fifteen = "\n".join(list15[chat_id])
                    reply("LIST 15")
                    reply(list_fifteen)
                reply('When done, say D @username.\n    If you added NC, include the NC eg: D @username NC\n\nMust enter usernames separate lines\nIf you engaged with a different account, say D @droppedIG then reply to that comment with \'engaged with @engageIG\'\nFailure to follow these rules may result in a ban')
                reply('Engage on latest photo')
            elif text.startswith('/done'):
                donename = text[5:]
                s = mainlist[chat_id]
                if donename in s:
                    mainlist[chat_id].remove(donename)
            elif text == '/check':
                p = len(mainlist[chat_id])
                if p > 0:
                    leechers = "\n".join(mainlist[chat_id])
                    reply('Still missing engagement from:\n')
                    reply(leechers)
                else:
                    reply('No Leechers!')
            elif text == '/telecheck':
                p = len(fromlist[chat_id])
                if p > 0:
                    leecht = "\n".join(fromlist[chat_id])
                    reply('Still missing engagement from:\n')
                    reply(leecht)
                else:
                    reply('No Leechers!')
            elif text == '/showblacklist':
                shobl = "\n".join(blacklist)
                reply("BLACKLIST")
                reply(shobl)

            elif text == ('/end'):
                reply('Round has ended')
            elif text.startswith('/remove'):
                removename = text[8:]
                tele = us_id
                qw = mainlist[chat_id]
                if removename in qw:
                    mainlist[chat_id].remove(removename)
                qw = fromlist[chat_id]
                if tele in qw:
                    fromlist[chat_id].remove(tele) 
                s = list1[chat_id]
                if removename in s:
                    list1[chat_id].remove(removename)   
                s = list2[chat_id]
                if removename in s:
                    list2[chat_id].remove(removename)
                s = list3[chat_id]
                if removename in s:
                    list3[chat_id].remove(removename)  
                s = list4[chat_id]
                if removename in s:
                    list4[chat_id].remove(removename)  
                s = list5[chat_id]
                if removename in s:
                    list5[chat_id].remove(removename)  
                s = list6[chat_id]
                if removename in s:
                    list6[chat_id].remove(removename) 
                s = list7[chat_id]
                if removename in s:
                    list7[chat_id].remove(removename)      
                s = list8[chat_id]
                if removename in s:
                    list8[chat_id].remove(removename)  
                s = list9[chat_id]
                if removename in s:
                    list9[chat_id].remove(removename)  
                s = list10[chat_id]
                if removename in s:
                    list10[chat_id].remove(removename) 
                s = list11[chat_id]
                if removename in s:
                    list11[chat_id].remove(removename) 
                s = list12[chat_id]
                if removename in s:
                    list12[chat_id].remove(removename)  
                s = list13[chat_id]
                if removename in s:
                    list13[chat_id].remove(removename)     
                s = list14[chat_id]
                if removename in s:
                    list14[chat_id].remove(removename)  
                s = list15[chat_id]
                if removename in s:
                    list15[chat_id].remove(removename)      
            else:
                reply('Not a valid command\n')

        # CUSTOMIZE FROM HERE
        elif text == ('H'):
            herelist[chat_id].append('H')

        elif text.startswith('@'):
            username = text
            if username == '@globevacations':
                if username not in blacklist: 
                    blacklist.append(username)
            else:
                mainlist[chat_id].append(username)
                fromlist[chat_id].append(us_id)
                #reply('appended to main')
                x = len(mainlist[chat_id])
                if x < 15:
                    list1[chat_id].append(username)
                elif x > 14 and x < 20:
                    list2[chat_id].append(username)
                elif x == 20:
                    #list2[chat_id].append('@antininefive')
                    list2[chat_id].append(username)
                    #list2[chat_id].append('@dericiousgarage')
                elif x > 20 and x < 30:
                    list2[chat_id].append(username)
                elif x > 29 and x < 35:
                    list3[chat_id].append(username)
                elif x == 35:
                    #list3[chat_id].append(username)
                    list3[chat_id].append(username)
                elif x > 35 and x < 45:
                    list3[chat_id].append(username)
                elif x > 44 and x < 50:
                    list4[chat_id].append(username)
                elif x == 50:
                    #list4[chat_id].append(username)
                    list4[chat_id].append(username)
                elif x > 50 and x < 60:
                    list4[chat_id].append(username)
                elif x > 59 and x < 65:
                    list5[chat_id].append(username)
                elif x == 65:
                    #list5[chat_id].append(username)
                    list5[chat_id].append(username)
                elif x > 65 and x < 75:
                    list5[chat_id].append(username)
                elif x > 74 and x < 80:
                    list6[chat_id].append(username)
                elif x == 80:
                    #list6[chat_id].append(username)
                    list6[chat_id].append(username)
                elif x > 80 and x < 90:
                    list6[chat_id].append(username)
                elif x > 89 and x < 95:
                    list7[chat_id].append(username)
                elif x == 95:
                    #list7[chat_id].append(username)
                    list7[chat_id].append(username)
                elif x > 95 and x < 105:
                    list7[chat_id].append(username)
                elif x > 104 and x < 110:
                    list8[chat_id].append(username)
                elif x == 110:
                    #list8[chat_id].append(username)
                    list8[chat_id].append(username)
                elif x > 110 and x < 120:
                    list8[chat_id].append(username)
                elif x > 119 and x < 125:
                    list9[chat_id].append(username)
                elif x == 125:
                    #list9[chat_id].append(username)
                    list9[chat_id].append(username)
                elif x > 125 and x < 135:
                    list9[chat_id].append(username)
                elif x > 134 and x < 140:
                    list10[chat_id].append(username)
                elif x == 140:
                    list10[chat_id].append(username)
                elif x > 140 and x < 150:
                    list10[chat_id].append(username)
                elif x > 149 and x < 155:
                    list11[chat_id].append(username)
                elif x == 155:
                    #list11[chat_id].append(username)
                    list11[chat_id].append(username)
                elif x > 155 and x < 165:
                    list11[chat_id].append(username)
                elif x > 164 and x < 170:
                    list12[chat_id].append(username)
                elif x == 170:
                    #list12[chat_id].append(username)
                    list12[chat_id].append(username)
                elif x > 170 and x < 180:
                    list12[chat_id].append(username)
                elif x > 179 and x < 185:
                    list13[chat_id].append(username)
                elif x == 185:
                    #list13[chat_id].append(username)
                    list13[chat_id].append(username)
                elif x > 185 and x < 195:
                    list13[chat_id].append(username)
                elif x > 194 and x < 200:
                    list14[chat_id].append(username)
                elif x == 200:
                    #list14[chat_id].append(username)
                    list14[chat_id].append(username)
                elif x > 200 and x < 210:
                    list14[chat_id].append(username)
                elif x > 209 and x < 215:
                    list15[chat_id].append(username)
                elif x == 215:
                    #list15[chat_id].append(username)
                    list15[chat_id].append(username)
                elif x > 215 and x < 225:
                    list15[chat_id].append(username)


        elif text.startswith('D '):
                donename = text[2:]
                s = mainlist[chat_id]
                if donename in s:
                    mainlist[chat_id].remove(donename)
                mn = fromlist[chat_id]
                tele = us_id 
                if tele in mn:
                    fromlist[chat_id].remove(tele)

        elif 'whatptime' in text:
            reply('look at the corner of your screen!')
        else:
            if getEnabled(chat_id):
                c = 5
            else:
                logging.info('not enabled for chat_id {}'.format(chat_id))


app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
    ('/autostart' , autostart)
], debug=True)
