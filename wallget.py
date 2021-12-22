#!/bin/env python3
import re
import os
import praw
import urllib.request


class Wallget:
    def __init__(self, prawbot):
        self.valid_ext = ["png", "jpg", "jpeg", "webp"]
        self.prawbot = prawbot
        self.saved = prawbot.user.me().saved(limit=50)

    def download(self):
        print(f'Retreiving saved wallpapers for: {self.prawbot.user.me()}')

        downloads = 0
        for link in self.saved:
            if link.subreddit == 'wallpapers':
                sanitized_title = re.sub('[\W_]+', '', link.title)
                extension = link.url.split('.')[-1].lower()
                filename = f'{sanitized_title}.{extension}'
                if extension not in self.valid_ext:
                    continue
                if os.path.exists(filename):
                    continue
                print(f'{link.title} : {link.url}')
                urllib.request.urlretrieve(link.url, filename)
                downloads += 1

        if downloads:
            print(f"{downloads} download(s) completed.")

if __name__ == '__main__':
    prawbot1 = praw.Reddit("bot1",
                         user_agent="wallget - Saved /r/wallpapers Downloader"
                  )
    downloader = Wallget(prawbot1)
    downloader.download()
