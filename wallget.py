import re
import os
import praw
import urllib.request


reddit = praw.Reddit("bot1",
                     user_agent="Wallget - Saved Wallpaper Downloader"
                     )

print(f'Retreiving saved wallpapers for: {reddit.user.me()}')

saved = reddit.user.me().saved(limit=40)

for link in saved:
    if link.subreddit == 'wallpapers':
        print(f'{link.title} : {link.url}')
        sanitized_title = re.sub('[\W_]+', '', link.title)
        extension = link.url.split('.')[-1]
        filename = f'{sanitized_title}.{extension}'
        if os.path.exists(filename):
            continue
        urllib.request.urlretrieve(link.url, filename)

print("Downloads completed.")

