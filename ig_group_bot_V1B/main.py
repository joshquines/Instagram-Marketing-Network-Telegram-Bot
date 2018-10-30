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
import time
from collections import defaultdict

# for sending images
from PIL import Image
import multipart

# standard app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2

#VARIABLES
OUTGOING_WEBHOOK = 'SLACK OUTGOING WEBHOOK GOES HERE'


def bot_talk(msg=None, img=None):
    if msg:
        resp = urllib2.urlopen(OUTGOING_WEBHOOK, urllib.urlencode({
            'text': msg.encode('utf-8'),
            'attachments': [ "text": 'pls' ]
            'disable_web_page_preview': 'true',
            #'reply_to_message_id': str(message_id),
        })).read()
        var slack_payload = {
        "attachments": [
        {
         "text": pls1
        }
        ]
        };
        slack_options = {
        'method': 'post',
        'payload': JSON.stringify(slack_payload)
        };



TOKEN = 'TELEGRAM TOKEN GOES HERE'
IG_TOKEN = 'IG TOKEN GOES HERE' 

BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

admins = ['TELEGRAM ADMINS HERE']
black_leech = []
endthelist = []
likers_list = []
yo_this = ['-1001066225659']
mainlist = defaultdict(list)
list1 = []
in_list = []
donelist = []
leechlist = []
fromlist = []
telelist = []
blacklist = []
chatList = ['-1001081667369','-1001066225659','-1001066225659']
herelist = []
otherlist = []
fllist = []
usernames = []
mplist = []
loltry = []
leera = []
userdrop = True
x = 0
excl =  u"\u203C"

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

#==================================================================================================================================================

class autolist(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        for p in yo_this:
            chat_id = p
            def reply2(msg=None, img=None):
                if msg:
                    resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                        'chat_id': str(chat_id),
                        'text': msg.encode('utf-8'),
                        #'disable_web_page_preview': 'true',
                        #'reply_to_message_id': str(message_id),
                    })).read() 
            #random.shuffle(list1)
            bla = len(list1) - 2
            list1.insert(bla, '@salt.vault')
        #FL LIST
            ul = len(usernames)
            while ul > 0:
                usernames.pop()
                ul -= 1
            a = len(list1)
            count = 0
            b = 1
            total = a/200 + 1
            if a % 200 == 0:
                total == a/200
            opo = str(total)
            for p in list1:
                k = list1[count]
                usernames.append(k)
                ul = len(usernames)
                count += 1 
                if ul == 201:
                    listit = "\n".join(usernames)
                    num = str(b)
                    reply2('F L - L I S T [' + num + '/' + opo + ']\n' + listit)
                    #time.sleep (50.0 / 1000.0)
                    b += 1
                    while ul > 0:
                        usernames.pop()
                        ul -= 1
            listit = "\n".join(usernames)
            num = str(b)
            if listit:
                reply2('F L - L I S T [' + num + '/' + opo + ']\n' + listit)
            #time.sleep (100.0 / 1000.0)

            #MP LIST
            for p in list1:
                mplist.append(p[1:])
            ul = len(usernames)
            while ul > 0:
                usernames.pop()
                ul -= 1
            a = len(mplist)
            count = 0
            b = 1
            total = a/200 + 1
            if a % 200 == 0:
                total == a/200
            opo = str(total)
            for p in mplist:
                k = mplist[count]
                usernames.append(k)
                ul = len(usernames)
                count += 1 
                if ul == 200:
                    listit = "\n".join(usernames)
                    num = str(b)
                    reply2('M P - L I S T [' + num + '/' + opo + ']\n' + listit)
                    #time.sleep (50.0 / 1000.0)
                    b += 1
                    while ul > 0:
                        usernames.pop()
                        ul -= 1
            listit = "\n".join(usernames)
            num = str(b)
            if listit:
                reply2('M P - L I S T [' + num + '/' + opo + ']\n' + listit)
            #time.sleep (50.0 / 1000.0)

            #S P L I T LIST
            ul = len(usernames)
            while ul > 0:
                usernames.pop()
                ul -= 1
            a = len(list1)
            count = 0
            b = 1
            total = a/16 + 1
            if a % 16 == 0:
                total = a/16

            opo = str(total)
            for p in list1:
                k = list1[count]
                usernames.append(k)
                ul = len(usernames)
                count += 1 
                if ul == 16:
                    listit = "\n".join(usernames)
                    num = str(b)
                    reply2('S P L I T - L I S T [' + num + '/' + opo + ']\n' + listit)
                    #time.sleep (50.0 / 1000.0)
                    b += 1
                    while ul > 0:
                        usernames.pop()
                        ul -= 1
            listit = "\n".join(usernames)
            num = str(b)
            if listit:
                reply2('S P L I T - L I S T [' + num + '/' + opo + ']\n' + listit)
            #time.sleep (50.0 / 1000.0)
            reply2('L I K E  A L L  L A T E S T  P I C S\n \n*FL List only if you use FL\n*MP List only if you use MP\n*All Split Lists if manual*\n\n*****\nTHERE IS NO MORE NEED TO D\nOnly D if you engaged with a different account, follow this EXACT format:\n\nD @droppedIG engaged with @engaged\n\nYou have 1.5 hours to engage\n2 hours for the 3PM ET round\n\nLeech checks are now automated and run by the bot to ensure that rounds are leech-free\nAny current leechers will be banned at the end of the round')
            global userdrop
            userdrop = False

#==================================================================================================================================================

class clearbl(webapp2.RequestHandler):
    def get(self):
        for p in blacklist:
            blacklist.pop()
        for p in chatList:
            chat_id = p 
            def reply123(msg=None, img=None):
                if msg:
                    resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                        'chat_id': str(chat_id),
                        'text': msg.encode('utf-8'),
                        #'disable_web_page_preview': 'true',
                        #'reply_to_message_id': str(message_id),
        })).read()        
            reply123('Blacklist Cleared')        

class end(webapp2.RequestHandler):
    global userdrop
    userdrop = False    
    def get(self):
        for p in chatList:
            chat_id = p
            def reply8(msg=None, img=None):
                if msg:
                    resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                        'chat_id': str(chat_id),
                        'text': msg.encode('utf-8'),
                        'disable_web_page_preview': 'true',
                        #'reply_to_message_id': str(message_id),
        })).read()
            p = len(mainlist)
            if p > 0:
                            #FORGOT THIS
                urlfetch.set_default_fetch_deadline(60)
                url = "https://api.instagram.com/v1/users/self/media/recent/?access_token="+IG_TOKEN
                conn = urllib2.urlopen(url)
                raw = conn.read()
                data = json.loads(raw)
                for photo in data["data"]:
                    med_id = photo["id"]
                    break
                MEDIA_ID = str(med_id)

                #POPULATE LIST
                url = "https://api.instagram.com/v1/media/"+ MEDIA_ID +"/likes?access_token=" + IG_TOKEN
                conn = urllib2.urlopen(url)
                raw = conn.read()
                data = json.loads(raw)
                try:
                    for photo in data["data"]:
                        the_likers = photo["username"]
                        if the_likers not in likers_list:
                            likers_list.append(the_likers)
                except KeyError:
                    reply8('No Likers')

                #CHECK IF IN_LIST IN INSTA_LIST
                #REMOVE USERNAME IF IN INSTA_LIST
                a = len(in_list)
                if a > 0:
                    try:
                        for p in in_list:
                            if p in likers_list:
                                del mainlist[p]
                                in_list.remove(p)
                            x = mainlist[p]
                            y = str(x)
                            #endthelist.append(y)
                    except KeyError:
                        reply8('Finish up')
                    for k,v in mainlist.iteritems():               # will become d.items() in py3k
                        joiner = "%s - %s" % (str(k), str(v))
                        endthelist.append(joiner)
                end_list = "\n".join(endthelist)
                reply8(excl + ' Round has ended. \n\nStill Missing From:\n' + end_list + '\n\nLeech checks are automated but >> we will manually check anyone left on this list << and will ban if they are missing likes.\n\n**Next round is in 1 hour')
            else:
                reply8(excl + ' Round has ended. If you haven\'t finished by now, you may be blacklisted.\n\n**Next round is in 1 hour')

class late(webapp2.RequestHandler):
    global userdrop
    userdrop = False   
    def get(self):
        for p in chatList:
            chat_id = p
            def reply345(msg=None, img=None):
                if msg:
                    resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                        'chat_id': str(chat_id),
                        'text': msg.encode('utf-8'),
                        'disable_web_page_preview': 'true',
                        #'reply_to_message_id': str(message_id),
        })).read()
            x = len(endthelist)
            while x > 0: 
                endthelist.pop()
                x -= 1
            p = len(mainlist)
            if p > 0:
                            #FORGOT THIS
                urlfetch.set_default_fetch_deadline(60)
                url = "https://api.instagram.com/v1/users/self/media/recent/?access_token="+IG_TOKEN
                conn = urllib2.urlopen(url)
                raw = conn.read()
                data = json.loads(raw)
                for photo in data["data"]:
                    med_id = photo["id"]
                    break
                MEDIA_ID = str(med_id)

                #POPULATE LIST
                url = "https://api.instagram.com/v1/media/"+ MEDIA_ID +"/likes?access_token=" + IG_TOKEN
                conn = urllib2.urlopen(url)
                raw = conn.read()
                data = json.loads(raw)
                try:
                    for photo in data["data"]:
                        the_likers = photo["username"]
                        if the_likers not in likers_list:
                            likers_list.append(the_likers)
                except KeyError:
                    reply345('No Likers')

                #CHECK IF IN_LIST IN INSTA_LIST
                #REMOVE USERNAME IF IN INSTA_LIST
                a = len(in_list)
                if a > 0:
                    try:
                        for p in in_list:
                            if p in likers_list:
                                del mainlist[p]
                                in_list.remove(p)
                            x = mainlist[p]
                            y = str(x)
                            #endthelist.append(y)
                    except KeyError:
                        reply345('Finish up')
                    for k,v in mainlist.iteritems():               # will become d.items() in py3k
                        joiner = "%s - %s" % (str(k), str(v))
                        endthelist.append(joiner)
                end_list = "\n".join(endthelist)
                reply345(excl + ' This is 20 minutes after the round. \n\nStill Missing From:\n' + end_list + '\n\nLeech checks are automated but >> we will manually check anyone left on this list <<\nAnyone on this list that has is missing likes will be banned and must pay the unban fee to get back in. No excuses. This is way past the end of round')
            else:
                reply345(excl + ' This is 20 minutes after the round. \n\nLeech checks are automated but >> we will manually check anyone left on this list <<\nAnyone on this list that has is missing likes will be banned and must pay the unban fee to get back in. No excuses. This is way past the end of round')

class onehour(webapp2.RequestHandler):
    def get(self):
        global userdrop
        userdrop = True 
        for p in chatList:
            chat_id = p
            def reply10(msg=None, img=None):
                if msg:
                    resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                        'chat_id': str(chat_id),
                        'text': msg.encode('utf-8'),
                        #'disable_web_page_preview': 'true',
                        #'reply_to_message_id': str(message_id),
        })).read()
            reply10('NR in 10 minutes\nGet ready!\n\nLet people know a round is happening!\n')

class forty(webapp2.RequestHandler):
    def get(self):
        for p in chatList:
            chat_id = p
            def reply9(msg=None, img=None):
                if msg:
                    resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                        'chat_id': str(chat_id),
                        'text': msg.encode('utf-8'),
                        #'disable_web_page_preview': 'true',
                        #'reply_to_message_id': str(message_id),
        })).read()
            reply9('*30 minutes till next round\nRound starts at :30\nGet ready!\n\nLet people know a round is about to happen!\n')

class keepdropping(webapp2.RequestHandler):
    global userdrop
    userdrop = True      
    def get(self):
        for p in chatList:
            chat_id = p
            def reply101(msg=None, img=None):
                if msg:
                    resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                        'chat_id': str(chat_id),
                        'text': msg.encode('utf-8'),
                        #'disable_web_page_preview': 'true',
                        #'reply_to_message_id': str(message_id),
        })).read()
            reply101('KEEP DROPPING\nLET PEOPLE KNOW A DROP IS HAPPNING NOW')
#==================================================================================================================================================
htrue = []

class autostart(webapp2.RequestHandler):
    global userdrop
    userdrop = True      
    def get(self):
        #a = len(mainlist)
        #while a > 0:
        #    mainlist.pop()
        #    a -= 1
        a = len(list1)
        mainlist.clear()
        while a > 0:
            list1.pop()
            a -= 1
        a = len(fllist)    
        while a > 0:
            fllist.pop()
            a -= 1
        a = len(fromlist)
        while a > 0:
            fromlist.pop()
            a -= 1
        a = len(mplist)    
        while a > 0:
            mplist.pop()
            a -= 1 
        a = len(loltry)
        while a > 0:
            loltry.pop() 
            a -= 1
        a = len(endthelist)
        while a > 0:
            endthelist.pop() 
            a -= 1
        a = len(in_list)
        while a > 0:
            in_list.pop()
            a -= 1
        a = len(likers_list)
        list1.append('@auralapse')
        #list1.append('@thequot3s')
        list1.append('@HELLOZOLLARICE')
        #list1.append('@destinationing')
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
            global userdrop
            userdrop = True        
            reply3(excl + 'DROP DROP DROP DROP DROP\nRound Is Starting! Drop your @usernames now\nDo NOT add anything after @username\nList will drop in 30 minutes\n**If you can\'t make this round but you entered, just enter /remove @username')  

#==================================================================================================================================================
class clearlist(webapp2.RequestHandler):
    def get(self):
        a = len(likers_list)
        while a > 0:
            likers_list.pop()
            a -= 1

class leech(webapp2.RequestHandler):
    def get(self):
        global userdrop
        userdrop = False     
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
            #FORGOT THIS
            urlfetch.set_default_fetch_deadline(60)
            url = "https://api.instagram.com/v1/users/self/media/recent/?access_token="+IG_TOKEN
            conn = urllib2.urlopen(url)
            raw = conn.read()
            data = json.loads(raw)
            for photo in data["data"]:
                med_id = photo["id"]
                break
            MEDIA_ID = str(med_id)

            #POPULATE LIST
            url = "https://api.instagram.com/v1/media/"+ MEDIA_ID +"/likes?access_token=" + IG_TOKEN
            conn = urllib2.urlopen(url)
            raw = conn.read()
            data = json.loads(raw)
            try:
                for photo in data["data"]:
                    the_likers = photo["username"]
                    if the_likers not in likers_list:
                        likers_list.append(the_likers)
            except KeyError:
                reply4('No Likers')

            #CHECK IF IN_LIST IN INSTA_LIST
            #REMOVE USERNAME IF IN INSTA_LIST
            a = len(in_list)
            if a > 0:
                for p in in_list:
                    if p in likers_list:
                        try:
                            del mainlist[p]
                            in_list.remove(p)
                        except KeyError:
                            reply4('k')
                print_missing = "\n".join(in_list)
                reply4('Usernames Missing:\n' + print_missing + '\n\nIf your name is still on the list and you\'re done liking all, double check with the next list coming up')
            else:
                reply4('NO LEECHERS!')


class WebhookHandler(webapp2.RequestHandler):
    def post(self):
        #us_idr = defaultdict(list)
        #chk = bool
        #chk = False
        #us_idr['username'] = 'null'
        urlfetch.set_default_fetch_deadline(60)
        body = json.loads(self.request.body)
        logging.info('request body:')
        logging.info(body)
        #dataz = json.loads(body)
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

        if 'username' in us_idr:
            us_id = us_idr['username']
        #elif 'username' in message['from']:
        #    us_id = us_idr['username']
        else:
            us_ie = us_idr['id']
            us_id = str(us_ie)
            #us_rd = str(us_rr)
            #us_id = us_rd 

        #try:
        #    us_id = us_idr['username']
        #if 'username' not in dataz:
        #    us_id = us_idr['id']
        #else:
        #    us_id = us_idr['username']
        
        chat = message['chat']
        chat_id = chat['id']
        excl = u'uE252'

        if not text:
            logging.info('no text')
            return
        if chat_id not in chatList:
            otherlist.append(chat_id)
        def reply(msg=None, img=None):
            if msg:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                    'chat_id': str(chat_id),
                    'text': msg.encode('utf-8'),
                    #'disable_web_page_preview': 'true',
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

            elif text == '/!getidyx':
                urlfetch.set_default_fetch_deadline(60)
                url = "https://api.instagram.com/v1/users/self/media/recent/?access_token="+IG_TOKEN
                conn = urllib2.urlopen(url)
                raw = conn.read()
                data = json.loads(raw)

                #if "id" in data["data"]:
                #    med_id = photo["id"]
                #yes = data["data"]
                for photo in data["data"]:
                    med_id = photo["id"]
                    break
                MEDIA_ID = str(med_id)
                #reply(MEDIA_ID)

                url = "https://api.instagram.com/v1/media/"+ MEDIA_ID +"/likes?access_token=" + IG_TOKEN
                conn = urllib2.urlopen(url)
                raw = conn.read()
                data = json.loads(raw)

                a = len(likers_list)
                while a > 0:
                    likers_list.pop()
                    a -= 1
                for photo in data["data"]:
                    the_likers = photo["username"]
                    likers_list.append(the_likers)
                listit = "\n".join(likers_list)
                ks = str(likers_list)
                reply(listit)


            elif text == '/!endcheck':
                p = len(mainlist)
                if p > 0:
                    leechers = "\n".join(mainlist)
                    #reply('Still missing engagement from:\n')
                    #reply(leechers)
                    a = len(leera)
                    while a > 0:
                        leera.pop()
                        a -= 1
                    for n,g in zip(mainlist,fromlist):
                        leera.append('[' + n + ' by: ' + g + ']')
                    #gaaa =  "\n".join(leera) 
                    this = "\n".join(loltry)
                    reply('M I S S I N G \nB A N N I N G:\n' + this)
                else:
                    reply('No Leechers!')
            elif text == '/!manualcheck':
                p = len(mainlist)
                if p > 0:
                    leechers = "\n".join(mainlist)
                    reply('Still missing engagement from:\n' + leechers)
                    #reply('Still missing engagement from:\n')
                    #reply(leechers)
                    #a = len(leera)
                    #while a > 0:
                    #    leera.pop()
                    #    a -= 1
                    #for n,g in zip(mainlist,fromlist):
                    #    leera.append('[' + n + 'by: ' + g + ']')
                    #gaaa =  "\n".join(leera) 
                    #reply('Still missing engagement from:\n' + gaaa)
                else:
                    reply('No Leechers!')
            elif text == '/clearblacklist':
                p = len(blacklist)
                while p > 0:
                    blacklist.pop()
                    p -= 1
                reply('Blacklist cleared')
            elif text == '/telecheck':
                p = len(fromlist)
                if p > 0:
                    leecht = "\n".join(fromlist)
                    reply('Still missing engagement from:\n')
                    reply(leecht)
                else:
                    reply('No Leechers!')
            elif text == '/showblacklist':
                shobl = "\n".join(blacklist)
                reply("BLACKLIST")
                reply(shobl)
            elif text == '/!end':
                if us_id == 'gainsforlife':
                    reply('Round has ended')
            elif text == '/rules':
                reply('*When the bot says drop, drop you @IGusername\n*Do not drop before bot tells you to\n*Do not drop after the bot drops the list\n **If you dropped your name but want to be removed from the list, say /remove @name\nThis is a like only group.\nD @username when you are done engaging the list.\n\n    **You will get a warn if you D wrong and potentially get added to the leechlist\n    **If you complain that you did not get comments, you will get a warn.')
            elif text =='/!listcheck':
                x = "\n".join(in_list)
                reply(x)
            elif text.startswith('/blacklist'):
                blname = text[11:]
                if blname not in blacklist:
                    blacklist.append(blname)
                    reply('Added to blacklist: ' + blname)
                else:
                    reply('Already in blacklist ' + blname)
            elif text.startswith('/unblacklist'):
                blname = text[13:]
                if blname in blacklist:
                    blacklist.remove(blname)
                    reply('Removed from blacklist: ' + blname)
                else:
                    reply('Not in blacklist: ' + blname)
            elif text.startswith('/remove'):
                at = text[8:]
                pla = text[9:]
                with_at = at.lower()
                removename = pla.lower()
                global userdrop
                if userdrop == True:
                    if removename in in_list:
                        in_list.remove(removename)
                        if with_at in list1:
                            list1.remove(with_at)
                        try:
                            del mainlist[removename]
                        except KeyError:
                            reply('Try again')
                        reply('Removed :' + removename)
                    else:
                        reply('Name not on list')  
                else:
                    reply('The round has already started. You must engage [' + with_at + ']')

        # CUSTOMIZE FROM HERE

        elif text.startswith('@'):
            global userdrop
            pla = text
            username = pla
            mpname = username[1:]
            if username == '@globevacations':
                if username not in blacklist: 
                    blacklist.append(username)
            elif ' nc' in username:
                reply('DO NOT PUT NC: ' + username)
            elif ' rc' in username:
                reply('DO NOT INCLUDE ANYTHING AFTER USERNAME: ' + username)
            elif ' RC' in username:
                reply('DO NOT INCLUDE ANYTHING AFTER USERNAME: ' + username)
            elif ' NC' in username:
                reply('DO NOT PUT NC :' + username)
            elif '\n' in username:
                srttt = str(us_id)
                reply('ONLY ENTER ONE USERNAME AT A TIME: \n' + srttt)
            elif mpname not in blacklist:
                if userdrop == True:
                    chat_id = '-1001066225659'
                    if chat_id not in chatList:
                        reply('Dear admin of this group. Remove this bot. It does not belong to you. Fuck you\nJOIN NOW: https://telegram.me/joinchat/D4hos0CdC2PN5QnFGSnTrw')
                    if mpname in in_list:
                        reply('Account already in list: ' + mpname)
                    else:                   
                        #mpname = username[1:]
                        srttt = str(us_id)
                        tele = 'by: @' + srttt
                        fullp = '@' + mpname + ' ' + tele
                        mainlist[mpname].append(tele)
                        in_list.append(mpname)
                        x = len(list1)
                        #full = '[' + username + ' by: ' + tele + ']'
                        #loltry.append(full)
                        if x == 13:

                            list1.append(username)
                        elif x == 16:

                            list1.append(username)
                        elif x == 15:

                            list1.append(username)
                        elif x == 28:

                            list1.append(username)
                        elif x == 6:

                            list1.append(username)
                        elif x == 40:

                            list1.append(username)
                        else:
                            list1.append(username)

                elif userdrop == False:
                    reply('It\'s not time to drop [' + username + ']' )


        elif text.startswith('D @'):
                srttt = str(us_id)
                tele = 'by: @' + srttt
                at = text[2:]
                pla = text[3:]
                with_at = at.lower()
                noat = pla.lower()
                if '\n' in text:
                    reply('Bruh you don\'t have to D unless you enaged with a different account\nhttps://telegram.me/joinchat/D4hos0CdC2PN5QnFGSnTrw')
                    chat_id = '-1001066225659'
                    if chat_id not in chatList:
                        reply('Dear admin of this group. Remove this bot. It does not belong to you.')
                elif 'engaged' in with_at:
                    #if donename in in_list:
                    try:
                        a,b,c,d,e = text.split()
                        donename = b[1:]
                        engaged = e[1:]
                        if donename in in_list:
                            in_list.remove(donename)
                            try:
                                del mainlist[donename]
                            except KeyError:
                                reply('Try again')
                            fullp = engaged + ' ' + tele
                            mainlist[engaged].append(tele)
                            in_list.append(engaged)
                            reply(donename + ' engaged with: ' + engaged + ' '+ tele)   
                        else:
                            reply('Account not found. Check for typo\nhttps://telegram.me/joinchat/D4hos0CdC2PN5QnFGSnTrw')                
                    except ValueError:
                        reply('You did it wrong.\nD @dropped engaged with @gavelikes\nhttps://telegram.me/joinchat/D4hos0CdC2PN5QnFGSnTrw')
                else:
                    reply('You don\'t have to D unless you engaged with a different account. There is an automated leech check that checks leeches via Instagram\nhttps://telegram.me/joinchat/D4hos0CdC2PN5QnFGSnTrw')


        elif text.startswith('!'):
            admin_id = str(us_id)
            if admin_id in admins:
                if text.startswith('!ban'):
                    ya = str(text[5:])
                    kk = ya + ' by: ' + admin_id
                    black_leech.append(kk)
                    reply('Added to banlist')
                elif text == '!forceTrue':
                    userdrop = True
                    reply('TRUUUU FAM')
                elif text == '!forceFalse':
                    userdrop = False
                    reply('NAHHHH FAM')
                elif text == '!showbanlist':
                    listblackleech = "\n".join(black_leech)
                    reply('Currently Banned:\n' + listblackleech)
                elif text.startswith('!updatebanlist'):
                    a = len(black_leech)
                    while a > 0:
                        black_leech.pop()
                        a -= 1
                    appw = text[15:]
                    black_leech.append(appw)
                elif text.startswith('!unbanlist'):
                    if admin_id == 'gainsforlife':
                        remove = text[11:]
                        if remove in black_leech:
                            black_leech.remove(remove)
                            reply('Removed: ' + remove)
                        else:
                            reply('Not in banlist')
                    else:
                        reply('Gains only')
            else:
                reply('Do not use admin commands')
        elif 'next' in text and 'round' in text:
            reply('ROUNDS: 3,6,9,12 AM/PM EASTERN TIME')
        elif 'nr?' in text:
            reply('ROUNDS: 3,6,9,12 AM/PM EASTERN TIME')
        elif text.startswith('nr?'):
            reply('ROUNDS: 3,6,9,12 AM/PM EASTERN TIME')
        elif text.startswith('Nr?'):
            reply('ROUNDS: 3,6,9,12 AM/PM EASTERN TIME')
        elif text.startswith('NR?'):
            reply('ROUNDS: 3,6,9,12 AM/PM EASTERN TIME')
        elif 'when' in text and 'next' in text:
            reply('ROUNDS: 3,6,9,12 AM/PM EASTERN TIME')
        elif 'whatptime' in text:
            reply('look at the corner of your screen!')
        elif 'done' in text and 'all' in text:
            reply('If your name is still on the list and you\'re done liking all, double check with the next list coming up')

        elif text == 'zinitbot!':
            chatList.append(chat_id)
            yo_this.append(chat_id)
            reply('Done!')
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
    ('/auto_list', autolist),
    ('/auto_end', end),
    ('/auto_leech', leech),
    ('/auto_onehour', onehour),
    ('/auto_forty', forty),
    ('/auto_clearbl', clearbl),
    ('/auto_clearlist', clearlist),
    ('/auto_keepdropping', keepdropping),
    ('/auto_late', late),
    ('/auto_start', autostart)
], debug=True)
