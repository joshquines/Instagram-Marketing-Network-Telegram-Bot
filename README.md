## None of these work anymore

These bots were created to manage an Instagram marketing group on Telegram and Slack.

**Disclaimer:**
Yes there's some API keys and Tokens still left over. 
Those are expired and he accounts for those are dead so it's fine. 

### Version History

**Version 3**
- Introduced a 'comment chain' system. Deprecated enforcement of Instagram Likes
- Use of Instagram's API endpoints to read each user's post's comments

**Version 2**
- Switched to telepot library: https://github.com/nickoala/telepot
- Introduced an 'auto leech' detecter. Checking of participation is now automated
- Use of Instagram's API endpoints to view each user's post's list of likers
- Fully automated 'rounds'


**Version 1B**
- Attempt to implement a Slack group to communicate with the Telegram group

**Version 1**
- Hosted on Google App Engine to automate 'rounds' with Cron
- Introduced an auto list generator
	- Each username who participates in a 'round' automatically gets added to a list
