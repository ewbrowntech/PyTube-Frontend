from pytube import YouTube
'''
streams.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 12 DEC 22

Methods for getting the constituent streams of a YouTube video and sorting through them
'''

# Get audio and video streams of YouTube video
def get_streams(url):
    streams = YouTube(url).streams
    return streams

# Find any video streams at a given resolution and return the one with the most compatible codec
def get_preffered_video_stream(videoStreams, resolution):
    acceptableStreams = []
    for stream in videoStreams:
        if stream.resolution == resolution: acceptableStreams.append(stream)
    if len(acceptableStreams) == 0: return "Error: No streams were found at the requested resolution."

    # Attempt to find stream encoded in AV1 for increased compatibility
    preferredStream = [stream for stream in acceptableStreams if 'av01' in stream.codecs[0]]
    # If there aren't any, try to find one encoded in AVC
    if preferredStream == []:
        preferredStream = [stream for stream in acceptableStreams if 'avc' in stream.codecs[0]]
    # If there aren't any of those, its probably encoded in VP9
    if preferredStream == []:
        preferredStream = [stream for stream in acceptableStreams if 'vp9' in stream.codecs[0]]
    # If there still isnt a preffered stream, something is VERY wrong
    if preferredStream == []:
        return "Error: I was unable to find any streams at that resolution encoded in AVC, AV1, or VP9"

    return preferredStream[0]