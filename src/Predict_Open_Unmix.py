import torch
import librosa
from openunmix import predict

from src.youtubeDownloader import downloadYoutubeAudio


class Predict_Open_Unmix:
    """
    Open Unmix for Music Source Separation, using pretrained models
    """
    def __init__(self):
        use_cuda = torch.cuda.is_available()
        self.device = torch.device("cuda" if use_cuda else "cpu")

    def predictWithOpenUnmix(self, songPath, youtube = False):
        # Load song
        if not youtube:
            mix_wav, sr = librosa.load(songPath, sr=44100)
        else:
            mix_wav, sr = downloadYoutubeAudio(songPath)


        estimates = predict.separate(
            torch.as_tensor(mix_wav).float(),
            #model_str_or_path = "umxhq",
            rate=sr,
            device=self.device
        )
        vocalsAudio = estimates['vocals'].detach().cpu().numpy()[0][0] + estimates['vocals'].detach().cpu().numpy()[0][1]
        drumsAudio = estimates['drums'].detach().cpu().numpy()[0][0] + estimates['drums'].detach().cpu().numpy()[0][1]
        bassAudio = estimates['bass'].detach().cpu().numpy()[0][0] + estimates['bass'].detach().cpu().numpy()[0][1]
        otherAudio = estimates['other'].detach().cpu().numpy()[0][0] + estimates['other'].detach().cpu().numpy()[0][1]
        totalAudio = vocalsAudio + drumsAudio + bassAudio + otherAudio

        return totalAudio, vocalsAudio, drumsAudio, bassAudio, otherAudio