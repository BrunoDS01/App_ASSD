import numpy as np
import librosa
#from librosa.display import specshow
import keras as keras
import soundfile as sf
import os

SAMPLE_RATE=8192
WINDOW_SIZE=1024
HOP_LENGTH=768

PATCH_SIZE=128
EPOCH = 1 # test
BATCH = 16
SAMPLE_STRIDE = 10

class Predict_U_Net:
    """
    U-Net for Music Source Separation, using pretrained models    
    """
    def __init__(self):
        # load saved models
        self.model_vocals = keras.models.load_model('src/models/vocal_PRUEBA_vocals.h5')
        self.model_drums = keras.models.load_model('src/models/vocal_PRUEBA_drums.h5')

    def predictWithU_Net(self, songPath):
        """
        Process the chosen song with the trained U-Net architecture.
        It will produce 2 tracks:
            - Vocals
            - Drums
            - Others
        """
        vocalsSpec = None
        drumsSpec = None
        # load saved model

        filename = os.path.basename(songPath)

        mix_wav, _ = librosa.load(songPath, sr=SAMPLE_RATE)
        mix_wav_mag_full, mix_wav_phase_full = librosa.magphase(librosa.stft(mix_wav, n_fft=WINDOW_SIZE, hop_length=HOP_LENGTH))

        timeFrames = mix_wav_mag_full.shape[1]

        START = 0

        for START in range(0, timeFrames, 128):

            END = START + 128
            if END > timeFrames:
                END = timeFrames

                mix_wav_mag = mix_wav_mag_full[:, START:END]
                mix_wav_phase = mix_wav_phase_full[:, START:END]

                matrix_zeros = np.zeros((mix_wav_mag.shape[0], 128 - (END - START)))

                mix_wav_phase_full = np.concatenate((mix_wav_phase_full, matrix_zeros), axis=1)

                # Concatenate matrices along columns
                mix_wav_mag = np.concatenate((mix_wav_mag, matrix_zeros), axis=1)
                mix_wav_phase = np.concatenate((mix_wav_phase, matrix_zeros), axis=1)
            else:
                mix_wav_mag = mix_wav_mag_full[:, START:END]
                mix_wav_phase = mix_wav_phase_full[:, START:END]

            # predict vocals
            X = mix_wav_mag[1:].reshape(1, 512, 128, 1)
            y_vocals_p = self.model_vocals.predict(X, batch_size=32)
            y_vocals = np.vstack((np.zeros((128)), y_vocals_p.reshape(512, 128)))

            y_drums_p = self.model_drums.predict(X, batch_size=32)
            y_drums = np.vstack((np.zeros((128)), y_drums_p.reshape(512, 128)))

            if START == 0:
                vocalsSpec = y_vocals
                drumsSpec = y_drums
            else: 
                vocalsSpec = np.concatenate((vocalsSpec, y_vocals), axis=1)
                drumsSpec = np.concatenate((drumsSpec, y_drums), axis=1)
        
        # spectrogram_db = librosa.power_to_db(X[0,:,:,0], ref=np.max)

        # # Display the spectrogram
        # plt.figure(figsize=(10, 6))
        # specshow(spectrogram_db, sr=SAMPLE_RATE)
        # plt.colorbar(format='%+2.0f dB')
        # plt.title('Spectrogram')
        # plt.show()

        
        sf.write('src/results/' + filename + '_vocals.wav',
                librosa.istft(vocalsSpec * mix_wav_phase_full, win_length=WINDOW_SIZE, hop_length=HOP_LENGTH), SAMPLE_RATE)
        
        sf.write('src/results/' + filename + '_drums.wav',
                librosa.istft(drumsSpec * mix_wav_phase_full, win_length=WINDOW_SIZE, hop_length=HOP_LENGTH), SAMPLE_RATE)