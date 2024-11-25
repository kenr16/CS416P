print("Starting dependency imports...")
import numpy as np
from scipy.io import wavfile
print("Dependencies successfully imported.")

# Define the white noise function
print("Creating white noise function...")
def white_noise(sample_rate, duration, intensity):
    noise = np.random.normal(0, intensity, sample_rate * duration)
    wavfile.write("sound/white_noise.wav", sample_rate, noise.astype(np.int16))
    return noise

# Create the parameters for white noise
sample_rate = 44100  # Samples per second
duration = 3  # Duration in seconds
intensity = 1000 # Intensity of the noise (Up to 32000)

# Generate the white noise sound and scale to 16-bit integer range
whitenoise = white_noise(sample_rate, duration, intensity)



