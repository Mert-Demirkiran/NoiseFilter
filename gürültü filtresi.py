import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

def butter_lowpass_filter(data, cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return lfilter(b, a, data)

fs = 500.0      
t = np.linspace(0, 1, int(fs), endpoint=False)
clean_signal = np.sin(2 * np.pi * 5 * t)  # 2 * pi * f * t
noise = 0.5 * np.random.normal(size=t.shape) 
dirty_signal = clean_signal + noise

cutoff = 10.0   
filtered_signal = butter_lowpass_filter(dirty_signal, cutoff, fs)

plt.figure(figsize=(10, 6))
plt.plot(t, dirty_signal, label='Gürültülü Sinyal', alpha=0.5)
plt.plot(t, filtered_signal, label='Filtrelenmiş (Temiz) Sinyal', linewidth=2)
plt.legend()
plt.title("Dijital Low-Pass Filtre Uygulaması")
plt.show()
