print("Starting dependency imports...")
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import numpy as np
print("Dependencies successfully imported.")

# Read the WAV file
print("Reading in the .wav files...")
samplerate1, data1 = wavfile.read('sound/sine.wav')
print("Sample rate:", samplerate1)
print("Data:", data1)

samplerate2, data2 = wavfile.read('sound/clipped.wav')
print("Sample rate:", samplerate2)
print("Data:", data2)

time = np.arange(0, len(data1)) / samplerate1

# Plot the waveform
print("Graphing the .wav files...")
plt.plot(time, data1, label='Original Sine Wave')
plt.plot(time, data2, label='Clipped Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Waveform')
plt.title('Waveform of imported .wav file')
plt.show()