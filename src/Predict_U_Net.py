import numpy as np
import librosa
import keras as keras

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
        self.model_bass = keras.models.load_model('src/models/vocal_PRUEBA_bass.h5')


    def predictWithU_Net(self, songPath):
        """
        Process the chosen song with the trained U-Net architecture.
        It will produce 4 tracks:
            - Original, downsampled
            - Vocals
            - Drums
            - Bass
        """
        vocalsSpec = None
        drumsSpec = None

        # Obtain spectrograms, downsampling to a sr = 8192
        mix_wav, _ = librosa.load(songPath, sr=SAMPLE_RATE)
        mix_wav_mag_full, mix_wav_phase_full = librosa.magphase(librosa.stft(mix_wav, n_fft=WINDOW_SIZE, hop_length=HOP_LENGTH))

        timeFrames = mix_wav_mag_full.shape[1]

        START = 0

        # Predict for all batches of 11 seconds
        for START in range(0, timeFrames, 128):
            END = START + 128
            if END > timeFrames:
                END = timeFrames

                mix_wav_mag = mix_wav_mag_full[:, START:END]
                mix_wav_phase = mix_wav_phase_full[:, START:END]
                matrix_zeros = np.zeros((mix_wav_mag.shape[0], 128 - (END - START)))
                mix_wav_phase_full = np.concatenate((mix_wav_phase_full, matrix_zeros), axis=1)
                mix_wav_mag_full = np.concatenate((mix_wav_mag_full, matrix_zeros), axis=1)


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

            # predict drums
            y_drums_p = self.model_drums.predict(X, batch_size=32)
            y_drums = np.vstack((np.zeros((128)), y_drums_p.reshape(512, 128)))

            # predict bass
            y_bass_p = self.model_bass.predict(X, batch_size=32)
            y_bass = np.vstack((np.zeros((128)), y_bass_p.reshape(512, 128)))

            if START == 0:
                vocalsSpec = y_vocals
                drumsSpec = y_drums
                bassSpec = y_bass
            else: 
                vocalsSpec = np.concatenate((vocalsSpec, y_vocals), axis=1)
                drumsSpec = np.concatenate((drumsSpec, y_drums), axis=1)
                bassSpec = np.concatenate((bassSpec, y_bass), axis=1)
                
        # obtain audio, using the original phase and aplying ISTFT
        vocalsAudio = librosa.istft(vocalsSpec * mix_wav_phase_full, win_length=WINDOW_SIZE, hop_length=HOP_LENGTH) 
        drumsAudio = librosa.istft(drumsSpec * mix_wav_phase_full, win_length=WINDOW_SIZE, hop_length=HOP_LENGTH)
        bassAudio = librosa.istft(bassSpec * mix_wav_phase_full, win_length=WINDOW_SIZE, hop_length=HOP_LENGTH)
        totalAudio = librosa.istft(mix_wav_mag_full * mix_wav_phase_full, win_length=WINDOW_SIZE, hop_length=HOP_LENGTH)
        otherAudio = totalAudio - vocalsAudio - drumsAudio - bassAudio

        return vocalsAudio, vocalsAudio, drumsAudio, bassAudio, otherAudio
    

    def getSampleRate(self):
        return SAMPLE_RATE



# spectrogram_db = librosa.power_to_db(X[0,:,:,0], ref=np.max)

# # Display the spectrogram
# plt.figure(figsize=(10, 6))
# specshow(spectrogram_db, sr=SAMPLE_RATE)
# plt.colorbar(format='%+2.0f dB')
# plt.title('Spectrogram')
# plt.show()