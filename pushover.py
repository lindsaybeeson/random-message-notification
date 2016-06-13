import requests
import random
from time import sleep
import logging

logging.basicConfig(level=logging.INFO)

api_key = "apyg3jsx9z377d3xzob1douxxt9g7m"
user_token = "urt4tc2h31wmsje9r6awgbvnbzirzu"

messages = [
    "did you drink enough water?",
    "remember to slow down when you talk",
    "you're doing fine",
    "cats are awesome",
]

logging.info("Starting up!")

message_count = 0

while message_count <= 4:
    logging.info('Sending message {}'.format(message_count))
    min_sleep = 60 * 60 * 2
    max_sleep = 60 * 60 * 4
    # random time between 2 and 4 hours
    time_to_sleep = random.uniform(min_sleep, max_sleep)

    # Log how much time we're sleeping for
    logging.info(time_to_sleep)

    message_to_send = random.choice(messages)

    data = {
        "message": message_to_send,
        "token": api_key,
        "user": user_token,
        "sound": "pianobar",
    }

    logging.info("About to send the message {}".format(message_to_send))

    r = requests.post('https://api.pushover.net/1/messages.json', data=data)

    # Sleep
    sleep(time_to_sleep)

    message_count += 1
