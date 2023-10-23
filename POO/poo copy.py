import matplotlib.pyplot as plt

class SistemaDeGraficos:
    def __init__(self, dados):
        self.dados = dados

    def criar_grafico_barras(self, x, y, titulo):
        plt.figure(figsize=(8, 6))
        plt.bar(x, y)
        plt.title(titulo)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.show()

    def criar_grafico_dispersao(self, x, y, titulo):
        plt.figure(figsize=(8, 6))
        plt.scatter(x, y)
        plt.title(titulo)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.show()

# Exemplo de uso
dados = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 8, 15, 7, 12]
}

sistema = SistemaDeGraficos(dados)

sistema.criar_grafico_barras(dados['x'], dados['y'], 'Gráfico de Barras')
sistema.criar_grafico_dispersao(dados['x'], dados['y'], 'Gráfico de Dispersão')
