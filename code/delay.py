print("Starting dependency imports...")
import numpy as np
from scipy.io import wavfile
print("Dependencies successfully imported.")

# Define the delay effect function
print("Defining the delay function...")
def create_delay(data, sampling_rate, delay_time):
    delay_samples = int(sampling_rate * delay_time)
    delay_data = np.zeros_like(data) # Create a new array with nothing but zeroes
    delay_data[delay_samples:] = data[:-delay_samples] # This slice notation refers to the portion of the delayed_signal array starting from index delay_samples and extending to the end of the array. Essentially, this is where the original signal (shifted by the delay) will be placed in the delayed signal.
    output_signal = data + delay_data # Mixing the wet and dry signals
    output_signal = np.clip(output_signal, -32768, 32767) # Clip the output signal to make certain that they are within range if INT16
    return output_signal

# Define the fade-in effect function
print("Defining the fade-in function...")
def fade_in(data, sampling_rate, fade_time):
    fade_samples = int(sampling_rate * fade_time)
    fade_curve = np.linspace(0, 1, fade_samples)  # Linear fade from 0 to 1
    data = data.astype(np.float64)  # Temporarily conversion
    data[:fade_samples] *= fade_curve  # Apply the fade curve to the beginning of the signal
    data = np.clip(data, -32768, 32767)  # Clip the values to ensure they are within the INT16 range
    return data.astype(np.int16) # Convert back

# Define the fade-out effect function
print("Defining the fade-out function...")
def fade_out(data, sampling_rate, fade_time):
    fade_samples = int(sampling_rate * fade_time)
    fade_curve = np.linspace(1, 0, fade_samples)  # Linear fade from 1 to 0
    data = data.astype(np.float64)  # Temporarily conversion
    data[-fade_samples:] *= fade_curve  # Apply the fade curve to the beginning of the signal
    data = np.clip(data, -32768, 32767)  # Clip the values to ensure they are within the INT16 range
    return data.astype(np.int16) # Convert back


# Read in the audio file to delay
print("Reading in the audio file...")
sampling_rate, data = wavfile.read('sound/dont_speak-no_doubt.wav')

# Check if the audio is stereo and convert to mono if necessary
if data.ndim > 1:
    data = data.mean(axis=1).astype(np.int16)  # Convert to mono by averaging channels

# Add delay
print("Adding delay...")
delay_time = 1.0  # The delay time in seconds for the delay. (1000ms = 1sec delay)
delay_data = create_delay(data, sampling_rate, delay_time)
print("Adding fade-in...")
fade_time = 10.0  # The fade_in time in seconds. (1000ms = 1sec fade-in)
fadein_data = fade_in(data, sampling_rate, fade_time)
print("Adding fade-out...")
fade_time = 260.0  # The fade_in time in seconds. (1000ms = 1sec fade-out)
fadeout_data = fade_out(data, sampling_rate, fade_time)

# Save the modified audio
print("Saving the modified audio file...")
wavfile.write('sound/delayed_audio.wav', sampling_rate, delay_data.astype(np.int16))
wavfile.write('sound/fadein_audio.wav', sampling_rate, fadein_data.astype(np.int16))
wavfile.write('sound/fadeout_audio.wav', sampling_rate, fadeout_data.astype(np.int16))