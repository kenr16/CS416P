print("Starting dependency imports...")
import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
import soundfile as sf
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

# Load audio file and get sampling rate
print("Retriving audio file...")
data, sampling_rate = sf.read('audio.wav') #data: The audio data as a NumPy array.

#Create and apply low-pass filter
print("Applying low-pass filter...")
cutoff_frequency = 100000  #Hz
filter_order = 5
filtered_data = lowpass_filter(data, cutoff_frequency, sampling_rate)

# Saving filtered audio
print("Saving audio file...")
sf.write('low_filtered_audio.wav', filtered_data, sampling_rate)

#Create and apply high-pass filter
print("Applying high-pass filter...")
cutoff_frequency = 1000  #Hz
filter_order = 5
filtered_data = highpass_filter(data, cutoff_frequency, sampling_rate)

# Saving filtered audio
print("Saving audio file...")
sf.write('high_filtered_audio.wav', filtered_data, sampling_rate)

#Create and apply band-pass filter
print("Applying band-pass filter...")
low_cutoff_frequency = 1000  #Hz
high_cutoff_frequency = 100000  #Hz
filter_order = 5
filtered_data = bandpass_filter(data, low_cutoff_frequency, high_cutoff_frequency, sampling_rate)

# Saving filtered audio
print("Saving audio file...")
sf.write('band_filtered_audio.wav', filtered_data, sampling_rate)

#Create sample data
print("Creating sample data...")
time = np.linspace(0, 1, 1000)  #Time vector
data = np.sin(2*np.pi*150*time) + np.random.rand(1000)  #Create example sine wave

#Plot the graph of the signals
print("Plotting graph of the signals...")
plt.figure(figsize=(10, 6))
plt.plot(time, data, label='Original Signal')
plt.plot(time, filtered_data, label='Filtered Signal')
plt.xlabel('Time in seconds')
plt.ylabel('Amplitude')
plt.title('Low-Pass Filter')
plt.legend()
plt.grid(True)
plt.show()



