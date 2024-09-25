#!/usr/bin/python3

import os

import pytube
from moviepy.editor import VideoFileClip

VIDEO_FORMAT = "acodec"
DEFAULT_ITAG = 137
AUDIO_OUTPUT_EXT = ".mp3"


def show_available_video_streams(streams):
    for this_stream in streams:
        # mostra la lista dei flussi video disponibili
        if VIDEO_FORMAT in str(this_stream):
            print(this_stream)


def get_stream_name_from_itag(video_url):
    videos = pytube.YouTube(video_url)

    show_available_video_streams(videos.streams)

    # scegli dalla lista in base all' 'itag'
    itag = input("inserisci l'itag del video: ")
    video = videos.streams.get_by_itag(int(itag))

    # rinomina video e scarica
    video_name = video.default_filename  # .replace("mp4", "")
    print("Downloading...")

    video.download(filename=str(video_name))
    print(f"Scaricamento {video_name} completato!")

    return video_name


def extract_audio_from_downloaded_video(video_downloaded):
    filename, ext = os.path.splitext(video_downloaded)
    video_clip = VideoFileClip(str(video_downloaded))
    audio_file = video_clip.audio
    audio_file.write_audiofile(f"{filename}.{AUDIO_OUTPUT_EXT}")

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
        file_video_name = get_stream_name_from_itag(stream)
        print(file_video_name)

        extract_audio = input("vuoi estrarre l'audio? (S/n) ")
        if extract_audio.lower == 's' or extract_audio == "":
            extract_audio_from_downloaded_video(file_video_name.replace("..", "."))
