import numpy as np
import soundfile as sf

data = np.sin(np.arange(44100) / 100 * 2 * np.pi)

sf.write('middle_c.wav', data, 44100)