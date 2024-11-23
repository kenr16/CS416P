print("Starting dependency imports...")
from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import soundfile as sf
print("Dependencies successfully imported.")

# Parameters for the sine wave
frequency = 440  # Hz
amplitude = 8192   # 1/4 maximum possible 16-bit aplitude value
duration = 1  # seconds
sampling_rate = 48000  # samples per second

# Generate time values
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate sine wave
sine_wave1 = amplitude * np.sin(2 * np.pi * frequency * t)

# Export the first sine wave to sine.wav
print("Exporting first sound file to 'sine.wav'")
sf.write('code/sine.wav', sine_wave1, sampling_rate)
print("Done")

# Plot the sine wave
#print("Plotting sine wave on graph...")
#plt.plot(t, sine_wave1)
#plt.xlabel('Time (s)')
#plt.ylabel('Amplitude')
#plt.title('Sine Wave')
#plt.grid(True)
#plt.show()
#print("Sine wave plotted.")

# Generate a sine wave with 2x the amplitude
sine_wave2 = 2 * amplitude * np.sin(2 * np.pi * frequency * t)

# Clip the sine wave
clipping_level = 8192
clipped_wave = np.clip(sine_wave2, -clipping_level, clipping_level)

# Export the second sine wave to clipped.wav
print("Exporting second sound file to 'clipped.wav'")
sf.write('sound/clipped.wav', clipped_wave, sampling_rate)
print("Done")

# Plot the original and clipped sine waves
print("Plotting both sine wave on graph...")
plt.plot(t, sine_wave1, label='Original Sine Wave')
plt.plot(t, clipped_wave, label='Clipped Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
print("Sine waves plotted.")

# Play the clipped sound wave to the computer's audio

sd.play(clipped_wave)
sd.wait()  # Wait until playback is finished