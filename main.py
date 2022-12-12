from pytube import YouTube
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
def get_audio_copy(url):
    filepath = ""
    return filepath

# Get video copy of the YouTube video at a specific resolution
def get_video_copy(url, resolution):
    filepath = ""
    return filepath