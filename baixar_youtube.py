"""
Baixa áudio de vídeos do YouTube, fatia em segmentos de até 3 s e salva como .wav
em datasets/new_audio.

Dependências:
    pip install yt-dlp
    brew install ffmpeg   (macOS)
    # ou: conda install -c conda-forge ffmpeg

Uso:
    python baixar_youtube.py <url> [url2 url3 ...]
    python baixar_youtube.py <url> --output datasets/new_audio
    python baixar_youtube.py --list urls.txt
"""

import os
import subprocess
import sys
import tempfile

SEGMENT_DURATION = 3          # segundos por segmento
DEFAULT_OUTPUT   = os.path.join("datasets", "new_audio")
SAMPLE_RATE      = 22050


def check_dependencies():
    missing = []
    try:
        import yt_dlp  # noqa: F401
    except ImportError:
        missing.append("yt-dlp  →  pip install yt-dlp")

    if subprocess.run(["which", "ffmpeg"], capture_output=True).returncode != 0:
        missing.append("ffmpeg  →  brew install ffmpeg")

    if missing:
        print("Dependências ausentes:")
        for m in missing:
            print(f"  {m}")
        sys.exit(1)


def download_full_wav(url: str, tmp_dir: str) -> str:
    """Baixa um vídeo como .wav completo em tmp_dir e retorna o caminho do arquivo."""
    import yt_dlp

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(tmp_dir, "%(id)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
            }
        ],
        "postprocessor_args": ["-ar", str(SAMPLE_RATE)],
        "quiet": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_id = info["id"]

    wav_path = os.path.join(tmp_dir, f"{video_id}.wav")
    return wav_path


def get_duration(wav_path: str) -> float:
    """Retorna a duração em segundos usando ffprobe."""
    result = subprocess.run(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            wav_path,
        ],
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def slice_wav(wav_path: str, output_dir: str, base_name: str) -> list[str]:
    """
    Divide wav_path em segmentos de SEGMENT_DURATION segundos.
    Retorna a lista de arquivos gerados.
    """
    duration   = get_duration(wav_path)
    n_segments = int(duration // SEGMENT_DURATION)
    if n_segments == 0:
        n_segments = 1  # áudio menor que 3 s → salva como está

    saved = []
    for i in range(n_segments):
        start    = i * SEGMENT_DURATION
        out_file = os.path.join(output_dir, f"{base_name}_seg{i+1:03d}.wav")
        cmd = [
            "ffmpeg", "-y",
            "-ss", str(start),
            "-t",  str(SEGMENT_DURATION),
            "-i",  wav_path,
            "-ar", str(SAMPLE_RATE),
            out_file,
        ]
        subprocess.run(cmd, capture_output=True, check=True)
        saved.append(out_file)
        print(f"  [{i+1}/{n_segments}] {out_file}")

    return saved


def process_urls(entries: list[tuple[str, str]], output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp_dir:
        for idx, (prefix, url) in enumerate(entries, 1):
            print(f"\n[{idx}/{len(entries)}] Baixando '{prefix}': {url}")
            try:
                wav_path = download_full_wav(url, tmp_dir)
                print(f"  Fatiando em segmentos de {SEGMENT_DURATION} s …")
                slice_wav(wav_path, output_dir, prefix)
            except Exception as e:
                print(f"  ERRO: {e}")


def main():
    entries = [
        ("cla", "https://www.youtube.com/watch?v=kSfEDb1cMAw"),
        ("vio", "https://www.youtube.com/watch?v=wh-pBxeHE3U"),
        ("pia", "https://www.youtube.com/watch?v=KA0Yh1OxJVI"),
    ]

    check_dependencies()
    print(f"Destino: '{DEFAULT_OUTPUT}'")
    process_urls(entries, output_dir=DEFAULT_OUTPUT)
    print("\nConcluído.")


if __name__ == "__main__":
    main()
