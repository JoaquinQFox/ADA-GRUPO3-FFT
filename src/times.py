# Medición de tiempos de ejecución con diferentes tamaños de entrada

# ----------------------------------------------------------------

import time
import math
from dft import dft
from fft import fft

# ----------------- Función de Generar Entradas ------------------

# función de prueba
def generar_signal (N):
    return [math.sin(2 * math.pi * 3 + t / N) for t in range(N)]

# --------------------- Tiempos de Ejecución ---------------------

# Medición de tiempos
def medir_tiempos():
    size        = [32, 64, 128, 256, 512, 1024, 2048, 4096]
    tiempos_dft = []
    tiempos_fft = []

    for N in size:
        signal = generar_signal(N)

        # Tiempos de DFT
        inicio     = time.perf_counter()
        dft(signal)
        fin        = time.perf_counter()
        tiempo_dft = fin - inicio

        tiempos_dft.append(tiempo_dft)
        
        # Tiempos de FFT
        inicio     = time.perf_counter()
        fft(signal)
        fin        = time.perf_counter()
        tiempo_fft = fin - inicio

        tiempos_fft.append(tiempo_fft)

    return size, tiempos_dft, tiempos_fft

# ---------------------------- Main ------------------------------
if __name__ == "__main__":

    size, tiempos_dft, tiempos_fft = medir_tiempos()

    for i in range(len(size)):
        
        # Mostrar
        print(f"N = {size[i]:4d} | DFT = {tiempos_dft[i]:.6f}s | FFT = {tiempos_fft[i]:.6f}s")