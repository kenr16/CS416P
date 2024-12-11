# CS416P
A repo for the work created for CS416P

## Final Project
The final project for this course is contained in the file compression.py.  This is a project to experiment with various different lossless file compression techniques.  The first form of lossless file compression is Run Length Encoding, or RLE.  This is where sequences of repeating characters are replaced with a single character and a number to represent how many times in a row that character repeats.  For example, "AAABBBBAACCCCCC" would be replaced with "A3B4A2C6", which shortens the string without losing any data.  A second, modified version of this is is also written here which will do the same to binary code, except with only integers representing how many ones and zeros fall in a row in alternating strings.  The third form of lossless compression used here is called Huffman encoding.  This is where each character found in the code is assigned a binary encoding.  The smallest possible binary encoding is used for the characters that appear in the string most often, and because of the fact that the Huffman tree is constructed from bottom to top, with only the leaves of the tree representing character encodings, there will never be a situation where one chracters binary encoding is confused with another.  This is called prefix encoding, and it means that the Huffman encoding can be decrypted easily without any special markers to separate out different binary encodings.  For this project, I take the random noise generated earlier in the course in whitenoise.py, then run it through the modified Run Length Encoding, as well as the Huffman encoding.  While the length of the original, the RLE and the Huffman encoding are compared at the end, it is something of an apples-to-oranges comparison, as it switches from binary to integer and back to binary format.  This project did not advance to the point where I write the final code to a file, nor did I reach the point where I wrote inverse functions to reverse the encoding, and return the file to its original form.  It was, however, a very interesting exercise, that allowed me to learn how lossless compression algorithms work, and to revisit binary trees that I had learned about in previous courses.  It would be interesting at a later date to revisit this, and further refine the methods used to compress files.  I believe that I could do a more efficient job.

### Clipped.py
The file clipped.py produced two .wav files, the first is a sine wave of a specific amplitude, the second is a clipped sine wave that has been truncated at the same amplitude as the first.

### Fourier.py
The file Fourier.py will create a single sine wave that represents a sound at a specific frequency and compute the Fourier transform of the sine wave, then plot both on a graph beside one another.

### Add.py
The file add.py will produce three different sine waves of different frequencies and amplitudes and add them together into a single composite wave.  From there, it will take the Fourier transform of the combined wav and plot the Fourier transform and the original wave together beside one another.

### Delay.py
The file delay.py will read in an audio file written into the code, the add in three different effects.  The first is the delay effect, where and empty array filled with zeroes will be added to the start of the sound file, thereby delaying the playback of the file.  The second and third effects will be a fade-in and fade-out effect that will modulate the volume allowing the song to fade-in or fade out over a few seconds duration.  All three effects will be saved as separate.wav files in the sound folder once they have been applied.

### Echo.py
The files echo.py will read in a sound file, then apply an echo effect several times over that will attenuate.  It will then save this modified .wav file with the echo effect applied in the sound folder as a separate file.

### Envelope.py
The file envelope.py will apply a volume envelope over a specified duration.  This envelope will have an attack, decay, sustain and release phase.  The program will then read in an audio file and apply the envelope effect to the file and save the modified envelope effect as a separate .wav file.

### Filters.py
The file filters.py will create a low-pass filter, a high-pass filter and a band-pass filter and finally a sound energy function which calculates the sound energy of a clip of a sound using the fourier transform, the magnitude spectrum and finally the power spectrum of the sound file.  From there, the program will read in an audio file, then apply each of the three filters, and save the results as individual sound files.  From there, it will calculate the sound energy of all three filters, and finally equalize the three bands by adjusting the amplitude, and add the three bands back together again into a single equalized sound file, then save the result.

### Popgen.py
The file popgen.py was modified to change the shape of the waveforms from traditional sine waves to sawtooth waves, then an envelope was created over the duration of each note, which will modulate the volume such that each note has an attack, decay, sustain and release phase.

### Readin.py
The file readin.py simply exists and an exercise in reading in a wavfile from an external source.  In this case, it will read in both sine.wav and clipped.wav, then plot both of these sine waves on a graph next to each other for comparison purposes.

### Sawtooth.py
The file sawtooth.py will create three differet sounds with the same frequency, amplitude and duration as one another, however, the shape of the sound waves will be different.  The first will be a traditional sine wave.  The second will be a sawtooth wave.  The third will be a square wave.  All three of these will be plotted on a graph and played back to the user.

### Whitenoise
The file whitenoise.py will simply generate one second of whitenoise by creating a sound file using random values scattered throughout the duration of the noise.  It will then save this whitenoise as a sound file in the sound folder.
