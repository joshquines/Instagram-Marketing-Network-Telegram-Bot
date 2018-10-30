import telepotNew
import time
import urllib3
import traceback
import datetime
from datetime import datetime
from datetime import timedelta
import time
from collections import defaultdict
import json
import urlfetch 
import urllib
import urllib.request
from urllib.request import urlopen
from pytz import timezone
import schedule
import crontab
import asyncio
import aiocron
from multiprocessing import Process
eastern = timezone('US/Mountain')
eastern2 = timezone('US/Eastern')
import os
import codecs

# GLOBAL VARIABLES
adminList = ['TELEGRAM ADMIN USERNAMES HERE']
approvedList = []
userList = defaultdict(list)

#GLOBALS and CONSTANTS 
TOKEN = 'TELEGRAM BOT TOKEN HERE'
GROUP_ID = -1001348884191
gainsChat = '288201442'

bot = telepotNew.Bot(TOKEN)
approvedAccount = defaultdict(str)

#@asyncio.coroutine
def reminder():
    message = "\n".join([
        "Reminder:",
        "To participate in our ZERO leech network, start a message with:",
        "🔹 1k+ : @infinitycommentsbot",
        "🔹 20k+: @infinity20kbot\n",
        "We also do not tolerate low quality accounts. \nIf you belive there is a low quality account in our network (memes, luxury, nsfw, spam, etc....)",
        #"Report that IG account to @infinityqcbot"
        #"🔹Invite: https://t.me/joinchat/ES2a4lBmVt-wroWO_BKSsA"
        ])
    bot.sendMessage(GROUP_ID, message, disable_web_page_preview=True)
schedule.every(4).hours.do(reminder)

def inviteMore():
    message = "\n".join([
        "Invite: ",
        "https://t.me/joinchat/ES2a4j-YetA34D19PBU42Q"
    ])
    bot.sendMessage(GROUP_ID, message, disable_web_page_preview=True)
schedule.every(1).hours.do(inviteMore)

def handle(msg):
    content_type, chat_type, chat_id = telepotNew.glance(msg)
    print(content_type, chat_type, chat_id)
    identifier = telepotNew.message_identifier(msg)

    # GROUP INSTRUCTIONS
    if chat_id == GROUP_ID:
        if content_type == 'new_chat_member':

            welcome2_0 = "\n".join([
                "Welcome to Infinity!",
                "\nWe are an engagement group catered to content creators and influencers. Whether you're a blogger, artist, photographer, musician, vlogger, traveller, entrepreneur, etc... you\'re welcomed!",
                "\nOur purpose is to get your posts viral and increase your organic exposure to potential new followers and/or clients\n",
                "We currently have 2 tiers:",
                "1k and 20k minimum followers",
                "\nTo get started, start a convo with:",
                "🔹 1k+:  @infinitycommentsbot",
                "🔹 20k+: @infinity20kbot",
                "\nIf you meet the requirements for both bots, you have the option to use both or just one."
            ])

            bot.sendMessage(chat_id, welcome2_0)
        elif content_type == 'text':
            text = msg["text"]
            userID = str(msg["from"]["id"])
            if userID != "288201442":
                print("Not gainsforlife")

                # SPAM CHECK
                spamWords = ['dm me', 'pm me', 'selling']
                if "http" in text.lower() or "t.me" in text.lower():
                    bot.sendMessage(chat_id, "Links get posted on @infinitycommentsbot or @infinity20kbot.\nOpen it up and follow the instructions!")
                    bot.sendMessage(gainsChat, "Attempted spam: " + str(text))
                    bot.deleteMessage(identifier)
                elif any([word in text.lower() for word in spamWords]):
                    bot.deleteMessage(identifier)

                # GROUP COMMANDS
                elif text == "/infinityrules" or text == "/infinityrules@infinitymanagerbot":
                    message = "\n".join([
                        "RULES:",
                        "\nFollowers:",
                        "🔹 1k+ for @infinitycommentsbot",
                        "🔹 20k+ for @infinity20kbot",
                        "\n-> Must have a high quality niche \n(**NOT ALLOWED: memes, luxury, get rich, sales, spam, nsfw, alcohol, weed, drugs, violence, political)",
                        "\n-> Comments must be high quality and relevant.",
                        ])
                    bot.sendMessage(chat_id, message)
                elif text == "/instructions" or text == "/instructions@infinitymanagerbot":
                    message = "\n".join([
                        "Here are the steps:",
                        "-> CLICK: @infinitycommentsbot or @infinity20kbot",
                        "-> Press the start button and follow instructions from there."
                        ])
                    bot.sendMessage(chat_id, message)
                elif text == "/invite" or text == "/invite@infinitymanagerbot":
                    bot.sendMessage(chat_id, "Invite: \nhttps://t.me/joinchat/ES2a4lBmVt-wroWO_BKSsA")
        else:
            bot.deleteMessage(identifier)
    print(content_type, chat_type, chat_id)

print ('Listening ...')
bot.message_loop(handle)

# Keep the program running.
while 1:
    schedule.run_pending()
    time.sleep(1)
