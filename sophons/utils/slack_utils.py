from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import re

load_dotenv()

slack_token = os.environ.get("slack_token")
client = WebClient(token=slack_token)

def get_channel_id(channel_name):
    try:
        response = client.conversations_list()
        channels = response['channels']
        for channel in channels:
            if channel['name'] == channel_name:
                return channel['id']
        return None
    except SlackApiError as e:
        print(f"Error fetching channels: {e.response['error']}")
        return None
    
def get_latest_message(channel_id):
    try:
        response = client.conversations_history(channel=channel_id, limit=1)
        messages = response['messages']
        if messages:
            latest_message = messages[0]
            is_yt, is_url = check_url_and_youtube(latest_message['text'])
            if is_yt:
                return latest_message['text'], latest_message['ts'], 'yt'
            elif is_url:
                return latest_message['text'], latest_message['ts'], 'url'
            else:
                return latest_message['text'], latest_message['ts'], 'None'
        else:
            return None, None, None
    except SlackApiError as e:
        print(f"Error fetching messages: {e.response['error']}")
        return None, None

def check_url_and_youtube(text):
    url_regex = re.compile(
        r'^(https?:\/\/)?' 
        r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|'
        r'(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w\-]*)?'
        r'\??(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)$'
    )

    youtube_regex = re.compile(
        r'(https?:\/\/)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)\/(watch\?v=|embed\/|v\/|.+\?v=)?([^&=%\?]{11})'
    )

    is_url = bool(url_regex.match(text))
    is_youtube = bool(youtube_regex.match(text)) if is_url else False

    return is_youtube, is_url

if __name__=="__main__":

    link, ts, type = get_latest_message(get_channel_id('content-dump'))
    print(f"{link}, {ts}, {type}")