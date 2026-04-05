import librosa
import numpy as np

def carregar_audio(caminho_arquivo, sr=22050):
    y, _ = librosa.load(caminho_arquivo, sr=sr)

    # normalizacao de amplitude
    y = y / (np.max(np.abs(y)) + 1e-8)
    return y