import librosa
import numpy as np

sr = 22050
fs = 2048   # n_fft
hs = 512    # hop_length
mfcc_dim = 13
ms = 128    # n_mels

def extract_feature(samples):
    result = []
    features = []

    # Timbre features
    spectral_centroid   = librosa.feature.spectral_centroid(y=samples, sr=sr, n_fft=fs, hop_length=hs)
    spectral_bandwidth  = librosa.feature.spectral_bandwidth(y=samples, sr=sr, n_fft=fs, hop_length=hs)
    spectral_contrast   = librosa.feature.spectral_contrast(y=samples, sr=sr, n_fft=fs, hop_length=hs)
    spectral_rolloff    = librosa.feature.spectral_rolloff(y=samples, sr=sr, n_fft=fs, hop_length=hs)
    spectral_flux       = librosa.onset.onset_strength(y=samples, sr=sr, center=True)
    zero_crossing       = librosa.feature.zero_crossing_rate(y=samples, frame_length=fs, hop_length=hs)

    # MFCCs (baseados na DCT — variante da DFT)
    mfcc = librosa.feature.mfcc(y=samples, sr=sr, n_fft=fs, hop_length=hs, n_mfcc=mfcc_dim)

    # Mel-spectrogram (representação 2D — "imagem" do sinal)
    mel_scale = librosa.feature.melspectrogram(y=samples, sr=sr, n_fft=fs, hop_length=hs, n_mels=ms)
    mel_scale = librosa.power_to_db(mel_scale)

    features.append(spectral_centroid)
    features.append(spectral_bandwidth)
    features.append(spectral_contrast)
    features.append(spectral_rolloff)
    features.append(spectral_flux)
    features.append(zero_crossing)

    for feature in features:
        result.append(np.mean(feature))
        result.append(np.std(feature))

    for i in range(mfcc_dim):
        result.append(np.mean(mfcc[i, :]))
        result.append(np.std(mfcc[i, :]))

    return result