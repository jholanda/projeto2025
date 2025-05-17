import numpy as np
import matplotlib.pyplot as plt
import argparse

# Configuração do parser de argumentos
parser = argparse.ArgumentParser(description="Ajuste de mínimos quadrados")
parser.add_argument("data_file", type=str, help="Nome do arquivo com os dados (x e y)")
parser.add_argument("params_file", type=str, help="Nome do arquivo com os valores de a e b")

# Parsing dos argumentos
args = parser.parse_args()

# Leitura dos parâmetros (a e b)
try:
    params = np.loadtxt(args.params_file, dtype=float)
    if params.size != 2:
        raise ValueError("O arquivo de parâmetros deve conter exatamente dois valores (a e b) em uma linha.")
    a, b = params  # Obtém os valores de a e b

    # Leitura dos dados de entrada
    data = np.loadtxt(args.data_file, dtype=float)
    if data.ndim == 1:
        data = data.reshape(-1, 2)
    
    x = data[:, 0]
    y = data[:, 1]

    # Reta ajustada
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = a + b * x_fit

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'o', label='Dados originais')
    plt.plot(x_fit, y_fit, '-', label=f'Reta ajustada: y = {a:.2f} + {b:.2f}x')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Ajuste de mínimos quadrados')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado -> {e.filename}")
except ValueError as e:
    print(f"Erro: {e}")

