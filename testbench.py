from audio_synthesize import audio_synthesize

path_speech = "BAC009S0002W0124.wav"
path_noise = "truck_idle.wav"
snr = 0

output, fs = audio_synthesize(path_speech, path_noise, snr)

#print (fs)



