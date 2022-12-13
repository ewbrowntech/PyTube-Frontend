import os
from pytube import YouTube
from src.streams import get_streams
from src.download import download_audio, download_video
from src.ffmpeg_functions import transcode, stitch_video
'''
main.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 12 DEC 22

Get info about a YouTube video or download audio or video copies of it
'''

# Get title of the YouTube video
def get_title(url):
    title = YouTube(url).title
    return title

# Get available resolutions
def get_resolutions(streams):
    videoStreams = streams.filter(only_video=True)
    resolutions = []
    for stream in videoStreams:
        if stream.resolution not in resolutions: resolutions.append(stream.resolution)
    return resolutions

# Get audio copy of the YouTube video
def get_audio_copy(url, downloadsFolderPath):
    streams = get_streams(url)
    isTemp = False
    filepath = download_audio(streams, isTemp, downloadsFolderPath)
    return filepath

# Get a copy of the video with video and no sound
def get_video_only_copy(url, resolution, downloadsFolderPath):
    streams = get_streams(url)
    filepath = os.path.join(downloadsFolderPath, 'YouTube-Video.mp4')
    rawVideo = download_video(streams, resolution, downloadsFolderPath)
    transcode(rawVideo, filepath)
    return filepath

# Get video copy of the YouTube video at a specific resolution
def get_video_copy(url, resolution, downloadsFolderPath):
    streams = get_streams(url)
    audioPath = download_audio(streams, True, downloadsFolderPath)
    videoPath = download_video(streams, resolution, downloadsFolderPath)
    filepath = os.path.join(downloadsFolderPath, "YouTube-Video.mp4")
    stitch_video(audioPath, videoPath, filepath)
    return filepath