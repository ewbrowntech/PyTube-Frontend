import ffmpeg
import os
'''
ffmpeg_functions.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 12 DEC 22

Use FFmpeg to stitch audio and video streams into a single file
'''



# Return the codec in which a video is encoded
def get_codec(filepath):
    info = ffmpeg.probe(filepath)
    videoStream = next(s for s in info['streams'] if s['codec_type'] == 'video')
    return videoStream['codec_name']

# Transcode video to h264 codec for faster stitching
def transcode(inputPath, outputPath):
    if os.path.exists(outputPath): os.remove(outputPath)  # This could be problematic, but it is necessary for now
    ffmpeg.input(inputPath).output(outputPath, codec="h264").run(quiet=True)
    os.remove(inputPath)

# Stitch audio and video streams together
def stitch_video(audioPath, videoPath, filepath):
    inputAudio = ffmpeg.input(audioPath)
    inputVideo = ffmpeg.input(videoPath)
    if os.path.exists(filepath): os.remove(filepath)  # This could be problematic, but it is necessary for now
    print("Stitching video...")
    ffmpeg.output(inputVideo, inputAudio, filepath).run(quiet=True)
    print("Stitching complete.")
    os.remove(audioPath)
    os.remove(videoPath)

