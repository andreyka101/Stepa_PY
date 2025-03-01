# pip install audioplayer

from audioplayer import AudioPlayer


# открывем запускаем аудио
audio = AudioPlayer("audio_x.mp3")

# запускаем аудио
print("start")
audio.play(block=True)
print("end")


# audio.play()
# input()
