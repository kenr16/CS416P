print("Starting dependency imports...")
import numpy as np
from scipy.io import wavfile
print("Dependencies successfully imported.")

# Define the echo effect function
print("Defining the echo function...")
def create_echo(data, sampling_rate, delay_time, decay_rate, mix):
    delay = int(sampling_rate * delay_time)
    echo = np.zeros_like(data)
    for i in range(delay, len(data)):
        echo[i] = data[i - delay] * decay_rate
    output_signal = (1 - mix) * data + mix * echo # Mixing the wet and dry signals
    output_signal = np.clip(output_signal, -32768, 32767) # Clip the output signal to make certain that they are within range if INT16
    return output_signal

# Read in the audio file to echo
print("Reading in the audio file...")
sampling_rate, data = wavfile.read('sound/dont_speak-no_doubt.wav')

# Check if the audio is stereo and convert to mono if necessary
if data.ndim > 1:
    data = data.mean(axis=1).astype(np.int16)  # Convert to mono by averaging channels

# Add echo
print("Adding echo...")
delay_time = 0.5  # The delay time in seconds for the echo. (500ms delay)
decay_rate = 0.5  # Decay for each repetition (0.5 = half)
mix = 0.5  # Mix of dry and wet signals (50% mix)
echoed_data = create_echo(data, sampling_rate, delay_time, decay_rate, mix)

# Save the modified audio
print("Saving the modified audio file...")
wavfile.write('sound/echoed_audio.wav', sampling_rate, echoed_data.astype(np.int16))