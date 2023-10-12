def convolv(signal, kernel):
    # Panjang sinyal dan kernel
    signal_len = len(signal)
    kernel_len = len(kernel)
    
    # Panjang sinyal hasil konvolusi
    result_len = signal_len + kernel_len - 1
    
    # Inisialisasi hasil konvolusi dengan nilai nol
    result = [0] * result_len
    
    # Flip kernel
    kernel = list(reversed(kernel))
    
    # Lakukan konvolusi
    for i in range(result_len):
        for j in range(kernel_len):
            if i - j >= 0 and i - j < signal_len:
                result[i] += signal[i - j] * kernel[j]
    
    return result

# Contoh penggunaan
signal = [1, 1, 3, 4, 3]
kernel = [3, 1, 3]

result = convolv(signal, kernel)
print("Hasil Konvolusi:", result)

