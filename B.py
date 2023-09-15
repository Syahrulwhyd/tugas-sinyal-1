import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)
data = np.random.rand(90)  # Data acak dengan 90 angka

# Fungsi untuk melakukan filtering dengan filter rata-rata
def average_filter(data, window_size):
    filtered_data = np.convolve(data, np.ones(window_size)/window_size, mode='valid')
    return filtered_data

# Ukuran jendela filter rata-rata
window_size = 9

# Melakukan filtering pada data
filtered_data = average_filter(data, window_size)

# Plot data asli dan data yang telah difilter
plt.figure(figsize=(10, 6))
plt.plot(data, label='Data Asli', color='b')
plt.plot(filtered_data, label=f'Data Filtered (window_size={window_size})', color='r')
plt.legend()
plt.xlabel('Index Data')
plt.ylabel('Nilai Data')
plt.title('Filtering Data Menggunakan NumPy dan Matplotlib')
plt.grid(True)
plt.show()
