from __future__ import unicode_literals
import yt_dlp
path = "D:/"

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{path}%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
}

ydl_opts1 = {
    'format': '137+140',
    'outtmpl': f'{path}%(title)s.%(ext)s',
    'prefer_ffmpeg': True,
    'ffmpeg_location': 'C:\\Users\\09765\\anaconda3\\envs\\pythonProject\\Scripts'
}

ydl_opts_mp3 = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://youtu.be/jqXjh9UFnqM'])

with yt_dlp.YoutubeDL(ydl_opts_mp3) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=wWgekWbLE0Y'])