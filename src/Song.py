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


    def setSongTracksData(self,
                            totalAudio = None,
                            vocalsAudio = None,
                            drumsAudio = None,
                            bassAudio = None):
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

        self.totalAudio = totalAudio
        self.vocalsAudio = vocalsAudio
        self.drumsAudio = drumsAudio
        self.bassAudio = bassAudio          

        self.otherAudio = self.totalAudio - self.vocalsAudio - self.drumsAudio - self.bassAudio


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
        tempVocalsAudio = self.vocalsAudio * (1.05 ** (vocalsVolume) - 1) / 130.5
        tempDrumsAudio = self.drumsAudio * (1.05 ** (drumsVolume) - 1) / 130.5
        tempBassAudio = self.bassAudio * (1.05 ** (bassVolume) - 1) / 130.5
        tempOtherAudio = self.otherAudio * (1.05 ** (otherVolume) - 1) / 130.5

        # Sum and normalize

        self.audio = (tempVocalsAudio + tempDrumsAudio + tempBassAudio + tempOtherAudio)

        self.audio = self.audio / np.max(np.abs(self.audio))

        # Apply master volume
        self.audio = self.audio * ((1.05 ** (totalVolume) - 1) / 130.5)

        # Resample audioto 22050 Hz
        self.audio = resample(self.audio, orig_sr = 8196, target_sr=22050)

    def getAudio(self):
        """
        Return the audio.
        - Sample Rate = 22050 Hz
        """
        return self.audio
    
