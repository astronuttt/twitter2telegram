# Simple Twitter to Telegram script based on [tweepy](https://github.com/tweepy/tweepy)

## Installation  
Make sure *python3* and *git* installed on your system


`git clone https://github.com/sinaebrahimi1/twitter2telegram.git`


and just install the requirements: `pip3 install -r requirements.txt`   


#### `config.py`

*Twitter configs:*


Put the page ids that you want to be monitored in `follows` as a list like `follows = ["123456", "54321"]`.   
_(You can extract user_ids from http://gettwitterid.com.)_


Get Twitter API Authentication Credentials from https://developer.twitter.com/ and place them in `Twitter Configs`  section:   


    1. Consumer key   
    2. Consumer secret    
    3. Access token   
    4. Access secret      


*Telegram configs:*

1. You have to create a channel ant put its id in `TWEET_CH` like the example. (to get channel_id, forward a message from channel to [@userinfobot](https://t.me/userinfobot))

2. Create a new bot with [@BotFather](https://t.me/BotFather) and place it's token in `BOT_API`.

3. Add the bot to the channel and make it channel admin.


## Running the script

`python3 main.py`

if you want to prevent crashes or things like that, just run this command:   
`while true; do python3 main.py; done`



#### contact me:
* email: ebrahimisina78@gmail.com
* telegram: [@Thunderstrack](https://t.me/Thunderstrack)