import tweepy
import config
import logging
import telebot
import time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


try:
    api.verify_credentials()
    logger.info("Authenticated!")
except:
    raise "Auhentication failed!"


# Authenticate to Telegram
bot = telebot.TeleBot(config.BOT_API)


try:
    bot.send_message(config.TWEET_CH, "Listening...", parse_mode='Html')
except Exception as e:
    logger.error(e)


class TweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, status):
        """
        function will be executed when a new tweet posted.
        """
        if status.in_reply_to_status_id is not None or status.user.id == self.me.id:
            return
        if not status.retweeted and 'RT @' not in status.text and not status.text.startswith("@"):
            logger.info(f"Processing tweet id {status.id}")
            text = f'***{status.user.name} Just Tweeted:\n\n' \
                   f'«<a href="https://twitter.com/{status.user.screen_name}/status/{status.id}">{status.user.name}</a>»'
            bot.send_message(config.TWEET_CH, text, parse_mode='Html')
            time.sleep(1)

    def on_error(self, status_code):
        logger.error(status_code)


def main():
    logger.info("Started Listening...")
    tweets_listener = TweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(follow=config.follows, is_async=True)


if __name__ == '__main__':
    main()
