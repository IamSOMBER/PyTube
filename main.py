#!/usr/bin/python3

import pytube
from moviepy.editor import VideoFileClip
import os


def download_stream(video_url):
    videos = pytube.YouTube(video_url)

    for stream in videos.streams:
        # mostra la lista dei video disponibili con le caratteristiche rilevanti
        if "video/mp4" in str(stream):
            print(stream)

    # scegli dalla lista in base all' 'itag'
    # itag = input("inserisci l'itag del video: ")
    itag = 22
    video = videos.streams.get_by_itag(int(itag))

    # rinomina video e scarica
    video_name = video.default_filename  # .replace("mp4", "")
    print("Downloading...")

    video.download(filename=str(video_name))
    print(f"Scaricamento {video_name} completato!")

    return video_name


def extract_audio_from_downloaded_video(video_downloaded):
    output_ext = ".mp3"
    filename, ext = os.path.splitext(video_downloaded)
    video_clip = VideoFileClip(str(video_downloaded))
    audio_file = video_clip.audio
    audio_file.write_audiofile(f"{filename}.{output_ext}")

    # Close the video clip
    video_clip.close()


if __name__ == '__main__':
    stream_list = []

    while True:
        url = input("YouTube url: ")
        if url == "":
            break
        stream_list.append(url)

    for stream in stream_list:
        file_video_name = download_stream(stream)
        # print(file_video_name)

        """ extract_audio = input("vuoi estrarre l'audio? (S/n) ")
        if extract_audio.lower =='s' or extract_audio =="":
            extract_audio_from_downloaded_video(file_video_name.replace("..", ".")) """
        extract_audio_from_downloaded_video(file_video_name.replace("..", "."))
