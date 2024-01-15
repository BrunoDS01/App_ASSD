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
        self.audio = np.zeros(1)
        self.sample_rate = None

        self.muteTrackList = [False, False, False, False]

        self.emptySong = True

    def setSongTracksData(self, sample_rate = 44100,
                            totalAudio = None,
                            vocalsAudio = None,
                            drumsAudio = None,
                            bassAudio = None,
                            otherAudio = None):
        """
        Load the tracks' audio
        """
        # Indicate that audio has been uploaded
        self.emptySong = False

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

        # Apply volume to each track
        if self.emptySong:
            return
        tempVocalsAudio = self.vocalsAudio * (1.05 ** (vocalsVolume) - 1) / 130.5
        tempDrumsAudio = self.drumsAudio * (1.05 ** (drumsVolume) - 1) / 130.5
        tempBassAudio = self.bassAudio * (1.05 ** (bassVolume) - 1) / 130.5
        tempOtherAudio = self.otherAudio * (1.05 ** (otherVolume) - 1) / 130.5

        # tempVocalsAudio = self.vocalsAudio * vocalsVolume / 100
        # tempDrumsAudio = self.drumsAudio * drumsVolume / 100
        # tempBassAudio = self.bassAudio * bassVolume / 100
        # tempOtherAudio = self.otherAudio * otherVolume / 100

        # See if the track is mute or not

        if self.muteTrackList[0]:
            tempVocalsAudio *= 0
        
        if self.muteTrackList[1]:
            tempDrumsAudio *= 0

        if self.muteTrackList[2]:
            tempBassAudio *= 0

        if self.muteTrackList[3]:
            tempOtherAudio *= 0
            
        # Sum and normalize

        self.audio = (tempVocalsAudio + tempDrumsAudio + tempBassAudio + tempOtherAudio)

        # if np.max(np.abs(self.audio)) < np.finfo(float).eps:
        #     self.audio = 0
        # else:
        #     self.audio = self.audio / np.max(np.abs(self.audio))

        # Apply master volume
        self.audio = self.audio * ((1.05 ** (totalVolume) - 1) / 130.5)
        # self.audio = self.audio * totalVolume / 100

        # Resample audioto 44100 Hz
        if self.sample_rate != 44100:
            self.audio = resample(self.audio, orig_sr =self.sample_rate, target_sr=44100)

    def muteUnmuteTrack(self, track):
        """
        Mute/Unmute track:
        - 0: Vocals
        - 1: Drums
        - 2: Bass
        - 3: Other
        """
        if not self.muteTrackList[track]:
            self.muteTrackList[track] = True
        
        else:
            self.muteTrackList[track] = False


    def getAudio(self):
        """
        Return the audio.
        - Sample Rate = 44100 Hz
        """
        return self.audio
    
