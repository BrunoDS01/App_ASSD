import torch
import librosa
import torchaudio
import numpy as np
import scipy
import os
from openunmix import umxl, predict
from openunmix.utils import preprocess


class Predict_Open_Unmix:
    """
    Open Unmix for Music Source Separation, using pretrained models
    """
    def __init__(self):
        use_cuda = torch.cuda.is_available()
        self.device = torch.device("cuda" if use_cuda else "cpu")

    def predictWithOpenUnmix(self, songPath):
        # Load song
        mix_wav, sr = librosa.load(songPath, sr=44100)

        estimates = predict.separate(
            torch.as_tensor(mix_wav).float(),
            rate=sr,
            device=self.device
        )
        vocalsAudio = estimates['vocals'].detach().cpu().numpy()[0][0] + estimates['vocals'].detach().cpu().numpy()[0][1]
        drumsAudio = estimates['drums'].detach().cpu().numpy()[0][0] + estimates['drums'].detach().cpu().numpy()[0][1]
        bassAudio = estimates['bass'].detach().cpu().numpy()[0][0] + estimates['bass'].detach().cpu().numpy()[0][1]
        otherAudio = estimates['other'].detach().cpu().numpy()[0][0] + estimates['other'].detach().cpu().numpy()[0][1]
        totalAudio = vocalsAudio + drumsAudio + bassAudio + otherAudio

        return totalAudio, vocalsAudio, drumsAudio, bassAudio, otherAudio