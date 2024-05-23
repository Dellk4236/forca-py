import random # Importa a biblioteca "random" para escolher aleatóriamente uma palavra

print("Bem-vindo ao jogo da forca! Criado por Dellk.")

import random

def escolher_palavra(): # Escolha de palavras
    escolhas = [
        "python", "forca", "jogo", "jogos", "jogo da forca", "programacao", "computador",
        "tecnologia", "internet", "inteligencia", "artificial", "algoritmo", "dados", 
        "ciencia", "rede", "software", "hardware", "criptografia", "seguranca", "sistema", 
        "operacional", "linguagem", "codigo", "interface", "usuario", "memoria", "processador", 
        "robótica", "sensores", "autômato", "inteligente", "aprendizado", "maquina", 
        "rede neural", "big data", "análise", "dados", "modelagem", "simulação", "realidade", 
        "virtual", "aumentada", "visão", "computacional", "automação", "industrial", "projeto", 
        "inovação", "tecnológica", "pesquisa", "desenvolvimento"
    ]
    return random.choice(escolhas)


def mostrar_progresso(palavra, letras_adivinhadas): # Exibição do progresso atual do jogo
    progresso = ""
    for letra in palavra:
        if letra in letras_adivinhadas or letra == " ":
            progresso += letra + " "
        else:
            progresso += "_ "
    return progresso.strip()

def verificar_vitoria(palavra, letras_adivinhadas): # Verificação de vitória
    for letra in palavra:
        if letra != " " and letra not in letras_adivinhadas:
            return False
    return True

def dificuldade(): # Seleção de dificuldade
    nivel = input("Escolha o nível de dificuldade: fácil [1], médio [2], difícil [3], impossível [4] ").lower()
    if nivel == "1":
        return 10
    elif nivel == "4236": # Modo debug, útil para testar alterações no código do jogo
        print(f"A palavra selecionada é {palavra}, verifique durante a execução do jogo...")
        return float('inf')
    elif nivel == "2":
        return 6
    elif nivel ==  "3":
        return 4
    elif nivel ==  "4":
        print("Você escolheu o modo impossível, se errar uma letra, acabou!")
        return 1
    else:
        print("Nível de dificuldade inválido. Escolha entre fácil [1], médio [2], difícil [3] e impossível [4]") # caso o jogador não digite nenhum nível de dificuldade válido, enviar a mensagem de dificuldade inválida
        return dificuldade()

palavra = escolher_palavra() # definição da variável "palavra"
letras_adivinhadas = [] # definição da variável "letras_adivinhadas"
tentativas_erradas = 0 # definição da variável "tentativas_erradas"
limite_tentativas = dificuldade() # definição da variável "limite_tentativas", integrada a dificuldade do jogo

while True: # Loop inicial do jogo
        print(f"Tentativas restantes: {limite_tentativas - tentativas_erradas}")
        print(f"Letras adivinhadas: {', '.join(letras_adivinhadas)}")
        print(mostrar_progresso(palavra, letras_adivinhadas))

        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha(): # verificação se o jogador está digitando apenas 1 letra
            print("Por favor, digite apenas uma letra.")
            continue

        if letra in letras_adivinhadas: # verifica se a letra digitada pelo jogador já foi usada
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_adivinhadas.append(letra)

        if letra in palavra: # verifica se a letra esta na palabra secreta
            print(f"A letra '{letra}' está na palavra.")
        else:
            print(f"A letra '{letra}' não está na palavra.") # caso a letra não esteja na palavra secreta, adiciona 1 tentativa errada
            tentativas_erradas += 1

        if verificar_vitoria(palavra, letras_adivinhadas): # se a condição "verificar_vitoria" for atingida, enviar a mensagem de parabéns
            print(f"Parabéns! Você adivinhou a palavra '{palavra}'!")
            break

        if tentativas_erradas >= limite_tentativas: # se a variável "tentativas_erradas" possuir valor maior que a variável "limite_tentativas" (integrada a dificuldade), enviar a mensagem de derrota
            print(f"Você perdeu! A palavra era '{palavra}'.")
            break