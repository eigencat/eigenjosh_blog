# https://stackoverflow.com/questions/8299303/generating-sine-wave-sound-in-python

import numpy as np
import soundfile as sf

volume = 0.4    # range(0.0, 1.0)
fs = 44100      # sampling frequency in Hz
length = 3      # length in seconds

def generateSound(freq):
    data = (np.sin(2*np.pi*np.arange(fs*length)*freq/fs)).astype(np.float32)
    sf.write(str(freq)+'.wav',data,fs)

generateSound(261)
generateSound(523)