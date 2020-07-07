import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from playsound import playsound


fs = 44100
second = 5
FILE_NAME = 'REC_FILE'
FILE_PATH = 'C:\\Users\\****\\Desktop\\'

print("recording")


#Record audio data into a NumPy array
#sounddevice.rec(frames=None, samplerate=None, channels=None, dtype=None, mapping=None, blocking=False, **kwargs)
record_voice = sd.rec( int(second*fs), samplerate=fs, channels=2 )



# save as type: *.wav
sd.wait()
write(FILE_NAME+'.wav', fs, record_voice)


# save as type: *.npy
np.save(FILE_PATH+FILE_NAME+'.npy', record_voice)


# plot
record_voice =  np.transpose(record_voice)
t = np.arange(fs*second)

fig, ch = plt.subplots(2,1, sharex=True, sharey=True)

for i in range(len( record_voice )):
    ch[i].plot(t, record_voice[i])
    ch[i].set_xlabel('[second]')
    ch[i].set_title(r'$CHANNEL_{}$'.format(i))
    
fig.tight_layout()
plt.setp(ch, xticks=np.arange(second+1)*44100, xticklabels=np.arange(second+1))
plt.show()



# playrec
play_voice = np.load(FILE_PATH+FILE_NAME)
sd.playrec( play_voice, samplerate = fs, channels=2 )


# play *.wav file
wav_file_path = FILE_PATH + FILE_NAME
playsound(wav_file_path + '.wav')
