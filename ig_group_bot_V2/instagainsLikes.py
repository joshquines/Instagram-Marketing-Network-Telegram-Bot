import telepot
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
import codecs


#LISTS
chat_idList = ['-1001082178741']
toDrop = []
checkList = []
usernames = []
dropList = []
toCheck = []
splitList = []
dropBlacklist = []
igList = []
endList = defaultdict(str)
warnCount = defaultdict(int)
blacklistCount = defaultdict(int)
endPrint = []
autoWarnList = []
blackList = ['t.me','telegram.me','/joinchat','.gg']
linkWhitelist = ['.com']
userID = defaultdict(str)
authorCheck = defaultdict(str)
dCount = defaultdict(int)

#GLOBALS and CONSTANTS 
canDrop = True
TOKEN = 'TELEGRAM TOKEN HERE'
IG_TOKEN = 'IG TOKEN HERE'
ACTIVE = True 




bot = telepot.Bot(TOKEN)

#@asyncio.coroutine
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        try:
            pr = msg["text"]
            pr = "\n<" + str(pr) + ">"
            print(content_type, chat_type, chat_id, pr)
        except:
            print(content_type, chat_type, chat_id)
    print(content_type, chat_type, chat_id)

    if content_type == 'new_chat_member':
        message = "\n".join([
            "WELCOME TO THE INSTAGAINS NETWORK",
            "Our purpose is to exploit social media algorithms to significantly increase the amount of exposure and rate of growth for accounts\n\n",
            "This is the Instagram LIKE ROUNDS group. \n---> Type !howto to see how to participate in this group!\n\n"
            ])
        bot.sendMessage(chat_id, message)

    global canDrop 
    if content_type == 'text':
        text = msg["text"]
        #bot.sendMessage(chat_id, text)

        # V A R I A B L E S
        try:
            authorUsername = str(msg["from"]["username"])
        except:
            authorUsername = str(msg["from"]["id"])
        authorId = str(msg["from"]["id"])
        chat_id = str(msg["chat"]["id"])
        #bot.sendMessage(chat_id, authorId + " " + authorUsername + " " + str(chat_id))

        #Admin Commands
        if authorUsername == 'gainsforlife':
            if text == '!f':
                bot.sendMessage(chat_id, "okokokok")
                autoCheck()
                autoCompiling()
                autoLeech()
                autoEnd()
                autoLate()
            elif text == '!test':
                bot.sendMessage(chat_id, "test")
                
            elif text == '!init':
                if chat_id not in chat_idList:
                    chat_idList.append(chat_id)
                    bot.sendMessage(chat_id, "Initialized")
            elif text == '!forceFalse':
                canDrop = False
                bot.sendMessage(chat_id, "Nahh fam")
            elif text == '!forceTrue':
                canDrop = True
                bot.sendMessage(chat_id, "Truu fam")
            elif text == '!check':
                autoCheck() 
            elif text == '!compile':
                autoCompiling()
            elif text == '!leech':
                autoLeech()
            elif text == '!end':
                autoEnd() 
            elif text == '!late':
                autoLate()
            elif text == '!drop':
                autoDrop() 
            elif text.startswith('!unblacklist'):
                userWarn = text[14:]
                unBlackList(userWarn, chat_id)
            elif text.startswith('!blacklist'):
                userWarn = text[12:]
                dropBlacklist.append(userWarn)
            elif text.startswith('!showblacklist'):
                listit = "\n".join(dropBlacklist)
                bot.sendMessage(chat_id, listit)
            elif text.startswith('!unwarn'):
                userWarn = text[9:]
                unWarn(userWarn, chat_id)
            elif text.startswith('!resetwarn'):
                userWarn = text[12:]
                resetWarn(userWarn, chat_id)

        if 'nr' in text or 'next round' in text or 'nextround' in text:
            bot.sendMessage(chat_id, "Round Times: 3,6,9,12 am/pm Eastern Time")
        if text == '!howto':
            message = "\n".join([
                "Instagains LIKE ROUNDS Info",
                "The purpose of LIKE ROUNDS is to game Instagram's algorithm by getting as much engagement as possible within the first hour of posting",
                "There are 8 rounds and each round is optional to participate in\n",
                "Round Times:",
                "3  AM/PM, (Eastern)",
                "6  AM/PM (Eastern)",
                "9  AM/PM (Eastern)",
                "12 AM/PM (Eastern)",
                "\n",
                "STEP 1",
                "-> 30 minutes before the round starts, the host will prompt you to drop your usernames. Type @yourInstagramUsername to enter. The host will remind you of the format",
                "If you are using a different Instagram account to give likes, type '@receiveLikes with @giveLikes'\n",
                "STEP 2",
                "-> The host will compile the usernames into lists. There are 3 types",
                "FollowLiker: This is if you use FollowLiker",
                "MassPlaner: This is if you use MassPlaner",
                "DM Split List: If you don't have a bot to give likes, copy and paste all the DM lists to yourself on Instagram, go to each user's latest post and give it a like\n",
                "STEP 3",
                "-> Give likes to all user's recent post. The is an automated system that checks directly on Instagram whether or not you actually gave likes", 
                "If you didn't give likes and were part of the round, you have 'leeched'",
                "You receive a warn for each round you leech. If you reach 5/5 warnings, you will be blacklisted from participating and will have to contact an admin\n\n",
                "We may seem strict, but it is for everyone's benefit.\n",
                "9am and 3pm Eastern are usually the biggest rounds so it is highly recommended that you upload your pics on Instagram a few minutes before this time!",
                "Let's go viral!"
                ])
            bot.sendMessage(chat_id, message)
        if text.startswith('D @') or text.startswith('d @') or text.startswith('done @') or text.startswith('Done @') or text.startswith('/done') or text.startswith('/Done'):
            count = dCount[authorId]
            count = count + 1
            dCount[authorId] = count
            if count == 1:
                bot.sendMessage(chat_id, "[" + str(count)  + "/15] Don't say D. The bot automatically checks direcly on Instagram: @" + authorUsername)
            elif count == 2:
                bot.sendMessage(chat_id, "[" + str(count)  + "/15] Don't say D: The bot automatically checks direcly on Instagram: @" + authorUsername)
            elif count == 3:
                bot.sendMessage(chat_id, "[" + str(count)  + "/15] Seriously.... Stop saying D: @" + authorUsername)
            elif count == 4:
                bot.sendMessage(chat_id, "[" + str(count)  + "/15] How many times do you have to be reminded not to say D?: @" + authorUsername)
            elif count == 5:
                bot.sendMessage(chat_id, "[" + str(count)  + "/15] If you keep this up, you will get banned @" + authorUsername)
            elif count == 6:
                bot.sendMessage(chat_id, "[" + str(count)  + "/15] STOP SAYING D @" + authorUsername)
            elif count == 7:
                bot.sendMessage(chat_id, "[" + str(count)  + "/15] You really want to get banned don't you? \n Don't say D @" + authorUsername)
            elif count == 8:
                bot.sendMessage(chat_id, "[" + str(count)  + "/15] You really want to get banned don't you?  Stop saying D @" + authorUsername)
            elif count == 9:
                bot.sendMessage(chat_id, "[" + str(count)  + "/15] I'm not kidding when you're going to get banned. Stop saying D @" + authorUsername)
            elif count == 10:
                bot.sendMessage(chat_id, "[" + str(count)  + "/15] 5 more times you do this and you're banned Stop saying D @" + authorUsername)
            elif count == 11:
                bot.sendMessage(chat_id, "[" + str(count)  + "/15] What's wrong with you? D @" + authorUsername)
            elif count == 12:
                bot.sendMessage(chat_id, "[" + str(count)  + "/15] \n1: You've been reminded 12 times\n2: There's tons of reminders to not say D\nSTOP SAYING D: @" + authorUsername)
            elif count == 13:
                bot.sendMessage(chat_id, "[" + str(count)  + "/15] 2 more times you say D, you're getting banned.\nSeriously. Follow instructions \nStop saying D @" + authorUsername)
            elif count == 14:
                bot.sendMessage(chat_id, "[" + str(count)  + "/15] IF YOU SAY D ONE MORE TIME YOU'RE GOING TO GET BANNED @" + authorUsername)
            elif count == 15:
                try:
                    bot.sendMessage(chat_id, "[" + str(count)  + "/15] You've failed to follow simple instructions. @" + authorUsername)
                    dCount[authorId] = 0
                    bot.kickChatMember(chat_id, authorId)
                except:
                    dCount[authorId] = 0
                    msgId = '288201442'
                    bot.sendMessage(msgId, "Kick " + authorId + " " + authorUsername + " from Instagains Likes")
        #DROP USERNAMES
        if text.startswith('@'):
            #bot.sendMessage(chat_id, "test")
            t = datetime.now(eastern)
            hour = t.hour
            minute = t.minute
            hour = int(hour)
            minute = int(minute)
            et = datetime.now(eastern2)
            eHour = et.hour
            eHour = int(eHour)
            eMinute = et.minute 
            eMinute = int(eMinute)
            #bot.sendMessage(chat_id, "Current time (ET) is: " + str(hour) + ":" + str(minute))
            if (hour == 3) or (hour == 6) or (hour == 9) or (hour == 12) or (hour == 15) or (hour == 18) or (hour == 21) or (hour == 0):
                canDrop = False
                if(minute >= 30):
                    canDrop = True 
            else:
                canDrop = False
                hour = hour + 2
                #bot.sendMessage(chat_id, "Current time (ET) is: " + str(hour) + ":" + str(minute))
            # GATE CHECKS
            if ('\n' in text):
                bot.sendMessage(chat_id, "Only one username at a time please")
            elif authorUsername in dropBlacklist:
                bot.sendMessage(chat_id, "You have been blacklisted from dropping accounts \nPlease contact an admin to get unblacklisted")
            elif canDrop == False:
                bot.sendMessage(chat_id, "It isn't time to drop yet. Current time (ET) is: " + str(eHour) + ":" + str(eMinute))
            elif (',') in text:
                bot.sendMessage(chat_id,"Wrong format. Format is:\n@receiveLikes with @giveLikes " + authorUsername)
            else:
                toList = text[1:]
                toCheck = toList.lower()
                continueDrop = True
                if (" " in toCheck) == True:
                    try:
                        a,b,c = toList.split(" ")
                        dropName = a
                        engagedName = c[1:] 
                        toCheck = engagedName.lower() 
                        toList = dropName 
                    except:
                        bot.sendMessage(chat_id,"Wrong format. Format is:\n@receiveLikes with @giveLikes " + authorUsername)
                if toCheck in checkList:
                    #bot.sendMessage(chat_id, "This username is already in the list")
                    t = authorCheck[toCheck]
                    if t != authorUsername:
                        bot.sendMessage(chat_id,  "This username was not dropped by you " + authorUsername)
                        continueDrop = False

                if toList in dropList:
                    bot.sendMessage(chat_id, "This username is already in the list: " + toList)
                    continueDrop = False
                if continueDrop == True:
                    x = len(checkList)
                    if x == 4:
                        dropList.append(toList)
                        checkList.append(toCheck)
                        authorCheck[toCheck] = authorUsername 
                        endList[toCheck] = authorUsername
                    elif x == 10:
                        dropList.append(toList)
                        checkList.append(toCheck)
                        authorCheck[toCheck] = authorUsername 
                        endList[toCheck] = authorUsername

                    elif x == 20:

                        dropList.append(toList)
                        checkList.append(toCheck)
                        authorCheck[toCheck] = authorUsername 
                        endList[toCheck] = authorUsername
                    elif x == 28:
                        dropList.append(toList)
                        checkList.append(toCheck)
                        authorCheck[toCheck] = authorUsername 
                        endList[toCheck] = authorUsername

                    else:
                        dropList.append(toList)
                        checkList.append(toCheck)
                        authorCheck[toCheck] = authorUsername 
                        endList[toCheck] = authorUsername


        elif text.startswith('@') and canDrop == False:
            bot.sendMessage(chat_id, "It is not yet time to drop")


        # REMOVE USERNAME
        if (text.startswith('!remove') or (text.startswith('/remove'))):
            if canDrop == False:
                et = datetime.now(eastern2)
                eHour = et.hour
                eHour = int(eHour)
                eMinute = et.minute 
                eMinute = int(eMinute)
                bot.sendMessage(chat_id, "The round has already started. You can't remove username now. Current time (ET) is: " + str(eHour) + ":" + str(eMinute))
            elif canDrop == True:
                toList = text[9:]
                toCheck = toList.lower()
                if " " in toCheck:
                    try:
                        a,b,c = toList.split(" ")
                        dropName = a 
                        engagedName = c[1:] 
                        toCheck = engagedName.lower()
                        toList = dropName 
                    except:
                        bot.sendMessage(chat_id, "Wrong format. Remove format is:\n!remove @receiveLikes with @giveLikes")
                    
                try:
                    if toList in dropList:
                        dropList.remove(toList)
                        if endList[toCheck]:
                            del endList[toCheck]
                        bot.sendMessage(chat_id, "Removed: " + toList)
                    if toCheck in checkList:
                        checkList.remove(toCheck)
                    try:
                        authorCheck[toCheck] = authorUsername 
                        if authorCheck[toCheck] in endList:
                            try:
                                #endList.remove(authorCheck[toCheck])
                                del endList[toCheck]
                            except:
                                tb = traceback.format_exc()
                                bot.sendMessage('-1001081667369', "232: removeUsername\n" + tb)
                    except:
                        bot.sendMessage(chat_id, "Username not found!")
                except:
                    tb = traceback.format_exc()
                    bot.sendMessage('-1001081667369', "232: removeUsername\n" + tb)
        elif (text.startswith('!remove') and (canDrop == False)):
            bot.sendMessage("The round has already started. You can't remove username now")

#=============================================================================================================

def unBlackList(x,y):
    userWarn = x 
    chat_id = y 
    try:
        dropBlacklist.remove(userWarn)
        bot.sendMessage(chat_id, userWarn + " has been removed from the blacklist")
    except:
        print("Can't unblacklist")

def autoCheck():
    for x in chat_idList:
        chat_id = x
        try:
            p = len(dropList)
            igUrl = url = "https://api.instagram.com/v1/users/self/media/recent/?access_token="+IG_TOKEN
            conn = urllib.request.urlopen(igUrl)
            raw = conn.read().decode('utf-8')
            data = json.loads(raw)
            for photo in data["data"]:
                med_id = photo["id"]
                break
            MEDIA_ID = str(med_id)
            #ADD TO igList
            igUrl = "https://api.instagram.com/v1/media/"+ MEDIA_ID +"/likes?access_token=" + IG_TOKEN
            conn = urllib.request.urlopen(igUrl)
            raw = conn.read().decode('utf-8')
            data = json.loads(raw)
            try:
                for photo in data["data"]:
                    igLikers = photo["username"]
                    if igLikers not in igList:
                        igList.append(igLikers.lower())
            except:
                print ('Can\'t check likers ')
                tb = traceback.format_exc()
                bot.sendMessage('-1001081667369', "262: autoCheck\n" + tb)
                print (tb)

            # REMOVE USERS FROM checkList if username found on IG 
            # USERS LEFT IN checkList ARE MISSING LIKES ON IG
            for xuser in checkList:
                if xuser in igList:
                    try:
                        checkList.remove(xuser)
                    except:
                        tb = traceback.format_exc()
                        print (tb)
                        print('Something broke in autoCheck')
                        bot.sendMessage('-1001081667369', "276: autoCheck\n" + tb)
                    #try:
                    #    endList.remove(authorCheck[xuser])
                    #except:
                    #    print('286: nope that didn\'t work')
                    #    tb = traceback.format_exc()
                    #    print (tb)
                    try:
                        #authorCheck[xuser] = authorUsername 
                        #endList.remove(authorCheck[xuser])
                        del endList[xuser]
                    except:
                        tb = traceback.format_exc()
                        print('Something broke in autoCheck')
                        bot.sendMessage('-1001081667369', "283: autoCheck\n" + tb)
        #bot.sendMessage(chat_id, "ping")
        except:
            print('autoCheck didnt work this time')
            tb = traceback.format_exc()
            bot.sendMessage('-1001081667369', "436: autoCheck\n" + tb)


def autoCompiling():
    for x in chat_idList:
        chat_id = x
        global canDrop
        canDrop = False 
        bot.sendMessage(chat_id, "- Round Closed - \nCompiling Lists")
        time.sleep(2)
        bot.sendMessage(chat_id, "...........")
        time.sleep(1)
        bot.sendMessage(chat_id, "...........")
        time.sleep(1)
        bot.sendMessage(chat_id, "...........")
        time.sleep(1)
        bot.sendMessage(chat_id, "...........")
        time.sleep(1)
        bot.sendMessage(chat_id, "List Incoming")
        time.sleep(2)
        autoList(chat_id)

def autoList(param):
    global ACTIVE
    chat_id = param
    checker = len(dropList)
    checkerIndex = checker/2
    checkerIndex = int(checkerIndex)
    if checker > 0:
        if checker > 0:
            dropList.insert(checkerIndex, 'salt.vault')
        chat_id = param

        # FOLLOWLIKER
        ul = len(usernames)
        while ul > 0:
            usernames.pop()
            ul -= 1
        a = checker
        b = 1 
        count = 0 
        total = a/200 + 1
        if a % 200 == 0:
            total = a/200
        total = int(total)
        opo = str(total)
        for p in dropList:
            k = dropList[count]
            usernames.append("@" + k)
            ul = len(usernames)
            count += 1
            if ul == 201:
                listit = "\n".join(usernames)
                num = str(b)
                bot.sendMessage(chat_id, 'F O L L O W L I K E R [' + num + '/' + opo + ']\n' + listit)
                b += 1
                while ul > 0:
                    usernames.pop()
                    ul -= 1
        listit =  "\n".join(usernames)
        num = str(b)
        if listit:
            bot.sendMessage(chat_id, 'F O L L O W L I K E R[' + num + '/' + opo + ']\n' + listit)

        # MASS PLANNER
        # FOLLOWLIKER
        ul = len(usernames)
        while ul > 0:
            usernames.pop()
            ul -= 1
        a = checker 
        b = 1
        count = 0 
        total = a/200 + 1
        if a % 200 == 0:
            total = a/200
        total = int(total)
        opo = str(total)
        for p in dropList:
            k = dropList[count]
            usernames.append(k)
            ul = len(usernames)
            count += 1
            if ul == 201:
                listit = "\n".join(usernames)
                num = str(b)
                bot.sendMessage(chat_id, 'M A S S P L A N N E R [' + num + '/' + opo + ']\n' + listit)
                b += 1
                while ul > 0:
                    usernames.pop()
                    ul -= 1
        listit =  "\n".join(usernames)
        num = str(b)
        if listit:
            bot.sendMessage(chat_id, 'M A S S P L A N N E R [' + num + '/' + opo + ']\n' + listit)

        # D M
        ul = len(usernames)
        while ul > 0:
            usernames.pop()
            ul -= 1
        a = checker 
        b = 1
        count = 0 
        total = a/15 + 1
        if a % 15 == 0:
            total = a/15
        total = int(total)
        opo = str(total)
        for p in dropList:
            k = dropList[count]
            usernames.append("@" + k)
            ul = len(usernames)
            count += 1
            if ul == 15:
                listit = "\n".join(usernames)
                num = str(b)
                bot.sendMessage(chat_id, 'D M  S P L I T  [' + num + '/' + opo + ']\n' + listit)
                b += 1
                while ul > 0:
                    usernames.pop()
                    ul -= 1
        listit =  "\n".join(usernames)
        num = str(b)
        if listit:
            bot.sendMessage(chat_id, 'D M  S P L I T[' + num + '/' + opo + ']\n' + listit)
        sendMessage = "\n".join([
            "L I K E   A L L   L I S T S",
            "> If you are using FollowLiker, only use the FollowLiker list",
            "> If you are using MassPlanner, only use the MassPlanner list",
            "> If you are on mobile, copy all the split lists into an Instagram DM to yourself. From there, press their username and engage on their latest post\n",
            "LET'S GO VIRAL!",
            "You have 2 hours to engage"
        ])
        bot.sendMessage(chat_id, sendMessage)
        ACTIVE = True
    else:
        bot.sendMessage(chat_id, "Not enough Users in the round")
        ACTIVE = False


def autoList2(param):
    checker = len(dropList)
    checkerIndex = checker % 5
    dropList.insert(checkerIndex, 'salt.vault')
    #FOLLOWLIKER
    chat_id = param
    numNames = len(dropList)
    splitList = []
    splitList.clear()

    #FOLLOWLIKER
    denom = 200
    total = (numNames/200) + 1
    if((numNames % 200) == 0):
        total = numNames/200
    int(total)
    fuu = int(total)
    counter = 0
    listCount = 1
    while (counter < numNames):
        innerCount = 1
        dropListSplit = dropList
        for p in dropListSplit[:200]:
            userToPost = "@" + p
            splitList.append(userToPost)
            counter += 1
            innerCount += 1
        toPrint = "\n".join(splitList) 
        listNum = str(listCount)
        bot.sendMessage(chat_id, 'FOLLOWLIKER LIST ' + "[" + str(listCount) + "/" + str(fuu) + "]\n" + toPrint)
        listCount += 1
        splitList.clear()

    #MASSPLANNER
    splitList.clear()
    denom = 200
    total = (numNames/200) + 1
    if((numNames % 200) == 0):
        total = numNames/200
    int(total)
    fuu = int(total)
    counter = 0
    listCount = 1
    while (counter < numNames):
        innerCount = 1
        dropListSplit = dropList
        for p in dropListSplit[:200]:
            userToPost = p
            splitList.append(userToPost)
            counter += 1
            innerCount += 1
        toPrint = "\n".join(splitList) 
        listNum = str(listCount)
        bot.sendMessage(chat_id, 'MASS PLANNER LIST ' + "[" + str(listCount) + "/" + str(fuu) + "]\n" + toPrint)
        listCount += 1
        splitList.clear()

    #DM LIST
    splitList.clear()
    denom = 15
    total = (numNames/15) + 1
    if((numNames % 15) == 0):
        total = numNames/15
    int(total)
    fuu = int(total)
    counter = 0
    listCount = 1
    while (counter < numNames):
        innerCount = 1
        dropListSplit = dropList
        for p in dropListSplit[:15]:
            userToPost = "@" + p
            splitList.append(userToPost)
            counter += 1
            innerCount += 1
        toPrint = "\n".join(splitList) 
        listNum = str(listCount)
        bot.sendMessage(chat_id, 'DM SPLIT LIST ' + "[" + str(listCount) + "/" + str(fuu) + "]\n" + toPrint)
        listCount += 1
        splitList.clear()

    sendMessage = "\n".join([
        "L I K E   A L L   L I S T S",
        "If you are using FollowLiker, only use the FollowLiker list",
        "If you are using MassPlanner, only use the MassPlanner list",
        "If you are on mobile, copy all the split lists into an Instagram DM to yourself. From there, press their username and engage on their latest post\n",
        "LET'S GO VIRAL!",
        "You have 2 hours to engage"
    ])
    bot.sendMessage(chat_id, sendMessage)

def autoDrop():
    for x in chat_idList:
        chat_id = x
        #CLEAR ALL LISTS
        splitList.clear()
        dropList.clear()
        checkList.clear()
        endList.clear()
        igList.clear()
        global canDrop 
        canDrop = True 
        sendMessage = "\n".join([
            "D R O P  U S E R N A M E S",
            "--------------------------",
            "--------------------------",
            "------ F O R M A T -------",
            "(Same account to engage)",
            "@receiveGiveLikes",
            "----------- O R ----------",
            "(Use different account to engage)",
            "@receivelikes with @givelikes",
            "--------------------------",
            "--------------------------",
            "The lists will drop in 30 minutes"
        ])
        bot.sendMessage(chat_id, sendMessage)

def autoLeech():
    try:
        for x in chat_idList:
            chat_id = x
            p = len(dropList)
            igUrl = url = "https://api.instagram.com/v1/users/self/media/recent/?access_token="+IG_TOKEN
            conn = urllib.request.urlopen(igUrl)
            raw = conn.read().decode('utf-8')
            data = json.loads(raw)
            for photo in data["data"]:
                med_id = photo["id"]
                break
            MEDIA_ID = str(med_id)
            #ADD TO igList
            igUrl = "https://api.instagram.com/v1/media/"+ MEDIA_ID +"/likes?access_token=" + IG_TOKEN
            conn = urllib.request.urlopen(igUrl)
            raw = conn.read().decode('utf-8')
            data = json.loads(raw)
            try:
                for photo in data["data"]:
                    igLikers = photo["username"]
                    if igLikers not in igList:
                        igList.append(igLikers.lower())
            except:
                print ('Can\'t check likers ')
                tb = traceback.format_exc()
                print (tb)
                tb = traceback.format_exc()
                bot.sendMessage('-1001081667369', "560: autoLeech\n" + tb)

            # REMOVE USERS FROM checkList if username found on IG 
            # USERS LEFT IN checkList ARE MISSING LIKES ON IG
            for xuser in checkList:
                if xuser in igList:
                    try:
                        checkList.remove(xuser)
                        #authorCheck[xuser] = authorUsername 
                        #endList.remove(authorCheck[xuser])
                    except:
                        print('Something broke in autoLeech')
                        tb = traceback.format_exc()
                        bot.sendMessage('-1001081667369', "573: autoLeech - checkList.remove(xuser)\n" + tb)

                    try:
                        #authorCheck[xuser] = authorUsername 
                        #endList.remove(authorCheck[xuser])
                        del endList[xuser]
                    except:
                        print('Something broke in autoLeech')
                        tb = traceback.format_exc()
                        bot.sendMessage('-1001081667369', "281: autoLeech - del endList[xuser]\n" + tb)
            #PRINT STILL MISSING
            endPrint.clear()
            global ACTIVE 
            if ACTIVE == True:
                for k,v in endList.items():
                    x = "[" + "%s - %s" % (str(k), str("By: @" + v)) + "]"
                    endPrint.append(x)
                printEnd = "\n".join(checkList) 
                printEnd = "\n".join(endPrint)     
                bot.sendMessage(chat_id, "STILL MISSING FROM \n")
                if len(endPrint) > 0:
                    split(endPrint, 20, chat_id)
                message = "\n".join([
                    "This is halfway into the round",
                    "You still have an hour to complete",
                    "Reminder: If your name still shows up on the final check, you will get a warn",
                    "5/5 warns will result in a blacklist from rounds "
                ])
            if ACTIVE == True:
                message21 = "STILL MISSING FROM"
                bot.sendMessage(chat_id, message)
    except:
        print("oops")


def autoEnd():
    global canDrop 
    canDrop = False
    try:
        for x in chat_idList:
            chat_id = x
            p = len(dropList)
            igUrl = url = "https://api.instagram.com/v1/users/self/media/recent/?access_token="+IG_TOKEN
            conn = urllib.request.urlopen(igUrl)
            raw = conn.read().decode('utf-8')
            data = json.loads(raw)
            for photo in data["data"]:
                med_id = photo["id"]
                break
            MEDIA_ID = str(med_id)

            #ADD TO igList
            igUrl = "https://api.instagram.com/v1/media/"+ MEDIA_ID +"/likes?access_token=" + IG_TOKEN
            conn = urllib.request.urlopen(igUrl)
            raw = conn.read().decode('utf-8')
            data = json.loads(raw)
            try:
                for photo in data["data"]:
                    igLikers = photo["username"]
                    if igLikers not in igList:
                        igList.append(igLikers.lower())
            except:
                print ("autoEnd - Can't read IG Likers")

            # REMOVE USERS FROM checkList if username found on IG 
            # USERS LEFT IN checkList ARE MISSING LIKES ON IG
            for xuser in checkList:
                if xuser in igList:
                    try:
                        checkList.remove(xuser)
                    except:
                        print ("autoEnd - Something went wrong in .remove from check" + xuser)
                        tb = traceback.format_exc()
                        print (tb)
                    try:
                        del endList[xuser]
                    except:
                        print ("autoEnd - Something went wrong in .remove from delDict" + xuser)
                        tb = traceback.format_exc()
                        print (tb)

            # STILL MISSING PRINT 
            endPrint.clear()
            global ACTIVE 
            if ACTIVE == True:
                for k,v in endList.items():               # will become d.items() in py3k
                    x = "[" + "%s - %s" % (str(k), str("By: @" + v)) + "]"
                    endPrint.append(x)
                printEnd = "\n".join(checkList)
                #await client.send_message(client.get_channel(igEngagement), "DEBUG: STILL MISSING FROM:\n" + printEnd)
                printEnd = "\n".join(endPrint)
                this = "STILL MISSING FROM:\n"
                bot.sendMessage(chat_id, this)
                if len(endPrint) > 0:
                    split(endPrint, 20, chat_id)
                message = "\n".join([
                    "This is the end of the round",
                    "If you are not done, you have an extra 20 minutes to complete",
                    "If your name still shows up on the final check, you will receive a warn",
                    "5/5 warns will result in a  blacklist from rounds"
                    ])
            if ACTIVE == True:
                message21 = "STILL MISSING FROM"
                bot.sendMessage(chat_id, message)
    except:
        print("oops")


def autoLate():
    global ACTIVE
    try:
        autoWarnList.clear()
        global canDrop 
        canDrop = False
        for x in chat_idList:
            chat_id = x
            p = len(dropList)
            igUrl = url = "https://api.instagram.com/v1/users/self/media/recent/?access_token="+IG_TOKEN
            conn = urllib.request.urlopen(igUrl)
            raw = conn.read().decode('utf-8')
            data = json.loads(raw)
            for photo in data["data"]:
                med_id = photo["id"]
                break
            MEDIA_ID = str(med_id)

            #ADD TO igList
            igUrl = "https://api.instagram.com/v1/media/"+ MEDIA_ID +"/likes?access_token=" + IG_TOKEN
            conn = urllib.request.urlopen(igUrl)
            raw = conn.read().decode('utf-8')
            data = json.loads(raw)
            try:
                for photo in data["data"]:
                    igLikers = photo["username"]
                    if igLikers not in igList:
                        igList.append(igLikers.lower())
            except:
                print ("autoEnd - Can't read IG Likers")

            # REMOVE USERS FROM checkList if username found on IG 
            # USERS LEFT IN checkList ARE MISSING LIKES ON IG
            for xuser in checkList:
                if xuser in igList:
                    try:
                        checkList.remove(xuser)
                    except:
                        print ("autoEnd - Something went wrong in .remove from check" + xuser)
                    try:
                        del endList[xuser]
                    except:
                        print ("autoEnd - Something went wrong in .remove from delDict" + xuser)



                # FIX THIS
                elif xuser not in igList:
                    try:
                        userWarn = endList[xuser]
                        print("userWarn: " + str(userWarn))
                        print("xuser: " + str(xuser))
                        if userWarn in autoWarnList:
                            print (userWarn + "already in warnlist")
                        else:
                            autoWarnList.append(userWarn)
                            warnNum = warnCount[userWarn]
                            warnNum = warnNum + 1
                            warnCount[userWarn] = warnNum
                            if ACTIVE == True:
                                bot.sendMessage(chat_id, "@" + str(userWarn) + " has been warned. You will be blacklisted if you keep leeching")
                                if warnNum == 18:
                                    bot.sendMessage(chat_id, "@" + str(userWarn) + " has been warned. You are extremely close to becoming blacklisted ")
                                if warnNum >= 20:
                                    dropBlacklist.append(userWarn)
                                    msgId = '288201442'
                                    bot.sendMessage(msgId, str(userwarn) + " has been blacklisted: Kick soon pls ")
                                    bot.sendMessage(chat_id, "@" + str(userWarn) + " has been blacklisted")
                                    warnCount[userWarn] = 0
                    except:
                        print("Auto end broke")
                        tb = traceback.format_exc()
                        print (tb)
            # STILL MISSING PRINT 
            endPrint.clear()
            #global ACTIVE 
            if ACTIVE == True:
                for k,v in endList.items():               # will become d.items() in py3k
                    x = "[" + "%s - %s" % (str(k), str("By: @" + v)) + "]"
                    endPrint.append(x)
                printEnd = "\n".join(checkList)
                #await client.send_message(client.get_channel(igEngagement), "DEBUG: STILL MISSING FROM:\n" + printEnd)
                printEnd = "\n".join(endPrint)
                this = "STILL MISSING FROM:\n"
                bot.sendMessage(chat_id, this)
                if len(endPrint) > 0:
                    split(endPrint, 20, chat_id)
                message = "\n".join([
                    "This 20 minutes passed the end of the round",
                    "If your name still shows up on the final check, you have received a warn",
                    "5/5 warns will result in a  blacklist from rounds",
                ])
            if ACTIVE == True:
                message21 = "STILL MISSING FROM"
                bot.sendMessage(chat_id, message)
    except:
        print("oops")

def unWarn(x,y):
    userWarn = x 
    chat_id = y
    warnNum = warnCount[userWarn]
    warnNum = warnNum -1 
    warnCount[userWarn] = warnNum
    bot.sendMessage(chat_id, str(userWarn) + " has a warn removed. [" + str(warnNum) + "/5]")

def resetWarn(x,y):
    userWarn = x 
    chat_id = y
    warnNum = warnCount[userWarn]
    warnNum = 0
    warnCount[userWarn] = warnNum
    if userWarn in dropBlacklist:
        dropBlacklist.remove(userWarn)
        try:
            del blacklistCount[userWarn]
        except:
            return
    bot.sendMessage(chat_id, str(userWarn) + " has warns reset. [" + str(warnNum) + "/5]")

def autoForty():
    for x in chat_idList:
        chat_id = x
        global canDrop
        canDrop = False 
        bot.sendMessage(chat_id, "Round starts in 30 minutes. Get Ready!")

def autoTen():
    for x in chat_idList:
        chat_id = x
        global canDrop
        canDrop = False 
        bot.sendMessage(chat_id, "Round starts in 10 minutes. Get Ready!")

def autoKeepDropping():
    for x in chat_idList:
        chat_id = x
        global canDrop
        canDrop = True 
        bot.sendMessage(chat_id, "K E E P    D R O P P I N G")
def thirtyAnnounce():
    for x in chat_idList:
        chat_id = x 
        message = "\n".join([
            "P L E A S E   R E A D\n",
            "This is the drop format:\n",
            "----Engaging with same account----",
            "@receiveandgiveLikes",
            "----Engaging with different account----",
            "@receiveLikes with @giveLikes\n",
            "There is no need to D anymore. You may get kicked if you keep on doing this",
            "Times are now 3,6,9,12 AM/PM Eastern Time\n\n",
            "Invite: https://t.me/joinchat/AAAAAD-YetDSblFMPBU42Q"
            #"Comments: https://t.me/joinchat/AAAAAD6cdD0zWp7vlQgQ3A",
            #"Discussion: https://t.me/joinchat/AAAAAD8lNrcQnITNmD49BA\n\n"
        ])
        bot.sendMessage(chat_id, message)
        
def testPing():
    for x in chat_idList:
        chat_id = x 
        message = "Testing....."
        bot.sendMessage(chat_id, message)

def split(arr, size, chatid):
    chat_id = chatid
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr   = arr[size:]
        pice2 = "\n".join(pice)
        bot.sendMessage(chat_id, pice2)
    arr2 = "\n".join(arr)
    bot.sendMessage(chat_id, arr2)

def clearD():
    for x in chat_idList:
        chat_id = x
        for i in dCount:
            dCount[i] = 0
        bot.sendMessage(chat_id, "D warns have been reset")

def comments():
    for x in chat_idList:
        chat_id = x 
        bot.sendMessage(chat_id, "Join Comments: https://t.me/joinchat/AAAAAD6cdD0zWp7vlQgQ3A")
def dropday():
    dropList.append('auralapse')


def dropday2():
    dropList.append('joshquines')



#schedule.every(30).minutes.do(comments)
schedule.every(2).weeks.do(clearD)  

#schedule.every().day.at("12:45").do(dropday)  
#schedule.every().day.at("9:45").do(dropday)  
#schedule.every().day.at("6:45").do(dropday2)     


#autoForty
schedule.every().day.at("0:00").do(autoForty)
schedule.every().day.at("3:00").do(autoForty)
schedule.every().day.at("6:00").do(autoForty)
schedule.every().day.at("9:00").do(autoForty)
schedule.every().day.at("12:00").do(autoForty)
schedule.every().day.at("15:00").do(autoForty)
schedule.every().day.at("18:00").do(autoForty)
schedule.every().day.at("21:00").do(autoForty)
#autoTen 
schedule.every().day.at("0:20").do(autoTen)
schedule.every().day.at("3:20").do(autoTen)
schedule.every().day.at("6:20").do(autoTen)
schedule.every().day.at("9:20").do(autoTen)
schedule.every().day.at("12:20").do(autoTen)
schedule.every().day.at("15:20").do(autoTen)
schedule.every().day.at("18:20").do(autoTen)
schedule.every().day.at("21:20").do(autoTen)
#autoDrop 
schedule.every().day.at("0:30").do(autoDrop)
schedule.every().day.at("3:30").do(autoDrop)
schedule.every().day.at("6:30").do(autoDrop)
schedule.every().day.at("9:30").do(autoDrop)
schedule.every().day.at("12:30").do(autoDrop)
schedule.every().day.at("15:30").do(autoDrop)
schedule.every().day.at("18:30").do(autoDrop)
schedule.every().day.at("21:30").do(autoDrop)
#autoKeepDropping
schedule.every().day.at("0:50").do(autoKeepDropping)
schedule.every().day.at("3:50").do(autoKeepDropping)
schedule.every().day.at("6:50").do(autoKeepDropping)
schedule.every().day.at("9:50").do(autoKeepDropping)
schedule.every().day.at("12:50").do(autoKeepDropping)
schedule.every().day.at("15:50").do(autoKeepDropping)
schedule.every().day.at("18:50").do(autoKeepDropping)
schedule.every().day.at("21:50").do(autoKeepDropping)
#autoCompiling 
schedule.every().day.at("1:00").do(autoCompiling)
schedule.every().day.at("4:00").do(autoCompiling)
schedule.every().day.at("7:00").do(autoCompiling)
schedule.every().day.at("10:00").do(autoCompiling)
schedule.every().day.at("13:00").do(autoCompiling)
schedule.every().day.at("16:00").do(autoCompiling)
schedule.every().day.at("19:00").do(autoCompiling)
schedule.every().day.at("22:00").do(autoCompiling)
#autoLeech 
schedule.every().day.at("2:00").do(autoLeech)
schedule.every().day.at("5:00").do(autoLeech)
schedule.every().day.at("8:00").do(autoLeech)
schedule.every().day.at("11:00").do(autoLeech)
schedule.every().day.at("14:00").do(autoLeech)
schedule.every().day.at("17:00").do(autoLeech)
schedule.every().day.at("20:00").do(autoLeech)
schedule.every().day.at("23:00").do(autoLeech)
#autoEnd 
schedule.every().day.at("2:59").do(autoEnd)
schedule.every().day.at("5:59").do(autoEnd)
schedule.every().day.at("8:59").do(autoEnd)
schedule.every().day.at("11:59").do(autoEnd)
schedule.every().day.at("14:59").do(autoEnd)
schedule.every().day.at("17:59").do(autoEnd)
schedule.every().day.at("20:59").do(autoEnd)
schedule.every().day.at("23:59").do(autoEnd)
#autoLate
schedule.every().day.at("3:19").do(autoLate)
schedule.every().day.at("6:19").do(autoLate)
schedule.every().day.at("9:19").do(autoLate)
schedule.every().day.at("12:19").do(autoLate)
schedule.every().day.at("15:19").do(autoLate)
schedule.every().day.at("18:19").do(autoLate)
schedule.every().day.at("21:19").do(autoLate)
schedule.every().day.at("0:19").do(autoLate)





schedule.every(2).hours.do(thirtyAnnounce)
#schedule.every(2).minutes.do(thirtyAnnounce)

schedule.every(3).minutes.do(autoCheck)
bot.message_loop(handle)


print ('Listening ...')

# Keep the program running.
while 1:
    schedule.run_pending()
    time.sleep(1)
