import praw
from datetime import datetime

client_id = 'flFNpIkhRFRqbxiqYbvkHg'
client_secret = 'fza-CNO-9yRREaRruBUrT5MpwAMEdA'
user_agent = 'redis databases'

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
) 
    
def get_data_from_reddit_url(url):
    post_url=url
  
    try:
        submission = reddit.submission(url=post_url)
        created_date = datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S UTC')
        lista = [submission.title,submission.url,submission.selftext,created_date]
        return lista

    except praw.exceptions.ClientException as e:
        print(f"Error: {e}")

