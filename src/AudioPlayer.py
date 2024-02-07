import sounddevice as sd
import threading
import numpy as np

class AudioPlayer:
    def __init__(self, sample_rate=44100, callback=None):
        self.sample_rate = sample_rate
        self.playing = False
        self.paused = False
        self.audio_data = np.zeros(1)
        self.thread = None
        self.pointer = 0
        self.callback = callback

    def play_audio(self, audio_data, sample_rate):
        if not self.playing:
            self.sample_rate = sample_rate
            self.audio_data = audio_data
            self.playing = True
            self.paused = False
            self.thread = threading.Thread(target=self._play_thread)
            self.thread.start()

    def stop_audio(self):
        if self.playing:
            self.playing = False
            self.paused = False
            self.pointer = len(self.audio_data) + 1
            self.thread.join()

    def pause_audio(self):
        if self.playing and not self.paused:
            self.paused = True

    def resume_audio(self):
        if self.playing and self.paused:
            self.paused = False

        # If the song was stoped
        elif not self.playing:
            self.stop_audio()
            self.play_audio(self.audio_data, self.sample_rate)

    def change_audio(self, audio_data=None, sample_rate = None):
        if sample_rate is not None:
            self.sample_rate = sample_rate
        if audio_data is not None:
            self.audio_data = audio_data

    def setAudioPlayedPercentage(self, percentage=0):
        self.pointer =  int(percentage / 100 * (len(self.audio_data) - 1))

    def getAudioPlayedPercentage(self):
        return self.pointer / (len(self.audio_data) - 1) * 100
    
    def getAudioCurrentTime(self):
        if self.sample_rate == 0:
            return 0
        else:
            return (self.pointer + 1) / self.sample_rate
    
    def getAudioTotalTime(self):
        if self.sample_rate == 0:
            return 0
        
        return len(self.audio_data) / self.sample_rate

    def _play_thread(self):
        self.pointer = 0
        self.callback(self.getAudioCurrentTime())

        while self.pointer < len(self.audio_data) and self.playing:
            if not self.paused:
                end = self.pointer + 102400
                if end > len(self.audio_data):
                    end = len(self.audio_data)
                block = self.audio_data[self.pointer:end]
                sd.play(block, samplerate=self.sample_rate, blocking=True)
                self.pointer += len(block)
                self.callback(self.getAudioCurrentTime())
                
        self.playing = False
        self.paused = False