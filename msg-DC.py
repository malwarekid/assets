import sys
import argparse
from discord_webhook import DiscordWebhook

def send_message(webhook_url, msg):
    try:
        webhook = DiscordWebhook(url=webhook_url, content=msg)
        response = webhook.execute()
        if response.status_code == 200:
            print("Message sent successfully.")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Send a message to a Discord webhook.")
    parser.add_argument("webhook_url", help="The URL of the Discord webhook.")
    parser.add_argument("message", help="The message to send.")
    
    args = parser.parse_args()
    
    send_message(args.webhook_url, args.message)

if __name__ == "__main__":
    main()
