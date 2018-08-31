import math
import random
from scipy.io import wavfile
import librosa

def rms(a):
    total = 0
    for n in range(1,len(a)):
        total += a[n]*a[n]

    total = math.sqrt(total/len(a))
    
    return total

def audio_synthesize(path_speech, path_noise, snr):

    fs, speech = wavfile.read(path_speech)



    speech,fs = librosa.load(path_speech,sr=None)
    noise,fs = librosa.load(path_noise,sr=None)

    noise_pre_scale = (1-snr/50)
    if (snr>0):
        noise = noise*noise_pre_scale

    len_speech = len(speech)
    len_noise = len(noise)

    start_point_noise = random.randint(0,len_noise-len_speech)
    end_point_noise = start_point_noise + len_speech - 1
    noise_current = noise[start_point_noise : end_point_noise + 1]
 #   len_noise_current = len(noise_current)
    rms_noise = rms(noise_current)
    rms_speech = rms(speech)
    db_noise = 20*math.log10(rms_noise)
    db_speech = 20*math.log10(rms_speech)
    current_snr = db_speech - db_noise
    db_adjust = snr - current_snr
    scale_adjust = math.pow(10,db_adjust/20)
    
    output = noise_current + speech*scale_adjust

    wavfile.write("test.wav", fs, output)

    #print (rms_noise)

    return output, fs
