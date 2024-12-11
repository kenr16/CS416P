# CS416P
A repo for the work created for CS416P

# Clipped.py
The file clipped.py produced two .wav files, the first is a sine wave of a specific amplitude, the second is a clipped sine wave that has been truncated at the same amplitude as the first.

# Fourier.py
The file Fourier.py will create a single sine wave that represents a sound at a specific frequency and compute the Fourier transform of the sine wave, then plot both on a graph beside one another.

# Add.py
The file add.py will produce three different sine waves of different frequencies and amplitudes and add them together into a single composite wave.  From there, it will take the Fourier transform of the combined wav and plot the Fourier transform and the original wave together beside one another.

# Delay.py
The file delay.py will read in an audio file written into the code, the add in three different effects.  The first is the delay effect, where and empty array filled with zeroes will be added to the start of the sound file, thereby delaying the playback of the file.  The second and third effects will be a fade-in and fade-out effect that will modulate the volume allowing the song to fade-in or fade out over a few seconds duration.  All three effects will be saved as separate.wav files in the sound folder once they have been applied.

# Echo.py
The files echo.py will read in a sound file, then apply an echo effect several times over that will attenuate.  It will then save this modified .wav file with the echo effect applied in the sound folder as a separate file.

# Envelope.py
The file envelope.py will apply a volume envelope over a specified duration.  This envelope will have an attack, decay, sustain and release phase.  The program will then read in an audio file and apply the envelope effect to the file and save the modified envelope effect as a separate .wav file.

# Filters.py
The file filters.py will create a low-pass filter, a high-pass filter and a band-pass filter and finally a sound energy function which calculates the sound energy of a clip of a sound using the fourier transform, the magnitude spectrum and finally the power spectrum of the sound file.  From there, the program will read in an audio file, then apply each of the three filters, and save the results as individual sound files.  From there, it will calculate the sound energy of all three filters, and finally equalize the three bands by adjusting the amplitude, and add the three bands back together again into a single equalized sound file, then save the result.

# Popgen.py
The file popgen.py was modified to change the shape of the waveforms from traditional sine waves to sawtooth waves, then an envelope was created over the duration of each note, which will modulate the volume such that each note has an attack, decay, sustain and release phase.

# Readin.py
The file readin.py simply exists and an exercise in reading in a wavfile from an external source.  In this case, it will read in both sine.wav and clipped.wav, then plot both of these sine waves on a graph next to each other for comparison purposes.

# Sawtooth.py
The file sawtooth.py will create three differet sounds with the same frequency, amplitude and duration as one another, however, the shape of the sound waves will be different.  The first will be a traditional sine wave.  The second will be a sawtooth wave.  The third will be a square wave.  All three of these will be plotted on a graph and played back to the user.

# Whitenoise
The file whitenoise.py will simply generate one second of whitenoise by creating a sound file using random values scattered throughout the duration of the noise.  It will then save this whitenoise as a sound file in the sound folder.
