print("Starting dependency imports...")
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import numpy as np
print("Dependencies successfully imported.")

# Read the WAV file
print("Reading in the .wav files...")
samplerate1, data1 = wavfile.read('code\sine.wav')
print("Sample rate:", samplerate1)
print("Data:", data1)

samplerate2, data2 = wavfile.read('code\clipped.wav')
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


#import wave
# Open the WAV file
#with wave.open('code\sine.wav', 'rb') as wav_file:  #rb for read binary, wb for write binary.
    # Get file parameters
    #sample_rate = wav_file.getframerate()
    #n_frames = wav_file.getnframes()
    #n_channels = wav_file.getnchannels()

    # Read the audio data
    #signal = wav_file.readframes(n_frames)
    #signal = np.frombuffer(signal, dtype=np.int16)

    # If stereo, average the channels
    #if n_channels == 2:
        #signal = signal.reshape(-1, 2).mean(axis=1)

# Create a time vector
#time = np.arange(0, n_frames) / sample_rate

# Plot the waveform
#plt.plot(time, signal)
#plt.xlabel('Time (s)')
#plt.ylabel('Amplitude')
#plt.title('Waveform of your_audio_file.wav')
#plt.show()

