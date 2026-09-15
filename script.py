import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio, display
from scipy.io import wavfile

RATE = 44_100
LA = 440
DO = 523.25

T = np.linspace(0,1,RATE)
son = np.sin(2*np.pi*LA*T)

plt.plot(T[:(44100//20)],son[:(44100//20)])
#plt.show()

audio = Audio(son, rate=RATE)
display(audio)