from gtts import gTTS
import vlc
import os
import time

language = 'en'
path_audio = "audio"
if not os.path.exists(path_audio):
    os.mkdir(path_audio)

class Audio:
    def text2audio(self, text, filename = "audio"):
        output = gTTS(text=text,lang=language, slow=False)
        path = os.path.join(path_audio, filename + ".mp3")
        output.save(path)
        return path
    def get_audio_duration(self, filename):
        # creating a vlc instance 
        vlc_instance = vlc.Instance()

        # creating a media player
        player = vlc_instance.media_player_new()

        # creating a media
        media = vlc_instance.media_new(filename)

        # setting media to the player
        player.set_media(media) 

        # play the video 
        player.play() 
            
        # wait time 
        time.sleep(.1)

        # getting the duration of the video
        duration = int(player.get_length() / 1000)
        return duration
    def play_audio(self, duration, filename):
        # creating a vlc instance 
        vlc_instance = vlc.Instance()

        # creating a media player
        player = vlc_instance.media_player_new()

        # creating a media
        media = vlc_instance.media_new(filename)

        # setting media to the player
        player.set_media(media) 

        player.play()
        # print("[+] waiting audio")
        time.sleep(duration)