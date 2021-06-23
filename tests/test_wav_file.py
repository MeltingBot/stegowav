import hashlib
import random
import string
from pathlib import Path

from wav_steganography.wav_file import WAVFile

audio_path = Path("audio")


def get_random_string(position_of_element: int) -> str:
    return ''.join(random.choice(string.ascii_letters) for _ in
                   range(random.randint(position_of_element, position_of_element)))


def get_file_path(filename):
    encoded_dir_path = audio_path / "encoded"
    encoded_dir_path.mkdir(exist_ok = True)
    encoded_file_path = encoded_dir_path / filename

    return encoded_file_path


def test_loading_and_plotting_wav_file():
    for audio_file in audio_path.glob("*.wav"):
        print(f"Loading audio file {audio_file}")
        file = WAVFile(audio_file)
        plots_path = audio_path / 'plots'
        plots_path.mkdir(exist_ok=True)
        file.plot(to_s=None, filename=plots_path / audio_file.name.replace(".wav", ".png"))


def test_loading_and_writing_wav_file():
    for audio_file in audio_path.glob("*.wav"):
        md5checksum = hashlib.md5(open(audio_file, 'rb').read()).hexdigest()
        print(f"Loading audio file {audio_file}")
        file = WAVFile(audio_file)
        written_path = audio_path / 'copied'
        written_path.mkdir(exist_ok=True)
        copied_file_path = written_path / audio_file.name
        file.write(copied_file_path, overwrite=True)
        copied_md5checksum = hashlib.md5(open(copied_file_path, 'rb').read()).hexdigest()
        assert md5checksum == copied_md5checksum, "Checksums mismatch!"


def test_encoding_decoding():
    for audio_file in audio_path.glob("*.wav"):
        file = WAVFile(audio_file)

        data_string = get_random_string(10000)
        data = data_string.encode("UTF-8")

        file.encode(data)

        encoded_file_path = get_file_path(audio_file.name)

        file.write(encoded_file_path, overwrite=True)

        encoded_file = WAVFile(encoded_file_path)

        decoded_data = encoded_file.decode()

        assert \
            decoded_data == data, "Decoded message is not the same as the encoded one!"


def test_encoding_decoding_with_error_correction():
    for audio_file in audio_path.glob("*.wav"):
        file = WAVFile(audio_file)

        data_string = get_random_string(7340)
        data = data_string.encode("UTF-8")

        file.encode(data, error_correction=True)

        encoded_file_path = get_file_path(audio_file.name)

        file.write(encoded_file_path, overwrite=True)

        encoded_file = WAVFile(encoded_file_path)

        decoded_data = encoded_file.decode(error_correction=True)

        assert \
            decoded_data == data, "Decoded and corrected message is not the same as the encoded one!"
