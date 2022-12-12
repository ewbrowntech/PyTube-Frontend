import os
from src.streams import get_preffered_video_stream
'''
file_info.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 12 DEC 22

Download the video and/or audio streams of a YouTube video
'''

# Download audio
def download_audio(streams, title, downloadsFolderPath):
    audioStreams = streams.filter(only_audio=True)
    preferredStream = audioStreams.order_by("abr").last()  # Get stream with highest audio bitrate
    filetype = preferredStream.mime_type.split("/")[1]     # Get the filetype of that stream
    if title == None:
        filename = "audio" + "." + filetype
    else:
        filename = title + "." + filetype
    filepath = os.path.join(downloadsFolderPath, filename)

    preferredStream.download(downloadsFolderPath, filename=filename)
    return filepath

# Download video
def download_video(streams, resolution, downloadsFolderPath):
    videoStreams = streams.filter(only_video=True)
    preferredStream = get_preffered_video_stream(videoStreams, resolution)
    if type(preferredStream) == str and "Error: " in preferredStream: return preferredStream
    filetype = preferredStream.mime_type.split("/")[1]  # Get the filetype of that stream
    filename = "video" + "." + filetype
    filepath = os.path.join(downloadsFolderPath, filename)

    preferredStream.download(downloadsFolderPath, filename=filename)
    return filepath