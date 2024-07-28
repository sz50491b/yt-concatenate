import urllib3
import json
import os
from yt_concate.settings import API_KEY

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def get_all_video_in_channel(channel_id):
    api_key = os.getenv('API_KEY')
    
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
    
    first_url = base_search_url + f'key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'
    
    video_links = []
    url = first_url
    while True:
        inp = urllib3.request(url=url, method='GET')
        resp = json.loads(inp.data.decode('utf-8'))
        
        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])
        
        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except KeyError:
            break
    return video_links


if __name__ == '__main__':
    # video_list = get_all_video_in_channel(CHANNEL_ID)
    # print(video_list)
    print(API_KEY)