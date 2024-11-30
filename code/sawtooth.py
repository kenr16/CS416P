print("Starting dependency imports...")
import numpy as np
from scipy import signal
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
print("Dependencies successfully imported.")

# Define parameters
frequency = 440  # Hz
amplitude = 1024   # Maximum possible 16-bit aplitude value: 32767
duration = 1  # second
sampling_rate = 48000  # Hz

# Generate the repeating wave patterns
print("Generating three different repeating wave patterns...")
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False) # Generate time values
sine_wave = amplitude * np.sin(2 * np.pi * frequency * t) # Generate sine wave
sawtooth_wave = amplitude * signal.sawtooth(2 * np.pi * frequency * t) # Generate sawtooth wave
square_wave = amplitude * signal.square(2 * np.pi * frequency * t) # Generate square wave

# Plot the original and clipped sine waves
print("Plotting both sine wave on graph...")
plt.plot(t, sine_wave, label='Original Sine Wave')
plt.plot(t, sawtooth_wave, label='Sawtooth Sine Wave')
plt.plot(t, square_wave, label='Square Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
print("Sine waves plotted.")

# Export the sine waves to sine.wav
#print("Exporting sound files to 'sound/sine.wav'")
#sf.write('sound/sine.wav', sine_wave1, sampling_rate)
#print("Done")

# Define the envelope effect function
#print("Defining the envelope function...")
#def envelope(duration, attack_time, decay_time, release_time):
#    attack = np.linspace(0, 1, int(attack_time * sampling_rate)) # Time for the volume to rise initially from zero
#    decay = np.linspace(1, 0.8 , int(decay_time * sampling_rate)) # Decay is the decline after the initial volume spike.
#    sustain = np.linspace(0.8, 0.8, int((duration - attack_time  - decay_time - release_time) * sampling_rate)) # Time theat the note stays the same volume
#    release = np.linspace(0.8, 0, int(release_time * sampling_rate)) # Time during which the volume declines to zero
#    return np.concatenate([attack, decay, sustain, release])

# Create an envelope
#print("Creating envelope to apply...")
#envelope = envelope(duration=1, attack_time=0.1, decay_time=0.1, release_time=0.5)

#sine_wave = sine_wave * envelope[:len(sine_wave)]
#sawtooth_wave = sawtooth_wave * envelope[:len(sawtooth_wave)]
#square_wave = square_wave * envelope[:len(square_wave)]

# Playback the audio on all three sound files.
print("Playing the audio for all three soundwave types...")
sd.play(sine_wave)
sd.wait()  # Wait until playback is finished before playing the next
sd.play(sawtooth_wave)
sd.wait()
sd.play(square_wave)
sd.wait()