print("Starting dependency imports...")
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
print("Dependencies successfully imported.")


# Create a sample signal
time = np.linspace(0, 1, 1000)  # Time vector
frequency = 5  # Frequency of the signal
sine_wave = np.sin(2 * np.pi * frequency * time)  # Sine wave

# Compute the Fourier transform
Fourier_transform = np.fft.fft(sine_wave)  # Use the Fast Fourier Transform (FFT)

# Calculate the frequencies corresponding to the FFT output
freqs = np.fft.fftfreq(len(sine_wave), time[1] - time[0])

# Plot the original signal and its Fourier transform
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(time, sine_wave)
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