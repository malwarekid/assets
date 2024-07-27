import sys
from discord_webhook import DiscordWebhook

WEBHOOK_URL = 'YOUR_WEBHOOK_HERE'

def send_message(msg):
    webhook = DiscordWebhook(url=WEBHOOK_URL, content=msg)
    webhook.execute()

def main():
    msg = input("Send a message: ")
    send_message(msg)
if __name__ == "__main__":
    main()
