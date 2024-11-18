print("Starting dependency imports...")
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
print("Dependencies successfully imported.")

# Function to generate a sine wave.
def create_wave(frequency, amplitude, duration, sampling_rate):
    time = np.linspace(0, duration, int(sampling_rate * duration))
    return amplitude * np.sin(2 * np.pi * frequency * time)


# Parameters for the sine wave
frequency = 440  # Hz
amplitude = 8192   # 1/4 maximum possible 16-bit aplitude value
duration = 1  # seconds
sampling_rate = 48000  # samples per second

# Generate time values
time = np.linspace(0, duration, int(sampling_rate * duration))

# Generate sine wave
sine_wave1 = create_wave(frequency, amplitude, duration, sampling_rate)

# Generate a sine wave with 4x the frequency and 1/2 the amplitude
amplitude = 4046
frequency = 1760
sine_wave2 = create_wave(frequency, amplitude, duration, sampling_rate)

# Generate a sine wave with 32x the frequency and 1/4 the amplitude
amplitude = 2023
frequency = 14080
sine_wave3 = create_wave(frequency, amplitude, duration, sampling_rate)

# Add all three sine waves together
final_sine_wave = sine_wave1 + sine_wave2 + sine_wave3

# Plot the sine waves added together
print("Plotting both sine wave on graph...")
plt.plot(time, sine_wave1, label='Original Sine Wave')
plt.plot(time, final_sine_wave, label='Added Sine Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
print("Sine waves plotted.")


# Compute the Fourier transform
Fourier_transform = np.fft.fft(final_sine_wave)  # Use the Fast Fourier Transform (FFT)

# Calculate the frequencies corresponding to the FFT output
freqs = np.fft.fftfreq(len(final_sine_wave), time[1] - time[0])

# Plot the original signal and its Fourier transform
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(time, final_sine_wave)
plt.title("Original Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.subplot(2, 1, 2)
plt.plot(freqs, np.abs(Fourier_transform))
plt.title("Fourier Transform")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.show()




#Plot the sine wave
#print("Plotting sine wave on graph...")
#plt.plot(time, sine_wave1)
#plt.xlabel('Time (s)')
#plt.ylabel('Amplitude')
#plt.title('Sine Wave')
#plt.grid(True)
#plt.show()
#print("Sine wave plotted.")