from __future__ import unicode_literals
import yt_dlp
# 下載的影片僅供教學用途 並無用於商業之用途

# path 改成你的下載路徑
path = "F:\\Video for Education\\"
# url 改成 你要下載的一部影片
url = "https://www.youtube.com/watch?v=2C7Kp0yBpvo"

def video_format_wav(url):
    ydl_opts_wav = {
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
    with yt_dlp.YoutubeDL(ydl_opts_wav) as ydl:
        ydl.download([url])

def video_format_mp4(url):
    ydl_opts_mp4 = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'outtmpl': f'{path}%(title)s.%(ext)s',
        'prefer_ffmpeg': True,
        'ffmpeg_location': 'C:\\Users\\09765\\anaconda3\\envs\\pythonProject\\Scripts'  # 這裡要改 你的ffmpeg.exe的位置
    }
    with yt_dlp.YoutubeDL(ydl_opts_mp4) as ydl:
        ydl.download([url])

def video_format_mp3(url):
    ydl_opts_mp3 = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': 'C:\\Users\\09765\\anaconda3\\envs\\pythonProject\\Scripts'  # 這裡要改 你的ffmpeg.exe的位置
    }

    with yt_dlp.YoutubeDL(ydl_opts_mp3) as ydl:
        ydl.download([url])

if __name__=="__main__":
    #video_format_wav(url)
    #video_format_mp3(url)
    video_format_mp4(url)





