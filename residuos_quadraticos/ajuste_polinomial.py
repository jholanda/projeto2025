import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

# Configuração do parser de argumentos
parser = argparse.ArgumentParser(description="Ajuste de polinômio por mínimos quadrados")
parser.add_argument("data_file", type=str, help="Nome do arquivo com os dados (x e y)")
parser.add_argument("params_file", type=str, help="Nome do arquivo com os coeficientes do polinômio")

# Parsing dos argumentos
args = parser.parse_args()

# Leitura dos parâmetros (coeficientes do polinômio)
try:
    # Carregar os coeficientes do arquivo
    coeficientes = np.loadtxt(args.params_file, dtype=float)
    
    # Determinando o grau do polinômio pelo número de coeficientes
    grau = len(coeficientes) - 1
    
    if grau < 1 or grau > 10:
        raise ValueError(f"O grau do polinômio é {grau}, mas deve estar entre 1 e 10.")
    
    print(f"Ajustando polinômio de grau {grau}")
    print(f"Coeficientes carregados: {coeficientes}")

    # Leitura dos dados de entrada
    data = np.loadtxt(args.data_file, dtype=float)
    if data.ndim == 1:
        data = data.reshape(-1, 2)
    
    x = data[:, 0]
    y = data[:, 1]

    # Valores de x para o plot da curva ajustada
    x_fit = np.linspace(min(x), max(x), 100)
    
    # Calcula os valores de y para o polinômio ajustado
    y_fit = np.zeros_like(x_fit)
    for i, coef in enumerate(coeficientes):
        # Adiciona o termo coef * x^i (onde i é a potência)
        y_fit += coef * x_fit ** i
    
    # Criando a expressão do polinômio para o título do gráfico
    expr = ""
    for i, coef in enumerate(coeficientes):
        if i == 0:
            expr += f"{coef:.2f}"
        elif i == 1:
            expr += f" + {coef:.2f}x"
        else:
            expr += f" + {coef:.2f}x^{i}"
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'o', label='Dados originais')
    plt.plot(x_fit, y_fit, '-', label=f'Polinômio ajustado: y = {expr}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Ajuste polinomial de grau {grau} por mínimos quadrados')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Nome do arquivo de saída
    base_name = os.path.splitext(args.data_file)[0]
    output_file = f"{base_name}_plot_grau{grau}.png"
    
    # Salvar o gráfico como imagem (opcional)
    plt.savefig(output_file)
    print(f"Gráfico salvo como {output_file}")

except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado -> {e.filename}")
except ValueError as e:
    print(f"Erro: {e}")
