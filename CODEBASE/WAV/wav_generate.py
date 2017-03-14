import numpy as np
import wave, struct, math
import sys
from scipy.io.wavfile import write

sampleRate = 44100.0 # hertz
duration = 3.0       # seconds
frequency = 440.0    # hertz

script,filename = sys.argv

words = open(filename).read().split() # splits the random numbers in the file to list
for i in range(0,len(words)):
	words[i] = int(words[i]) * 999999

words = words * 6
words_array = np.array(words)
scaled = np.int16(words_array/np.max(np.abs(words_array)) * 32767)
write('test.wav', 44100, words_array)
wavef = wave.open('test.wav','w')
wavef.setnchannels(1)
wavef.setsampwidth(2)
wavef.setframerate(sampleRate)

for i in range(int(duration * sampleRate)):
    value = int(32767.0*math.cos(frequency*math.pi*float(i)/float(sampleRate)))
    data = struct.pack('<h', value)
    wavef.writeframesraw( data )
