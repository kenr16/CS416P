print("Starting dependency imports...")
import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
print("Dependencies successfully imported.")


#Create low-pass filter
print("Creating low-pass filter...")
cutoff_frequency = 200  #Hz
sampling_rate = 2000  #Hz
filter_order = 4
nyquest_frequency = sampling_rate / 2
normal_cutoff = cutoff_frequency / nyquest_frequency
b, a = butter(filter_order, normal_cutoff, btype='lowpass') #'highpass' is also possible here

#Create sample data
print("Creating sample data...")
time = np.linspace(0, 1, 1000)  #Time vector
data = np.sin(2*np.pi*150*time) + np.random.rand(1000)  #Create example sine wave
filtered_data = filtfilt(b, a, data) #Filter applied

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