import os
from slack import WebClient
from dotenv import load_dotenv
from scripts.builder import construct_payload
from scripts.sga_scrape import scrape_bad_urls

bad_urls = ''



def post_quote_to_channel():

    slack_string = ''

    if bad_urls:
        for url in bad_urls:
            slack_string += f"{url} : {bad_urls[url]} + \n"

    if slack_string  == '':
        slack_string = 'Currently no broken links'


    load_dotenv()

    BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

    # Initialize a Web API client
    slack_web_client = WebClient(token=BOT_TOKEN)



    # Get the onboarding message payload
    message = construct_payload({
        "type": "section",
        "text": {
                "type": "mrkdwn",
                "text": "*Broken SGA Links:*"
        }
    },
        {
        "type": "divider"
    },
        {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"{slack_string}"
        }
    })
    # Post the onboarding message in Slack
    response = slack_web_client.chat_postMessage(**message)
