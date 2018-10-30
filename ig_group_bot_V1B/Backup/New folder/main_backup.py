import StringIO
import json
import logging
import random
import urllib
import urllib2
import time


# for sending images
from PIL import Image
import multipart

# standard app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2

TOKEN = '253523598:AAEorvsOBGTFLUktkHM6L96KXo2SiA3b_gw'

BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

#Global Variables
mainlist = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list_counter = 0


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
        date = message.get('date')
        text = message.get('text')
        fr = message.get('from')
        chat = message['chat']
        chat_id = chat['id']

        if not text:
            logging.info('no text')
            return

        def reply(msg=None, img=None):
            if msg:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                    'chat_id': str(chat_id),
                    'text': msg.encode('utf-8'),
                    'disable_web_page_preview': 'true',
                    'reply_to_message_id': str(message_id),
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

        if text.startswith('/'):
            if text == '/start':
                reply('Bot enabled')
                setEnabled(chat_id, True)
            elif text == '/zero':
                list_counter = 0
            elif text == '/stop':
                reply('Bot disabled')
                setEnabled(chat_id, False)
            elif text == '/image':
                img = Image.new('RGB', (512, 512))
                base = random.randint(0, 16777216)
                pixels = [base+i*j for i in range(512) for j in range(512)]  # generate sample image
                img.putdata(pixels)
                output = StringIO.StringIO()
                img.save(output, 'JPEG')
                reply(img=output.getvalue())
            elif '@globevacations' in text:
                reply('blacklisted')
            elif text.startswith('/zzrop'):
                username = text[6:]
                mainlist.append(username)
                list_one =  "\n".join(mainlist)
                reply(list_one)
            elif text == '/print_list_2':
                reply("printing")
            else:
                reply('What command?')
        # CUSTOMIZE FROM HERE
        elif text.startswith('9'):
            anotherstring = text[1:]
            list4.append(anotherstring)
            list_four =  "\n".join(list4)
            reply(list_four)
        elif text.startswith('8'):
            username = text[1:]
            mainlist.append(username)
            #reply("debug before check")
            if x < 10:
                list1.append(username)
                reply("one")
            elif x == 10:
                list1.append(username)
                reply("one")
            elif x == 11:
                reply("one")
                list1.append(username)
            elif x > 11 and x < 21:
                list1.append(username)
                reply("one")
            elif x == 21:
                list2.append("username2") #22
                list1.append(username)
            elif x == 22:
                reply("two")
                list2.append("username2")
                list2.append(username)
            elif x == 23:
                list2.append("username2")
                list2.append(username)
            elif x == 24:
                list2.append("username2")
                list2.append(username)
            elif x == 25:
                list2.append("username2")
                list2.append(username)
            elif x > 25 and x < 30:
                list2.append(username)
            elif x == 30:
                list2.append(username)
            elif x == 31:
                list2.append(username)
            elif x == 32:
                list2.append("username2")
                list2.append(username)
            elif x == 33:
                list2.append("username2")
                list2.append(username)
            elif x > 33 and x < 40:
                list2.append(username)
            elif x == 40:
                list3.append("username2")
                list3.append(username)
            elif x > 41 and x < 61:
                list3.append(username)
            elif x > 60 and x < 80:
                list4.append(username)
            elif x == 80:
                list4.append("username2")
                list4.append(username)
            elif x == 81:
                list5.append("username2")
                list5.append(username)
            elif x == 82:
                list5.append("username2")
                list5.append(username)
            elif x > 82 and x < 101:
                list5.append(username)
            elif x == 100:
                list6.append("username2")
                list6.append(username)
            elif x > 100 and x < 121:
                list7.append(username)
            else:
                list10.append(username)
        elif text == ('drop_list'):
            reply('why')
            one = len(list1)
            y = str(one)
            reply(y)
            reply('debug')
            two = len(list2)
            three = len(list3)
            four = len(list4)
            five = len(list5)
            six = len(list6)
            seven = len(list7)
            if one > 0:
                list_one = "\n".join(list1)
                reply(list_one)
            if two > 0:
                list_two = "\n".join(list2)
                reply(list_two)                
        elif text == ('print_list_1'):
            list_one = "\n".join(list1)
            list_two = "\n".join(list2)
            reply(list_one)
            reply(list_two)
        elif 'yas' in text:
            reply('yaaaaaaaasssss')
        elif 'pls' in text:
            reply('this is just drop')
        elif 'who are you' in text:
            reply('The best')
        elif 'what time' in text:
            reply('look at the corner of your screen!')
        else:
            countz = 0
        def addList(msg=None, img=None):
            if text.startswith('@'):
                reply("yes")


app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
], debug=True)
