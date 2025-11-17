import matplotlib.pyplot as plt
import numpy as np

from times import medir_tiempos

# ================================================================
# Función para crear los gráficos
# ================================================================

def crear_graficos_comparativos(size, tiempos_dft, tiempos_fft):
    """
    Genera y guarda los 3 gráficos clave para el análisis de rendimiento.
    """
    
    # --- Gráfico 1: Escala Lineal ---
    plt.figure(figsize=(10, 7))
    plt.plot(size, tiempos_dft, marker='o', linestyle='--', label='DFT ($O(N^2)$)')
    plt.plot(size, tiempos_fft, marker='x', linestyle='-', label='FFT ($O(N \log N)$)')
    plt.xlabel('Tamaño de la Señal (N)')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.title('Comparativa de Rendimiento (Escala Lineal)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig('comparativa_rendimiento_lineal.png')
    print("Gráfico 'comparativa_rendimiento_lineal.png' generado.")

    # --- Gráfico 2: Escala Log-Log ---
    plt.figure(figsize=(10, 7))
    plt.plot(size, tiempos_dft, marker='o', linestyle='--', label='DFT ($O(N^2)$)')
    plt.plot(size, tiempos_fft, marker='x', linestyle='-', label='FFT ($O(N \log N)$)')
    plt.xlabel('Tamaño de la Señal (N) - Escala Log')
    plt.ylabel('Tiempo de Ejecución (segundos) - Escala Log')
    plt.title('Comparativa de Rendimiento (Escala Log-Log)')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig('comparativa_rendimiento_loglog.png')
    print("Gráfico 'comparativa_rendimiento_loglog.png' generado.")
    
    # --- Gráfico 3: Factor de Aceleración (Speedup) ---
    # Evitar división por cero si el tiempo de FFT es muy pequeño
    speedup = [td / tf for td, tf in zip(tiempos_dft, tiempos_fft) if tf > 0]
    
    plt.figure(figsize=(10, 7))
    plt.plot(size, speedup, marker='s', linestyle='-', color='green', label='Factor de Aceleración (Tiempo DFT / Tiempo FFT)')
    plt.xlabel('Tamaño de la Señal (N) - Escala Log')
    plt.ylabel('Factor de Aceleración (Veces más rápida)')
    plt.title('Factor de Aceleración de FFT sobre DFT')
    plt.xscale('log') 
    plt.yscale('log') 
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig('factor_aceleracion.png')
    print("Gráfico 'factor_aceleracion.png' generado.")

# ---------------------------- Main ------------------------------
if __name__ == "__main__":
    
    # 1. Medir tiempos 
    print("Ejecutando grafico.py...")
    size, tiempos_dft, tiempos_fft = medir_tiempos()
    
    # 2. Crear gráficos 
    crear_graficos_comparativos(size, tiempos_dft, tiempos_fft)
    
    print("\nProceso P6 (grafico.py) completado. 3 gráficos generados.")