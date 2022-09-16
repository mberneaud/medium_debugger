import os


def get_abspath(filename: str):
    return os.path.abspath(filename)


for i, file in enumerate(os.listdir("audio_data")):
    speaker_id = file.split("_")[-1][:-len(".flac")]
    print(f"File {i}: {get_abspath(file)}; Speaker id: {speaker_id}")
