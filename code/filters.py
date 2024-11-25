print("Starting dependency imports...")
import numpy as np
from scipy.signal import butter, filtfilt
from scipy.io import wavfile
print("Dependencies successfully imported.")

# Define a low-pass filter function
print("Creating low-pass filter...")
def lowpass_filter(data, cutoff_frequency, sampling_rate, filter_order):
    nyquest_frequency = sampling_rate / 2
    normal_cutoff = cutoff_frequency / nyquest_frequency
    b, a = butter(filter_order, normal_cutoff, btype='lowpass') #'highpass' is also possible here
    y = filtfilt(b, a, data)
    return y # Returns the filtered audio data as a NumPy array.

# Define a high-pass filter function
print("Creating high-pass filter...")
def highpass_filter(data, cutoff_frequency, sampling_rate, filter_order):
    nyquest_frequency = sampling_rate / 2
    normal_cutoff = cutoff_frequency / nyquest_frequency
    b, a = butter(filter_order, normal_cutoff, btype='highpass') #'highpass' is also possible here
    y = filtfilt(b, a, data)
    return y # Returns the filtered audio data as a NumPy array.

# Define a band-pass filter function
print("Creating band-pass filter...")
def bandpass_filter(data, low_cutoff_frequency, high_cutoff_frequency, sampling_rate, filter_order):
    nyquest_frequency = sampling_rate / 2
    low_cutoff = low_cutoff_frequency / nyquest_frequency
    high_cutoff = high_cutoff_frequency/ nyquest_frequency
    b, a = butter(filter_order, [low_cutoff, high_cutoff], btype='bandpass') #'highpass' and 'lowpass' are also possible here
    y = filtfilt(b, a, data)
    return y # Returns the filtered audio data as a NumPy array.

# Calculate the sound energy of audio
print("Creating sound energy function...")
def sound_energy(data):
    fourier_transform = np.fft.fft(data)  # Use the Fast Fourier Transform (FFT)
    magnitude_spectrum = np.abs(fourier_transform)
    power_spectrum = magnitude_spectrum ** 2
    sound_energy = np.sum(power_spectrum)
    return sound_energy

# Sound band energy equalization function
print("Creating sound band equalization function...")
def equalize_bands(low_band, mid_band, high_band):
    low_energy = sound_energy(low_band)
    mid_energy = sound_energy(mid_band)
    high_energy = sound_energy(high_band)
    average_energy = (low_energy + mid_energy + high_energy) / 3
    print("Low energy ratio: " + str(low_energy/average_energy))
    print("Band energy ratio: " + str(mid_energy/average_energy))
    print("High energy ratio: " + str(high_energy/average_energy))
    equalized_low_band = low_band / (low_energy/average_energy)
    equalized_mid_band = mid_band / (mid_energy/average_energy)
    equalized_high_band = high_band / (high_energy/average_energy)
    equalized_audio = equalized_low_band + equalized_mid_band + equalized_high_band
    return equalized_audio

# Load audio file and get sampling rate
print("Retriving audio file...")
sampling_rate, data = wavfile.read('sound/dont_speak-no_doubt.wav')

#Create and apply low-pass filter
print("Applying low-pass filter...")
cutoff_frequency = 300  #Hz
filter_order = 5
filtered_data_low = lowpass_filter(data, cutoff_frequency, sampling_rate, 5)

#Create and apply high-pass filter
print("Applying high-pass filter...")
cutoff_frequency = 2000  #Hz
filter_order = 5
filtered_data_high = highpass_filter(data, cutoff_frequency, sampling_rate, 5)

#Create and apply band-pass filter
print("Applying band-pass filter...")
low_cutoff_frequency = 300  #Hz
high_cutoff_frequency = 2000  #Hz
filter_order = 5
filtered_data_band = bandpass_filter(data, low_cutoff_frequency, high_cutoff_frequency, sampling_rate, 5)

# Equalizie the audio bands
print("Equalizing the audio bands...")
equalized_audio_data = equalize_bands(filtered_data_low, filtered_data_high, filtered_data_band)


# Saving filtered audio
print("Saving audio files...")
wavfile.write('sound/low_filtered_audio.wav', sampling_rate, filtered_data_low.astype(np.int16))
wavfile.write('sound/high_filtered_audio.wav', sampling_rate, filtered_data_high.astype(np.int16))
wavfile.write('sound/band_filtered_audio.wav', sampling_rate, filtered_data_band.astype(np.int16))
wavfile.write('sound/equalized_audio.wav', sampling_rate, equalized_audio_data.astype(np.int16))


#sampling_rate, data = wavfile.read('sound/africa-toto.wav')
#wavfile.write('sound/echoed_audio.wav', sampling_rate, echoed_data)


#Create sample data
#print("Creating sample data...")
#time = np.linspace(0, 1, 1000)  #Time vector
#data = np.sin(2*np.pi*150*time) + np.random.rand(1000)  #Create example sine wave

#Plot the graph of the signals
#print("Plotting graph of the signals...")
#plt.figure(figsize=(10, 6))
#plt.plot(time, data, label='Original Signal')
#plt.plot(time, filtered_data_low, label='Low Filtered Signal')
#plt.plot(time, filtered_data_high, label='High Filtered Signal')
#plt.plot(time, filtered_data_band, label='Band Filtered Signal')
#plt.xlabel('Time in seconds')
#plt.ylabel('Amplitude')
#plt.title('Low-Pass Filter')
#plt.legend()
#plt.grid(True)
#plt.show()





