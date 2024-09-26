#!/usr/bin/python3

import yt_dlp
from yt_dlp import DownloadError

if __name__ == '__main__':
    stream_list = []

    while True:
        url = input("YouTube url: ")
        if url == "":
            break
        stream_list.append(url)

    try:

        with yt_dlp.YoutubeDL() as ydl:
            ydl.download(stream_list)

    except DownloadError as exception:
        print(f"{stream_list} is not a valid URLs list")