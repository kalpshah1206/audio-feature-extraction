import sounddevice as sd
import numpy as np
from pydub import AudioSegment
# from playsound import playsound
import librosa


# Define a function to record audio from the microphone
# and save it to a file

def record_audio(file_path, duration=5, sample_rate=44100):
    print("Recording...")

    # Record audio from the microphone
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()

    # Convert to AudioSegment
    audio_segment = AudioSegment(audio_data.tobytes(), frame_rate=sample_rate, sample_width=2, channels=1)

    # Save the recorded audio
    audio_segment.export(file_path, format="wav")
    print(f"Audio recorded and saved at: {file_path}")


# Specify the file path where you want to save the recorded audio
wav_file_path = "recorded_audio.wav"

# Record audio from the microphone and save to a file
record_audio(wav_file_path, duration=5, sample_rate=44100)

# Play the saved audio file using playsound
print("Playing the recorded audio...")
# playsound(wav_file_path)


# Define a function to extract audio features
def extract_audio_features(file_path):
    # Load audio file using librosa
    y, sr = librosa.load(file_path, sr=None)

    # Calculate volume
    volume = np.mean(librosa.feature.rms(y=y))

    # Calculate MFCC features
    # mfccs = librosa.feature.mfcc(y, sr=sr, n_mfcc=13)

    # Calculate pitch (fundamental frequency)
    pitch, _ = librosa.core.piptrack(y=y, sr=sr)
    pitch_frequency = np.nanmean(librosa.pitch_tuning(pitch))

    return volume, pitch_frequency


# Specify the path to the audio file
audio_file_path = "recorded_audio.wav"

# Extract features
volume, pitch_frequency = extract_audio_features(audio_file_path)

# Display the extracted features
print("Audio features:")
print(f'Volume: {volume}')
# print(f'MFCCs shape: {mfccs.shape}')
print(f'Average Pitch: {pitch_frequency} Hz')

# input("Press Any key to exit ...")