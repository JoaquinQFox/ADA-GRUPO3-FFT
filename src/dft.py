import math

# Implementación de algoritmo de transformada de fourier discreta (DFT)
def dft(signals : list[complex]):
    N = len(signals)
    X = [0j] * N

    for k in range(N):
        X[k] = 0j
        for n in range(N):
            angle = -2 * math.pi * k * n / N
            term = signals[n] * (math.cos(angle) + 1j * math.sin(angle))
            X[k] = X[k] + term

    return X

if __name__ == "__main__":
    signal = [math.sin(2 * math.pi * 1 * t / 32) + 0.5 * math.sin(2 * math.pi * 3 * t / 32) for t in range(32)]
    result = dft(signal)
    N = len(result)

    for i, val in enumerate(result):
        print(f"X[{i}] = {val:.4f}")
