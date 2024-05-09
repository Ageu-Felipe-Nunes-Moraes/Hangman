


from random import choice # Módulo para randomizar
import tkinter as tk # Módulo gráfico
from tqdm import tqdm # Módulo para barra de progresso
import time # Módulo para tempo
import easygui # Módulo para criar menu 
import os # Módulo que reinicia o programa do zero
import sys # Módulo que reincia o programa do zero


# Função que identifica o evento de clique do usuário
def tecla_pressionada(event):

    # Busca a letra que o usuário pressionou, no alfabeto
    if event.char.isalpha():
        
        # Verifica a letra que o usuário pressionou
        verifica_cliques = event.char.upper()
        
        # Verifica a letra pressionada pelo usuário e ver se ela pertence a lista das letras da palavra aleatória
        if verifica_cliques in set(letras_separadas):
            
            # Se a condicional de cima for verdade, ela acrescenta a letra aleatória correspondente à lista vazia nomeada de "depositoLetrasCertas" 
            deposito_letras_certas.append(verifica_cliques)


        # Encontra os números e as posições de uma letra na palavra selecionada sem se importa se são maiúsculas ou minúsculas
        posicoes = [numero_letras+1 for numero_letras, letra in enumerate(palavra) if letra.upper() == event.char or (numero_letras == 0 and letra.upper() == event.char.upper()) or letra.lower() == event.char or (numero_letras == 0 and letra.lower() == event.char.lower())] 
        
        # Mensagem que aparece da letra e da posição na tela
        mensagem_posicao.config(text=f"Posições da letra {event.char.upper()}: {posicoes}")
        

        # Verifica a letra que o usuário pressionou
        verifica_cliques = event.char.upper()

        # Verifica se a letra já foi pressionada antes
        if verifica_cliques in deposito_letras_repetidas: 
            
            
            # Cria uma mensagem
            letras_repetidas = tk.Label(tela, text=(f"A letra {verifica_cliques} já foi utilizada!!!"), bg="white", fg="brown") 

            # Apliaca as coordenadas da mensagem
            letras_repetidas.place(x = 900, y = 250)

            # Formata a mensagem
            letras_repetidas.config(font=("Times New Roman", 17))


        # Executará se a condicional de cima não fôr satisfeita    
        else:
            
            # verisifica se a letra que o usuário pressionou não pertence a palavra e nem as posições dela
            if verifica_cliques not in palavra_sorteada.upper() and not posicoes: 
                    
                # Pega a letra pressionada e manda para uma lista vazia
                deposito_letras_erradas.append(verifica_cliques)
                    
                # Mostra o texto antecedente às letras erradas
                letras_erradas = tk.Label(tela, text="Letras Erradas: ", bg="white")
                    
                # Mostra as coordenadas
                letras_erradas.place(x = 620, y = 550)

                # Formata as letras
                letras_erradas.config(font=("Times New Roman", 17))

                
            # Loop que define o índice da letra mais a variável qualquer
            for numero_loop_erro, nao_letra in enumerate(deposito_letras_erradas):

                # Apenas garante que não haja erro de indexação
                if numero_loop_erro < len(lista_vazia_erros):
                            
                    # Ele atribui esse loop ao loop de texto vazio que aparece na tela, colocando as letras erradas uma por vez de acordo com a necessidade
                    lista_vazia_erros[numero_loop_erro]['text'] = nao_letra
                            
                    # Verifica os erros
                    
                    verificar_erros()

            
            # Se a letra não tiver na palavra aleátoria, a condicional é executada
            if verifica_cliques not in letras_palavra:
                    
                # Acrescenta a letra pressionada pelo usuário na lista vazia
                letras_palavra.append(verifica_cliques)

                # Chama a função que verifica a vitória
                verifica_vitoria()

                # Adiciona a letra à lista de letras pressionadas que é o "depositoLetrasCertas"
                deposito_letras_repetidas.append(verifica_cliques)
        

        # Verifica se a letra que o usuário pressionou, pertence a palavra randômica
        if event.char.upper() in palavra_sorteada.upper() and posicoes == [numero_posicao+1 for numero_posicao in range(len(palavra_sorteada)) if palavra_sorteada[numero_posicao].upper() == event.char.upper()]: 
            
            # Letra pressionada que será exibida nas posições especificadas
            verifica_cliques = event.char.upper() 
        

            # Estrutura de repetição que ira definir as posições das letras
            for posicao in posicoes:
                
                # Modifica o espaço vazio onde se encontra a letra, pela letra selecionada pelo usuário
                lista_vazia[posicao-1].config(text=verifica_cliques)             
    

    # Executará se a condicional de cima não fôr satisfeita 
    else:
        
        #Mensagem que aparece se a tecla pressionada não for uma letra
        mensagem_posicao.config(text="A tecla pressionada não é uma letra.") 


# Função para fechar programa usando a tecla 'Esc'
def sair_janela(event): 
    # Comando que fecha programa
    tela.destroy()

# Função para reiniciar o jogo utilizando módulos
def reiniciar(event=None):
    python = sys.executable
    os.execl(python, python, *sys.argv)


# Função para criar o botão de reiniciar
def criar_botao_reiniciar():
    
    # Cria botão de Reiniciar
    botao_reiniciar = tk.Button(tela, text="Reiniciar", command=lambda:[reiniciar()], bg = "brown", fg = "White")

    # Aplica as coordenadas do botão
    botao_reiniciar.place(x = 645, y = 650)


# Função que mostra a palavra que tinha que ser, na tela
def mostrar_palavra_correta():

    # Cria a mensagem
    palavra_certa = tk.Label(tela, text=(f"A palavra era '{palavra_sorteada.upper()}'!!!"), bg="white", fg="blue", font=("Times New Roman", 20))

    # posiciona a imagem
    palavra_certa.place(x = 880, y = 250)


# Função que verifica a vitória
def verifica_vitoria():
    
    
    # Verificar se todas as letras da lista estão presentes na palavra aleatória
    if set(deposito_letras_certas) == set(letras_separadas):
        

        # Cria uma mensagem de vitória
        vitoria = tk.Label(tela, text="PARABÉNS, VOCÊ VENCEU!!!", bg="white", fg="green", font=("Times New Roman", 17))

        # Posiciona a imagem na tela
        vitoria.place(x = 545, y = 50)

        # Chamando função
        criar_botao_reiniciar()

        # Comando que impede a leitura de qual tecla o usuário está pressionando
        tela.unbind("<KeyPress>")


# Função que verifica Erros e monta a forca
def verificar_erros():

    # Número de letras erradas pressionadas pela usuário
    num_erros = len(deposito_letras_erradas)


    # Mostra a cabeça da forca se a pessoa errar 1 vez
    if escolha == "Normal" and num_erros == 1:
        
        # Muda a imagem por outra
        imagem_forca.config(image=endereco_imagem_cabeca)

    # Mostra o corpo da forca se a pessoa errar 2 vezes
    if escolha == "Normal" and num_erros == 2:
        
        # Muda a imagem por outra
        imagem_forca.config(image=endereco_imagem_corpo)

    # Mostra um braço da forca se a pessoa errar 3 vezes
    if escolha == "Normal" and num_erros == 3:
        
        # Muda a imagem por outra
        imagem_forca.config(image=endereco_imagem_braco1)

    # Mostra o outro braço da forca se a pessoa errar 4 vezes
    if escolha == "Normal" and num_erros == 4:
        
        # Muda a imagem por outra
        imagem_forca.config(image=endereco_imagem_braco2)

    # Mostra a perna da forca se a pessoa errar 5 vezes
    if escolha == "Normal" and num_erros == 5:
        
        # Muda a imagem por outra
        imagem_forca.config(image=endereco_imagem_perna1)

    # Mostra a outra perna da forca se a pessoa errar 6 vezes
    if escolha == "Normal" and num_erros == 6:
        
        # Muda a imagem por outra
        imagem_forca.config(image=endereco_imagem_perna2)

        # Chamando função
        mostrar_palavra_correta()

        # Cria uma mensagem de derrota
        derrota = tk.Label(tela, text="VOCÊ PERDEU!!!", bg="white", fg="red", font = ("Times New Roman", 17))
        
        # Posiciona a mensagem
        derrota.place(x = 627, y = 50)

        # Comando que impede a leitura de qual tecla o usuário está pressionando
        tela.unbind("<KeyPress>")

        # Chamando função
        criar_botao_reiniciar()


    # Mostra a cabeça da forca se a pessoa errar 1 vez
    if escolha == "Tormento" and num_erros == 1:
        
        # Muda a imagem por outra
        imagem_forca.config(image=endereco_imagem_cabeca)

    # Mostra o corpo da forca se a pessoa errar 2 vezes
    if escolha == "Tormento" and num_erros == 2:
        
        # Muda a imagem por outra
        imagem_forca.config(image=endereco_imagem_corpo)

    # Mostra os dois braços da forca se a pessoa errar 3 vezes
    if escolha == "Tormento" and num_erros == 3:
        
        # Muda a imagem por outra
        imagem_forca.config(image=endereco_imagem_braco2)
    
    # Mostra as duas pernas da forca se a pessoa errar 4 vezes
    if escolha == "Tormento" and num_erros == 4:
        
        # Muda a imagem por outra
        imagem_forca.config(image=endereco_imagem_perna2)   

        # Chamando função
        mostrar_palavra_correta()

        # Cria uma mensagem de derrota
        derrota = tk.Label(tela, text="VOCÊ PERDEU!!!", bg="white", fg="red", font = ("Times New Roman", 17))
        
        # Posiciona a mensagem
        derrota.place(x = 627, y = 150)

        # Comando que impede a leitura de qual tecla o usuário está pressionando
        tela.unbind("<KeyPress>")

        # Chamando função
        criar_botao_reiniciar()


    # Mostra a cabeça da forca se a pessoa errar 1 vez 
    if escolha == "Inferno" and num_erros == 1:
        
        # Muda a imagem por outra
        imagem_forca.config(image=endereco_imagem_cabeca)

    # Mostra a forca completa se errar 2 vezes
    if escolha == "Inferno" and num_erros == 2:
        
        # Muda a imagem por outra
        imagem_forca.config(image=endereco_imagem_perna2)

        # Chamando função
        mostrar_palavra_correta()

        # Cria uma mensagem de derrota
        derrota = tk.Label(tela, text="VOCÊ PERDEU!!!", bg="white", fg="red", font = ("Times New Roman", 17))
        
        # Posicona a mensagem
        derrota.place(x = 627, y = 150)

        # Comando que impede a leitura de qual tecla o usuário está pressionando
        tela.unbind("<KeyPress>")

        # Chamando função
        criar_botao_reiniciar()


    # Mostra a forca completa se errar 2 vezes
    if escolha == "Nightmare" and num_erros == 1:
        
        # Muda a imagem por outra
        imagem_forca.config(image=endereco_imagem_perna2)

        # Chamando função
        mostrar_palavra_correta()

        # Cria uma mensagem de derrota
        derrota = tk.Label(tela, text="VOCÊ PERDEU!!!", bg="white", fg="red", font = ("Times New Roman", 17))
        
        # Posiciona a mensagem
        derrota.place(x = 627, y = 150)

        # Comando que impede a leitura de qual tecla o usuário está pressionando
        tela.unbind("<KeyPress>")

        # Chamando função
        criar_botao_reiniciar()


# Deposito vazio para letras Certas sem repetir nenhuma
deposito_letras_certas = []

# Deposito vazio para letras certas
letras_palavra = []

# Deposito vazio para letras repetidas
deposito_letras_repetidas = [] 

# Deposito vazio para letras erradas
deposito_letras_erradas = []


# Definindo a contagem da barra de proogresso
for barra in tqdm(range(100)):

    # Definindo o tempo entre cada contagem
    time.sleep(0.015)


# Opções de dificuldade
opcoes = ["Normal", "Tormento", "Inferno", "Nightmare"]

# Título e botões
escolha = easygui.buttonbox("Escolha um nível de dificuldade: ", choices=opcoes)


# Cria a tela
tela = tk.Tk()

# Define a janela para o modo de tela cheia
tela.geometry('1300x700')

# Coloca a janela no topo, em cima de outras janelas
tela.attributes("-topmost", True)

# Deixa o fundo Branco
tela.configure(background='white')


# Caminho atual dos arquivos
caminho_atual = os.path.abspath(os.path.dirname(__file__))

caminho_relativo_forca_txt = os.path.join(caminho_atual, 'Recursos_Jogo/forca.txt')

# Ler dados de um arquivo
with open(caminho_relativo_forca_txt, 'r') as arquivo:

    # Organiza o arquivo para ser lido
    palavra = arquivo.readlines()
    
# Retira o símbolo de quebrar linha "/n"
sem_quebra_linha = [linha.rstrip() for linha in palavra]

# Palavra sorteada sem a quebra de linha visível
palavra_sorteada = choice(sem_quebra_linha)


# Todos os caminhos relativos dos arquivos do jogo
caminho_relativo_imagem_forca = os.path.join(caminho_atual, 'Recursos_Jogo/madeiraForca.png')
caminho_relativo_imagem_cabeca = os.path.join(caminho_atual, 'Recursos_Jogo/cabecaForca.png')
caminho_relativo_imagem_corpo = os.path.join(caminho_atual, 'Recursos_Jogo/corpoForca.png')
caminho_relativo_imagem_braco1 = os.path.join(caminho_atual, 'Recursos_Jogo/braco1Forca.png')
caminho_relativo_imagem_braco2 = os.path.join(caminho_atual, 'Recursos_Jogo/braco2Forca.png')
caminho_relativo_imagem_perna1 = os.path.join(caminho_atual, 'Recursos_Jogo/perna1Forca.png')
caminho_relativo_imagem_perna2 = os.path.join(caminho_atual, 'Recursos_Jogo/perna2Forca.png')


# Buscar o endereço das imagens
endereco_imagem_forca = tk.PhotoImage(file=caminho_relativo_imagem_forca) 

endereco_imagem_cabeca = tk.PhotoImage(file=caminho_relativo_imagem_cabeca)

endereco_imagem_corpo = tk.PhotoImage(file=caminho_relativo_imagem_corpo)

endereco_imagem_braco1 = tk.PhotoImage(file=caminho_relativo_imagem_braco1)

endereco_imagem_braco2 = tk.PhotoImage(file=caminho_relativo_imagem_braco2)

endereco_imagem_perna1 = tk.PhotoImage(file=caminho_relativo_imagem_perna1)

endereco_imagem_perna2 = tk.PhotoImage(file=caminho_relativo_imagem_perna2)


# Traz a imagem para o parâmetro 'image' através da widget(ferramenta) 'Label'
imagem_forca = tk.Label(tela, image=endereco_imagem_forca)

# Posiciona a imagem
imagem_forca.place(x=250, y=150)


# Define a dificuldade do jogo
if escolha == "Normal":
    
    # Chama a função que irá verificar os erros
    verificar_erros()
    
    # Define a quantidade de tentativas do jogador
    tentativas = 6

# Define a dificuldade do jogo
elif escolha == "Tormento":

    # Chama a função que irá verificar os erros
    verificar_erros()

    # Define a quantidade de tentativas do jogador
    tentativas = 4


# Define a dificuldade do jogo
elif escolha == "Inferno":

    # Chama a função que irá verificar os erros
    verificar_erros()

    # Define a quantidade de tentativas do jogador
    tentativas = 2


# Define a dificuldade do jogo
elif escolha == "Nightmare":

    # Chama a função que irá verificar os erros
    verificar_erros()

    # Define a quantidade de tentativas do jogador
    tentativas = 1
 

# Ler quantas letras tem na palavra
letras_quantidade = len(palavra_sorteada)


# Deixam as letras separadas e em maiúsculas
letras_separadas = list(palavra_sorteada.upper())

caminho_relativo_imagem_caixa_letra = os.path.join(caminho_atual, 'Recursos_Jogo/caixaLetra.png')

# Chama a imagem da caixa da letra para uma variável
caixa_letra = tk.PhotoImage(file=caminho_relativo_imagem_caixa_letra)


# Número incial de um contador que faz adição
c = 0

# Para cada letra da palavra selecionada, chama uma caixa
for cada_letra in range(1, letras_quantidade + 1):

    # Soma 40 ao contador
    c += 40

    # Chama a imagem na tela
    letra = tk.Label(tela, image=caixa_letra)

    # Posiciona cada caixa com 40 pixels de distância uma das outras
    letra.place(x=550 + c, y=445)


# Palavra que será lida
palavra = palavra_sorteada

# Mensagem vazia antes de ser preenchida
mensagem_posicao = tk.Label(tela, text="", bg="white")

# Chama a função e analisa qual tecla foi pressionada atráves o '<KeyPress>'
tela.bind('<KeyPress>', tecla_pressionada)


# Soma 40 ao contador 
c2 = 0

# Lista vazia
lista_vazia_erros = []


# Cria um espaço vazio para cada letra errada
for letra_errada in range(1, tentativas + 1):  

    # Soma 40 ao contador  
    c2 += 40

    # Mensagem vazia antes de ser preenchida
    letra_errada = tk.Label(tela, text="", bg="white", fg="red")

    # Mostra as coordenadas
    letra_errada.place(x = 542 + c2, y = 600)
    
    # Formata a letra
    letra_errada.config(font=("Times New Roman", 15))
    
    # Adiciona os erros à lista vazia
    lista_vazia_erros.append(letra_errada)


#Cria mensagem de instrução para sair da tela
legenda = tk.Label(tela, text="Presione a tecla 'ESC' para sair do programa", bg='white')

# Associa a tecla 'Esc' à função 'sairJanela'
tela.bind("<Key-Escape>", sair_janela)

# Lista vazia
lista_vazia = []

# Número inicial de um contador que faz adição
c3 = 0

# Cria uma letra para cada caixa
for cada_caixa in range(1, letras_quantidade + 1):
    
    # Soma 40 ao contador
    c3 += 40
    
    # Cria uma mensagem vazia
    legendas_letras = tk.Label(tela, text="", bg="white")

    # Mostras as coodenadas e define a distância entre as letras
    legendas_letras.place(x = 557.5 + c3, y = 447.5)

    # Formata a letra
    legendas_letras.config(font=("Times New Roman", 17))

    # Acrescenta as letras recebidas por meio da função(para o fim da lista), na variável "legendasLetras"
    lista_vazia.append(legendas_letras) 

# Faz o programa ficar aberto e em loop
tela.mainloop()
