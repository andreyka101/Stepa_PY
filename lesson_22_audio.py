# pip install audioplayer

from audioplayer import AudioPlayer


# открывем аудио
audio = AudioPlayer("audio_x.mp3")



# запускаем аудио c блокировкой сроки 
print("start")
audio.play(block=True)
print("end")


# запускаем аудио без блокировки сроки 
# audio.play()
# input()
