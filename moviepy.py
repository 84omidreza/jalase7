from moviepy import editor

video = editor.VideoFileClip('yas.mp4')
video.audio.write_audiofile('yas.mp3')