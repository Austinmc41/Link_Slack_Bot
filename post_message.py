import os
from slack import WebClient
from dotenv import load_dotenv
from builder import construct_payload

load_dotenv()

BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# Initialize a Web API client
slack_web_client = WebClient(token=BOT_TOKEN)


def post_quote_to_channel():



    # Get the onboarding message payload
    message = construct_payload({
        "type": "section",
        "text": {
                "type": "mrkdwn",
                "text": "Wow such text"
        }
    },
        {
        "type": "divider"
    },
        {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Wow such text"
        }
    })
    # Post the onboarding message in Slack
    response = slack_web_client.chat_postMessage(**message)

post_quote_to_channel()