import re
import os
import praw
import urllib.request


reddit = praw.Reddit("bot1",
                     user_agent="wallget - Saved /r/wallpapers Downloader"
                     )
valid_ext = ["png", "jpg", "jpeg", "webp"]
saved = reddit.user.me().saved(limit=50)

print(f'Retreiving saved wallpapers for: {reddit.user.me()}')

for link in saved:
    if link.subreddit == 'wallpapers':
        sanitized_title = re.sub('[\W_]+', '', link.title)
        extension = link.url.split('.')[-1].lower()
        if extension not in valid_ext:
            continue
        filename = f'{sanitized_title}.{extension}'
        if os.path.exists(filename):
            continue
        print(f'{link.title} : {link.url}')

        urllib.request.urlretrieve(link.url, filename)

print("Download(s) completed.")

