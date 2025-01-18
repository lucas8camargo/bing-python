from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def realizar_pesquisas(termos, repeticoes, perfil_path):

    # Configuração do Edge WebDriver com o perfil do usuário
    options = webdriver.EdgeOptions()
    options.add_argument(f"user-data-dir={perfil_path}")  # Caminho para o perfil do usuário
    options.add_argument("--start-maximized")  # Maximizar janela
    driver = webdriver.Edge(options=options)

    try:
        # Esse loop não é útil para o Reward porque ele só vai considerar a primeira vez que o termo é pesquisado, mas pode ser util em usos semelhantes
        for i in range(repeticoes): 

            print(f"Execução {i+1} de {repeticoes}:")

            # Aqui será realizado o loop de pesquisas do termo
            for termo in termos:

                print(f"Pesquisando por: {termo}")

                # Abre a página inicial do Bing
                driver.get("https://www.bing.com")

                # Encontra a barra de pesquisa, limpa o campo, digita o termo e seleciona a tecla Enter para pesquisar
                barra_pesquisa = driver.find_element(By.NAME, "q")
                barra_pesquisa.clear()
                barra_pesquisa.send_keys(termo)
                barra_pesquisa.send_keys(Keys.RETURN)

                # Aguardar alguns segundos para contabilizar os pontos
                time.sleep(5)
    finally:
        # Fecha o navegador
        driver.quit()

# Lista com os termos para pesquisa
# A quntidade de termos pode variar dependendo dos pontos ganhos para cada pesquisa
termos_para_pesquisa = [
    # Fundamentos
    "sintaxe python", "tipos de dados python", "estruturas de controle python", "funções python", "módulos python",
    "pacotes python", "orientação a objetos python", "herança python", "polimorfismo python", "exceções python",

    # Estruturas de Dados
    "listas python", "tuplas python", "dicionários python", "conjuntos python", "pilhas python", "filas python",

    # Bibliotecas Essenciais
    "pandas python", "numpy python", "matplotlib python", "seaborn python", "scikit-learn python",

    # Ciência de Dados e Machine Learning
    "regressão linear python", "árvore de decisão python", "random forest python", "clustering python", "neural networks python",
    "deep learning python", "tensorflow python", "pytorch python", "keras python", "nlp python",

    # Desenvolvimento Web
    "flask python", "django python", "rest api python", "web scraping python", "beautifulsoup python",

    # Outros Tópicos
    "testes unitários python", "depuração python", "versionamento de código python", "git python", "docker python",
    "programação concorrente python", "programação assíncrona python", "design patterns python", "algoritmos python", "estrutura de dados python"
]

# Define a quantidade de vezes que o loop de pesquisa será executado
quantidade_de_pesquisas = 1

# Utiliza o perfil com a conta Microsoft logada para receber os pontos
# Atualize este caminho para o correto para cada pessoa
caminho_perfil = r"C:\Users\Lucas\AppData\Local\Microsoft\Edge\User Data\Default"

# Execução da função
realizar_pesquisas(termos_para_pesquisa, quantidade_de_pesquisas, caminho_perfil)