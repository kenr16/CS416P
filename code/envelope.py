print("Starting dependency imports...")
import numpy as np
import scipy.io.wavfile as wavfile
print("Dependencies successfully imported.")

# Define the envelope effect function
print("Defining the envelope function...")
def envelope(duration, attack_time, decay_time, release_time):
    attack = np.linspace(0, 1, int(attack_time * sample_rate)) # Time for the volume to rise initially from zero
    decay = np.linspace(1, 0.8 , int(decay_time * sample_rate)) # Decay is the decline after the initial volume spike.
    sustain = np.linspace(0.8, 0.8, int((duration - attack_time  - decay_time - release_time) * sample_rate)) # Time theat the note stays the same volume
    release = np.linspace(0.8, 0, int(release_time * sample_rate)) # Time during which the volume declines to zero
    return np.concatenate([attack, decay, sustain, release])

# Load audio file and get sampling rate
print("Retriving audio file...")
sample_rate, audio_data = wavfile.read('sound/sine.wav')

# Create an envelope
print("Creating envelope to apply...")
envelope = envelope(duration=1, attack_time=0.1, decay_time=0.1, release_time=0.5)

# Apply the envelope to the audio data
print("Applying envelope to audio files...")
enveloped_audio = audio_data * envelope[:len(audio_data)]

# Saving enveloped audio
print("Saving audio files...")
wavfile.write('sound/enveloped_audio.wav', sample_rate, enveloped_audio.astype(np.int16))