# pip install audioplayer

from audioplayer import AudioPlayer


audio = AudioPlayer("audio_x.mp3")
print("start")
audio.play(block=True)
print("end")


# audio.play()
# input()