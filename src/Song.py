import numpy as np
from librosa import resample


class Song:
    """
    Song: contains all the tracks necessary
    """

    def __init__(self):
        self.totalAudio = None
        self.vocalsAudio = None
        self.drumsAudio = None
        self.bassAudio = None
        self.otherAudio = None
        self.audio = None


    def setSongTracksData(self, sample_rate = 44100,
                            totalAudio = None,
                            vocalsAudio = None,
                            drumsAudio = None,
                            bassAudio = None,
                            otherAudio = None):
        """
        Load the tracks' audio
        """
        if totalAudio is None:
            totalAudio = np.zeros(1)

        if vocalsAudio is None:
            vocalsAudio = np.zeros(len(totalAudio))

        if drumsAudio is None:
            drumsAudio = np.zeros(len(totalAudio))

        if bassAudio is None:
            bassAudio = np.zeros(len(totalAudio))

        if otherAudio is None:
            otherAudio = np.zeros(len(totalAudio))

        self.totalAudio = totalAudio
        self.vocalsAudio = vocalsAudio
        self.drumsAudio = drumsAudio
        self.bassAudio = bassAudio          
        self.otherAudio = otherAudio

        self.sample_rate = sample_rate


    def setTracksVolumes(self,
                   totalVolume = 100,
                   vocalsVolume = 100,
                   drumsVolume = 100,
                   bassVolume = 100,
                   otherVolume = 100
                   ):
        """
        Set the volume of each track:


        """
        # tempVocalsAudio = self.vocalsAudio * (1.05 ** (vocalsVolume) - 1) / 130.5
        # tempDrumsAudio = self.drumsAudio * (1.05 ** (drumsVolume) - 1) / 130.5
        # tempBassAudio = self.bassAudio * (1.05 ** (bassVolume) - 1) / 130.5
        # tempOtherAudio = self.otherAudio * (1.05 ** (otherVolume) - 1) / 130.5

        tempVocalsAudio = self.vocalsAudio * vocalsVolume / 100
        tempDrumsAudio = self.drumsAudio * drumsVolume / 100
        tempBassAudio = self.bassAudio * bassVolume / 100
        tempOtherAudio = self.otherAudio * otherVolume / 100

        # Sum and normalize

        self.audio = (tempVocalsAudio + tempDrumsAudio + tempBassAudio + tempOtherAudio)

        self.audio = self.audio / np.max(np.abs(self.audio))

        # Apply master volume
        #self.audio = self.audio * ((1.05 ** (totalVolume) - 1) / 130.5)
        self.audio = self.audio * totalVolume / 100

        # Resample audioto 44100 Hz
        if self.sample_rate != 44100:
            self.audio = resample(self.audio, orig_sr =self.sample_rate, target_sr=44100)

    def getAudio(self):
        """
        Return the audio.
        - Sample Rate = 44100 Hz
        """
        return self.audio
    
