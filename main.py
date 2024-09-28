#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
from tkinter.constants import DISABLED

import yt_dlp
from yt_dlp.utils import DownloadError


# Funzione per abilitare il pulsante quando il link è inserito
def check_link(*args):
    link = link_var.get()

    if link:
        button_add.config(state=tk.NORMAL)
    else:
        button_add.config(state=tk.DISABLED)


def add_to_list():
    url = link_var.get()
    button_start.config(state=tk.NORMAL)

    # aggiungi l'url nell'elenco del widget
    textbox_url.insert(tk.END, f"{url}\n")

    # rimuovere tutto il testo presente nell'Entry box
    entry_url.delete(0, tk.END)

    stream_list.append(url)
    print(f"aggiunto: {url}")


def start_download():
    try:

        with yt_dlp.YoutubeDL() as ydl:
            ydl.download(stream_list)
            messagebox.showinfo("Download", "scaricamento completato con successo")

            # Pulisce la lista degli URL per i prossimi download
            stream_list.clear()

            # Cancella il contenuto della textbox per gli URL
            textbox_url.delete("1.0", tk.END)

    except DownloadError:
        messagebox.showerror("Errore", "scaricamento non riuscito")


if __name__ == '__main__':
    stream_list = []

    window = tk.Tk()
    window.title("YouTube Downloader")

    youtube_url_label = tk.Label(window, text="YouTube url")

    # Variabile per il link
    link_var = tk.StringVar()
    link_var.trace_add("write", check_link)

    entry_url = tk.Entry(window, textvariable=link_var, width=50)

    # Crea un pulsante per aggiungere l'URL alla lista
    button_add = tk.Button(window, text="aggiungi", state=DISABLED, command=add_to_list)

    url_list_label = tk.Label(window, text="Elenco URLs")

    # Crea una Textbox per la lista degli URL dei video
    textbox_url = tk.Text(window)

    # Variabile per il checkbutton audio (1 se selezionato, 0 se deselezionato)
    audio_check = tk.IntVar()

    # Creazione del checkbutton
    check_button = tk.Checkbutton(window, text="Estrai audio", variable=audio_check)

    # Crea un pulsante per avviare il download
    button_start = tk.Button(window, text="Start", state=DISABLED, command=start_download)

    youtube_url_label.pack(pady=5)
    entry_url.pack(pady=5)
    button_add.pack(pady=10)
    url_list_label.pack(pady=10)
    textbox_url.pack(fill=tk.BOTH, expand=True, pady=10)
    check_button.pack(pady=20)
    button_start.pack(pady=10)

    # Avvia l'applicazione Tkinter
    window.mainloop()
