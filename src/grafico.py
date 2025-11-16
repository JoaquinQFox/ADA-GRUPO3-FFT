# Graficos comparativos de tiempos de ejecución de DFT y FFT

# ----------------------------------------------------------------

import time
import math
from dft import dft
from fft import fft
# from generar_signal import times

# --------------------- Tiempos de Ejecución ---------------------

# función de prueba
def generar_signal (N):
    return [math.sin(2 * math.pi * 3 + t / N) for t in range(N)]

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
        
        # Mostrar de prueba
        print(f"N = {N:4d} | DFT = {tiempo_dft:.6f}s")

    return size, tiempos_dft, tiempos_fft

# Main
if __name__ == "__main__":
    medir_tiempos()

# ----------------------------------------------------------------




