import math
import cmath

# fft de coleyu tukey
def fft(signals: list[complex]):
    N = len(signals)
    if N <= 1:
        return signals
    
    # fft de las muestras pares e impares
    par = fft(signals[0::2])
    impar = fft(signals[1::2])
    
    # calcular los factores twiddle
    T = [cmath.exp(-2j * math.pi * k / N) * impar[k] for k in range(N // 2)]
    
    #combinar los resultados
    return [par[k] + T[k] for k in range(N // 2)] + \
           [par[k] - T[k] for k in range(N // 2)]

if __name__ == "__main__":
    # Señal de prueba: suma de dos curvas  senoidales
    signal = [math.sin(2*math.pi*1*t/32)+0.5*math.sin(2*math.pi*3*t/32) for t in range(32)]
    
    result = fft(signal)
    
    for i, val in enumerate(result):
        print(f"X[{i}] = {val.real:.4f} + {val.imag:.4f}j")
