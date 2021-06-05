import pytube

if __name__ == '__main__':
    url = input("YouTube url: ")
    videos = pytube.YouTube(url)

    for stream in videos.streams:
        # mostra la lista dei video disponibili con le caratteristiche rilevanti
        if "video/mp4" in str(stream):
            print(stream)

    # scegli dalla lista in base all' 'itag'
    itag = input("inserisci l'itag del video: ")
    video = videos.streams.get_by_itag(int(itag))

    # rinomina video, elimina estensione ridondante e scarica
    video_name = video.default_filename.replace("mp4", "")
    print("Downloading ", video_name)
    video.download(filename=str(video_name))

    print("Scaricamento completato!")
