import sounddevice as sd
import numpy as np
import threading

class AudioPlayer:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.playing = False
        self.paused = False
        self.audio_data = None
        self.thread = None

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
            self.thread.join()

    def pause_audio(self):
        if self.playing and not self.paused:
            self.paused = True

    def resume_audio(self):
        if self.playing and self.paused:
            self.paused = False

    def _play_thread(self):
        pointer = 0
        while pointer < len(self.audio_data) and self.playing:
            if not self.paused:
                block = self.audio_data[pointer:pointer + 102400]
                sd.play(block, samplerate=self.sample_rate, blocking=True)
                pointer += len(block)