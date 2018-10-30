import telepot
import time
import urllib3
import traceback
import datetime
import time
from collections import defaultdict
import json
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
import os
# GLOBAL VARIABLES
adminList = ['Telegram Usernames Go Here']
approvedList = []
userList = defaultdict(list)
pendingPosts = []
pendingPosts.append('Enter a URL here. Only used for initiazation')
pendingPosts.append('Enter a URL here. Only used for initiazation')
pendingPosts.append('Enter a URL here. Only used for initiazation')
pendingPosts.append('Enter a URL here. Only used for initiazation')
pendingPosts.append('Enter a URL here. Only used for initiazation')
pendingPosts.append('Enter a URL here. Only used for initiazation')
pendingPosts.append('Enter a URL here. Only used for initiazation')
pendingPosts.append('Enter a URL here. Only used for initiazation')
pendingPosts.append('Enter a URL here. Only used for initiazation')
pendingPosts.append('Enter a URL here. Only used for initiazation')
pendingPosts.append('Enter a URL here. Only used for initiazation')
blacklist = []
telegramIG = defaultdict(str)
doneStatus = defaultdict(bool)
leechStatus = defaultdict(bool)
checkLeech = defaultdict(bool)
userLink = defaultdict(str)
adminCounter = defaultdict(int)
commenterList = defaultdict(list)
chatList = []
networkMember = []
#GLOBALS and CONSTANTS 
canDrop = True
TOKEN = 'INSTAGRAM TOKEN GOES HERE'
GROUP_ID = <GROUP CHAT ID GOES HERE>
adminChat = <YOUR TELEGRAM ID GOES HERE>
TELEGRAM_USERNAME = 'TELEGRAM USERNAME GOES HERE (NO @)'
bot = telepot.Bot(TOKEN)
approvedAccount = defaultdict(str)
# REPOPULATE APPROVEDLIST + BLACKLIST
txtWrite = open("approvedList.txt", "r+")
txtLines = txtWrite.readlines()
for i in txtLines:
    ii = i.strip()
    approvedList.append(ii)
    #print("approvedList: " + str(i))
txtWrite.close()
# REPOPULATE NETWORK MEMBERS
f = open('networkMembers.txt', 'a+')
fLines = f.readlines()
fCount = 0
for x in fLines:
    fCount = fCount + 1
if fCount > 8:
    for x in fLines:
        x = x.strip()
        networkMembers.append(x)
f.close()
# REPOPULATE PENDING POSTS
f = open('postList.txt', 'r+')
fLines = f.readlines()
fCount = 0
for x in fLines:
    x = x.strip()
    pendingPosts.insert(0, x)
    pendingPosts.pop()
f.close()
# ANNOUNCE BOT RESTART
txtWrite = open("chatList.txt", "r+")
txtLines = txtWrite.readlines()
for i in txtLines:
    ii = i.strip()
    chatList.append(ii)
    try:
        pass
        #bot.sendMessage(ii, "BOT UPDATE:\n-> Tweaks and fixes for bot stability\nIf you find any bugs, report to admin \n\n**Please reinitialize your account by typing\n 'initialize me @IGusername\nAlso don\'t forget to pin me")
    except:
        print("No can do: " + str(i))
        tb = traceback.format_exc()
        print (tb)
txtWrite.close()
blkList = open("blackList.txt", "r+")
txtLines = blkList.readlines()
for i in txtLines:
    ii = i.strip()
    blacklist.append(ii)
blkList.close()
def checkUsername(igLink, debug):
    try:
        igUrl = str(igLink) + "?__a=1"
        if debug == True:
            bot.sendMessage(adminChat, "It is: " + igUrl)
        conn = urllib.request.urlopen(igUrl)
        raw = conn.read().decode('utf-8')
        data = json.loads(raw)
        igUsername = data["graphql"]["shortcode_media"]["owner"]["username"]
        if debug == True:
            bot.sendMessage(adminChat, "igUsername: " + str(igUsername.upper()))
        if igUsername.upper() in blacklist:
            return False
        else:
            return True
    except:
        print("Error trying to check username")
        tb = traceback.format_exc()
        print (tb)
def botAnnounce():
    #for x in chatList:
    #    try:
    bot.sendMessage(GROUP_ID, "A new post has been added!\nAdd your post to @ now!")
schedule.every(30).minutes.do(botAnnounce)
# ADMIN PRIVILEGES
def getLatest(IG_TOKEN):
    # GET MEDIA_ID OF POST
    igUrl = url = "https://api.instagram.com/v1/users/self/media/recent/?access_token=" + IG_TOKEN
    conn = urllib.request.urlopen(igUrl)
    raw = conn.read().decode('utf-8')
    data = json.loads(raw)
    for photo in data["data"]:
        med_id = photo["id"]
        break
    MEDIA_ID = str(med_id)  
    igUrl = "https://api.instagram.com/v1/media/" + MEDIA_ID + "?access_token=" + IG_TOKEN
    conn = urllib.request.urlopen(igUrl)
    raw = conn.read().decode('utf-8')
    data = json.loads(raw)
    try:
        x = data["data"]
        igLink = x["link"]
    except:
        print ("autoEnd - Can't read IG Likers")
    if igLink not in pendingPosts:
        pendingPosts.insert(0, igLink)
        #bot.sendMessage(GROUP_ID, "A new post has been added to the queue")
        pendingPosts.pop()
        botAnnounce()
        bot.sendMessage(adminChat, "Added: " + str(igLink), disable_web_page_preview=True)
    
"""
#J.QNS
schedule.every().day.at("20:00").do(getLatest, TOKEN)
schedule.every().day.at("15:20").do(getLatest, TOKEN)
"""
# Check Followers
def followerCount(igCheck, debug, chat_id):
    try:
        bot.sendMessage(chat_id, "test")
        igUrl = "https://instagram.com/" + str(igCheck) + "/?__a=1"
        conn = urllib.request.urlopen(igUrl)
        raw = conn.read().decode('utf-8')
        data = json.loads(raw)
        followerNum = data['graphql']['user']['edge_followed_by']['count']
        if debug == True:
            bot.sendMessage(chat_id, followerNum)
        if followerNum < 500:
            return False
        else:
            if followerNum > 20000:
                bot.sendMessage(chat_id, "You are also qualified to use @!")
            return True
    except:
        print("Error trying to check followers")
        tb = traceback.format_exc()
        print (tb)
def commentCheck(igUsername, igLink, debug, chat_id):
    startTime = time.time()
    try:
        # Open igLink to check
        igUrl = str(igLink) + "?__a=1"
        conn = urllib.request.urlopen(igUrl)
        raw = conn.read().decode('utf-8')
        data = json.loads(raw)
        try:
            # Get list of commenters
            photo = data["graphql"]["shortcode_media"]["edge_media_to_comment"]["edges"]
            disabledStatus = data["graphql"]["shortcode_media"]["comments_disabled"]
            
            # Open txtFile to append igCommenter 
            if igLink.startswith('https://www.instagram.com/p/'):
                igLink = igLink.replace('https://www.instagram.com/p/', '')
            elif igLink.startswith('https://instagram.com/p/'):
                igLink = igLink.replace('https://instagram.com/p/', '')
            fName = str(igLink)
            # Redundancy to 100% remove directory issues
            fName = str(igLink).replace('/','_')
            fName = fName.replace('.',"_")
            fName = fName.replace(':',"_")
            fName = "" + fName + ".txt"
            f = open(fName, "a+") 
            f.seek(0)
            alreadyInside = f.read()
            # Append igCommenter to txtFile
            for usernames in photo:
                igCommenter = usernames["node"]
                igCommenter = igCommenter["owner"]["username"]
                if igCommenter.upper() not in alreadyInside:
                    f.write(igCommenter.upper() + '\n')
            # checkLeech initially is true
            checkLeech[chat_id] = True
            # Check starts here
            if igUsername != 'append':
                # START CHECKING FOR COMMENTERS
                # Read from txtFile
                f.seek(0)
                finalCommenters = f.read()
                # If cannot open IG post, ignore leechCheck
                if igUsername.upper() in finalCommenters:
                    checkLeech[chat_id] = False 
                    bot.sendMessage(chat_id, "Comment found from igUsername: " + str(igUsername))
                else:
                    if disabledStatus == "true":
                        bot.sendMessage(chat_id, "Comments turned off for this post!")
                        checkLeech[chat_id] = False 
                    else:
                        bot.sendMessage(chat_id, "Comment missing!")
                        checkLeech[chat_id] = True
                f.close()
                return checkLeech[chat_id]
            else:
                f.close()
                return checkLeech[chat_id]
        except:
            bot.sendMessage(adminChat, "Cannot get List of commenters")
            tb = traceback.format_exc()
            print (tb)
            bot.sendMessage(adminChat, tb)
    except:
        bot.sendMessage(adminChat, "Cannot get List of commenters outer")
        tb = traceback.format_exc()
        print (tb)
    bot.sendMessage(adminChat,"commentCheck() execution: " + str(time.time() - startTime))
# 
def appendCommenters():
    startTime = time.time()
    try:
        # Go through all the current userLists
        for x in userList:
            chat_id = x 
            # Get igLink
            for y in userList[chat_id]:
                igLink = y 
                status = 'append'
                commentCheck(status, igLink, False, chat_id)
        # Go through the pendingPosts
        for y in pendingPosts:
            igLink = y 
            status = 'append'
            commentCheck(status, igLink, False, chat_id)
    except:
        # There are no userLists
        pass
schedule.every(10).minutes.do(appendCommenters)
#@asyncio.coroutine
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    identifier = telepot.message_identifier(msg)
    # GET USERNAMES
    try:            
        username = str(msg["from"]["username"])
        usernameStatus = True
    except:
        usernameStatus = False
    
    if usernameStatus == True:
        # BOT ACTIONS FOR DM 
        if chat_id > 0:
            if content_type == 'text':
                try:            
                    username = str(msg["from"]["username"])
                    networkMember.append(username.upper())
                    txtWrite = open("networkMembers.txt", "a+")
                    txtWrite.write(username.upper() + '\n')
                    txtWrite.close()
                except:
                    pass
                text = msg["text"]
                print(content_type, chat_type, chat_id, username, text, str(usernameStatus))
                # START
                if text == "/start":
                    bot.sendMessage(chat_id, "1) Type \'initialize me @yourIGusername\'\n")
                # BOT INSTRUCTIONS
                elif text == "/instructions":
                    message = "\n".join([
                        "INSTRUCTIONS",
                        "Step 1 --->\n  Type initialize me @IGusername",
                        "Step 2 --->\n  Copy & Paste your IG post URL",
                        "Step 3 --->\n  You will receive a list of posts to like on (Usually 10 - 12)",
                        "Step 4 --->\n  Once you are done commenting, type \'done\'",
                        "Step 5 --->\n  The bot will check for your comments",
                        "Step 6 --->\n  If you are missing comments, the bot will let you know which one you\'re missing",
                        "Step 7 --->\n  If you have successfully completed, the bot will then add your post to the queue to receive comments",
                        "\n\nRULE:\n Your account must be high quality. Failure to meet this requirement will result in your IG account being blacklisted in the network",
                        #"\nINVITE: Type /invite"
                        ])
                    bot.sendMessage(chat_id, message)
                # GIVE INVITE LINK
                elif text == "/invite":
                    bot.sendMessage(chat_id, "Invite: https://t.me/joinchat/ES2a4lBmVt-wroWO_BKSsA")
                # INITIALIZE ACCOUNT
                if text.startswith("initialize me") or text.startswith("Initialize me"):
                    userIG = text.upper()[15:]
                    username = str(msg["from"]["username"])
                    if userIG in blacklist:
                        bot.sendMessage(chat_id, "Your IG account has been blacklisted due to your account being low quality")
                    else:
                        bot.sendMessage(chat_id, "Your IG username to give comments is: @" + userIG)
                        bot.sendMessage(chat_id, "Also, if your account is in a low quality niche (luxury, memes, nsfw, weed, quotes, etc....), your IG account will eventually get blacklisted")
                        debug = False
                        #counter = followerCount(userIG, debug, chat_id)
                        #bot.sendMessage(chat_id, str(counter) + "OH NO")
                        #if counter == True:
                        if (1 == 1):
                            instructions = "\n".join([
                                "INSTRUCTIONS",
                                "Step 1 --->\nCopy & Paste your IG post URL",
                                "Step 2 --->\nYou will receive a list of posts to like on (Usually 10 - 12)",
                                "Step 3 --->\nOnce you are done commenting, type \'done\'",
                                "Step 4 --->\nThe bot will check for your comments",
                                "Step 5 --->\nIf you are missing comments, the bot will let you know which one you\'re missing",
                                "Step 6 --->\nIf you have successfully completed, the bot will then add your post to the queue to receive comments",
                                ])
                            bot.sendMessage(chat_id, "Your IG account has been approved. You may now start participating.\n**Type /instructions to get started")
                            # Append user's IG to approvedList
                            txtWrite = open("approvedList.txt", "a+")
                            txtWrite.write(userIG + '\n')
                            txtWrite.close()
                            approvedList.append(userIG)
                            telegramIG[chat_id] = userIG
                            #DEBUG
                            bot.sendMessage(chat_id, "USERNAME IS: " + telegramIG[chat_id])
                            if chat_id not in chatList:
                                
                                chatList.append(str(chat_id) + '\n')
                                txtWrite = open("chatList.txt", "a+")
                                txtWrite.write(str(chat_id))
                                txtWrite.close()
                        # IG Username does not meet the follower requirements
                        if counter == False:
                            bot.sendMessage(chat_id, "Your IG account does not meet the requirements for this bot.")
                # cHECK WHAT IG USERNAME
                elif text.upper() == "MYUSERNAME":
                    telegramUser = telegramIG[chat_id]
                    bot.sendMessage(chat_id, "Your IG username is : " + str(telegramUser))
                # USER ENTERS ROUND
                elif (text.startswith("https://instagram.com/p/") and text.endswith("/")) or (text.startswith("https://www.instagram.com/p/") and text.endswith("/")) :
                    telegramUser = telegramIG[chat_id]
                    telegramUserz = telegramUser + '\n'
                    # Check if in approvedList
                    if (1 == 1):
                        try:
                            del userList[chat_id]
                        except:
                            pass
                        # Create user's own checkList      
                        userLink[chat_id] = text
                        if userLink[chat_id] in pendingPosts:
                            bot.sendMessage(chat_id, "This post is already inside the list!")
                        else:
                            blacklistCheck = checkUsername(userLink[chat_id], False)
                            if blacklistCheck == False:
                                bot.sendMessage(chat_id, "This IG account has been blacklisted from the network due to low quality")
                            else:
                                userList[chat_id] = pendingPosts
                                
                                # Create File
                                fName = str(text).replace('/','_')
                                fName = fName.replace('.',"_")
                                fName = fName.replace(':',"_")
                                fName = "" + fName + ".txt"
                                f = open(fName, "a+") 
                                f.close()
                                # Give user list of posts to comment on
                                linkLists = "\n".join(userList[chat_id])
                                bot.sendMessage(chat_id, "Give comments to ALL of the following posts:\n " + linkLists, disable_web_page_preview=True)
                                bot.sendMessage(chat_id, "Now looking for comments from: @" + telegramUser + "\n\nIf a post has come up again and you have already commented on it, you don\'t have to comment on it again")
                                bot.sendMessage(chat_id, "Type \"done\" when you have completed")
                                doneStatus[chat_id] = False
                    else:
                        if telegramUser in blacklist:
                            bot.sendMessage(chat_id, "Your account does not meet the quality requirements and has been unapproved and blacklisted")
                        else:
                            bot.sendMessage(chat_id, "Please type \"Initialize me @yourIGusername\" to get started\n")
                # USER IS DONE ROUND
                elif text.upper() == "DONE":
                    telegramUser = telegramIG[chat_id]
                    if telegramUser in approvedList:
                        debug = False
                        # Get links in userList to Check
                        for x in userList[chat_id]:
                            leechStatus[chat_id] = commentCheck(telegramUser, x, debug, chat_id)
                            # Let user know what they're missing comments on
                            if leechStatus[chat_id] == True:
                                bot.sendMessage(chat_id, 'You are missing a comment on: ' + x + '\n\nType \"done\" again once you have finished commenting on all posts', disable_web_page_preview=True)
                                
                                # Let admin know who tried to leech
                                try:
                                    username = str(msg["from"]["username"])
                                    bot.sendMessage(adminChat, str(username) + " has attempted to leech with " + str(telegramUser))
                                except:
                                    bot.sendMessage(adminChat, str(telegramUser) + " (IG) has attempted to leech" + "on: " + str(x))
                                doneStatus[chat_id] = False
                                break
                            else:                              
                                doneStatus[chat_id] = True
                        
                        # Finalize round for user
                        if doneStatus[chat_id] == True:
                            try:
                                del userList[chat_id]
                            except:
                                print("Unable to delete userList")
                            # Delete last post in list FIFO    
                            pendingPosts.pop()
                            # Insert newLink to front of list
                            pendingPosts.insert(0, userLink[chat_id])
                            # Replace txtList of posts with new one
                            f = open('postList.txt', 'w')
                            for x in pendingPosts:
                                x = str(x) + '\n'
                                f.write(x)
                            f.close()   
                            # reset doneStatus to false
                            doneStatus[chat_id] = False
                            bot.sendMessage(chat_id, "You have completed the round. Your post has now been added to the queue :\n" + str(userLink[chat_id]), disable_web_page_preview=True)
                            #bot.sendMessage(, "New post added!\n@")
                            # Let admin know who tried to leech
                            try:
                                username = str(msg["from"]["username"])
                                bot.sendMessage(adminChat, str(username) + " has completed with " + str(telegramUser))
                            except:
                                pass  
                            botAnnounce()
                            
                            # Make sure to speed up remove posts whenever admins add their own post
                            for x in adminList:
                                try:
                                    if adminCounter[x]:
                                        adminCounter[x] = adminCounter[x] + 1
                                        if adminCounter[x] > 10:
                                            pendingPosts.pop()
                                except:
                                    pass
                    # DONT ALLOW UNAPPROVED TO PARTICIPATE
                    else:
                        if telegramUser in blacklist:
                            bot.sendMessage(chat_id, "Your account does not meet the quality requirements and has been unapproved and blacklisted")
                        else:
                            bot.sendMessage(chat_id, "Your IG account has not yet been approved. Please type \"Initialize me @yourIGusername\" to get started")
                # ADMIN COMMANDS
                elif text.startswith("!remove"):
                    if username in adminList:
                        try:
                            igToRemove = text.upper()[9:]
                            blacklist.append(igToRemove)
                            approvedList.remove(igToRemove)
                            bot.sendMessage(GROUP_ID, "@" + igToRemove + " has been blacklisted. \nIG account quality too low.")
                        except:
                            bot.sendMessage(chat_id, "Username is not currently approved")
                        try:
                            chtRemove = open("chatList.txt", "r+")
                            chtLines = chtRemove.readlines()
                            chtRemove.seek(0)
                            for x in chatList:
                                xx = x.strip()
                                if telegramIG[xx] == igToRemove:
                                    for y in chtLines:
                                        yy = y.strip()
                                        if yy !=  xx:
                                            chtRemove.truncate()
                                            chtRemove.close()
                                    chatList.remove(xx)
                        except:
                            pass
                        
                        # Remove from approvedListTxt
                        txtRemove = open("approvedList.txt", "r+")
                        txtLines = txtRemove.readlines()
                        txtRemove.seek(0)
                        blksty = open("blackList.txt", "a+")
                        blksty.write(igToRemove + '\n')
                        blksty.close()
                        for i in txtLines:
                            ii = i.strip()
                            if ii != igToRemove:
                                txtRemove.write(i)
                        txtRemove.truncate()
                        txtRemove.close()
                        bot.sendMessage(chat_id, "@" + igToRemove + " has been unapproved")
                    else:
                        bot.sendMessage(chat_id, "You\'re not an admin")
                elif text.startswith("!postadd"):
                    if username in adminList:
                        try:
                            igLink = text.split()[1]
                            if (igLink.startswith("https://instagram.com/p/") and igLink.endswith("/")) or (igLink.startswith("https://www.instagram.com/p/") and igLink.endswith("/")):
                                pendingPosts.insert(0, igLink)
                                bot.sendMessage(chat_id, "Your post has been added to the queue")
                                botAnnounce()
                                adminCounter[username] = 0         
                            else:
                                bot.sendMessage(chat_id, "Unable to add post. Please add again\nFormat:\n->!postadd <IGpostLink>")
                        except:
                            bot.sendMessage(chat_id, "Unable to add post. Please add again")
                            tb = traceback.format_exc()
                            print (tb)
                    else:
                        bot.sendMessage(chat_id, "You\'re not an admin")
                elif text.startswith("!addadmin"):
                    if username == TELEGRAM_USERNAME:
                        adminToAdd = text[10:]
                        adminList.append(adminToAdd)
                        bot.sendMessage(chat_id, adminToAdd + " is now an admin")
                    else:
                        bot.sendMessage(chat_id, "Unable to add admin")
                elif text.startswith("!debug"):
                    if username == TELEGRAM_USERNAME:
                        try:
                            if text[7:].startswith("followercount"):
                                bot.sendMessage(chat_id, "DEBUG: followerCount")
                                userCheck = text[21:]
                                debug = True
                                counter = followerCount(userCheck, debug, chat_id)
                                x = str(counter)
                                bot.sendMessage(chat_id, "DEBUG: followerCount returned: " + x)
                            elif text[7:].startswith("commentcheck"):
                                bot.sendMessage(chat_id, "DEBUG: commentCheck")
                                userCheck = text.split()[2]
                                linkCheck = text.split()[3]
                                debug = True
                                cmtChk = commentCheck(userCheck, linkCheck, debug, chat_id)
                                bot.sendMessage(chat_id, "DEBUG: commentCheck returned: " + str(cmtChk))
                            elif text[7:] == "approvelist":
                                linkLists = "\n".join(approvedList)
                                bot.sendMessage(chat_id, linkLists)
                            elif text[7:] == "pendinglist":
                                linkLists = "\n".join(pendingPosts)
                                bot.sendMessage(chat_id, linkLists)
                            elif text[7:] == "whatuser":
                                telegramUser = telegramIG[chat_id]
                                bot.sendMessage(chat_id, "Your IG username is : " + str(telegramUser))
                            elif text[7:] == "commands":
                                bot.sendMessage(chat_id, "followercount\ncommentcheck\napprovelist\npendinglist\nwhatuser\ncommands")
                            elif text[7:].startswith("usercheck"):
                                toCheck = text.split()[2]
                                checkUsername(toCheck, True)
                        except:
                            tb = traceback.format_exc()
                            print (tb)
                            bot.sendMessage(chat_id, "Error \n\n" + tb)
            else:
                try:
                    bot.deleteMessage(identifier)
                except:
                    pass
    else:
        if chat_id > 0:
            bot.sendMessage(chat_id, "You must make a Telegram username to participate.\n-> Go to settings\n-> Press Edit\n-> Scroll down to usernames and add a username")
            try:
                bot.deleteMessage(identifier)
            except:
                pass
    print(content_type, chat_type, chat_id)
print ('Listening ...')
bot.message_loop(handle)
# Keep the program running.
while 1:
    schedule.run_pending()
    time.sleep(1)