


from random import choice # Módulo para randomizar
import tkinter as tk # Módulo gráfico
from tqdm import tqdm # Módulo para barra de progresso
import time # Módulo para tempo
import easygui # Módulo para criar menu 
import os # Módulo que reinicia o programa do zero
import sys # Módulo que reincia o programa do zero


# Função que identifica o evento de clique do usuário
def teclaPressionada(event):

    # Busca a letra que o usuário pressionou, no alfabeto
    if event.char.isalpha():
        
        # Verifica a letra que o usuário pressionou
        verificaCliques = event.char.upper()
        
        # Verifica a letra pressionada pelo usuário e ver se ela pertence a lista das letras da palavra aleatória
        if verificaCliques in set(letrasSeparadas):
            
            # Se a condicional de cima for verdade, ela acrescenta a letra aleatória correspondente à lista vazia nomeada de "depositoLetrasCertas" 
            depositoLetrasCertas.append(verificaCliques)


        # Encontra os números e as posições de uma letra na palavra selecionada sem se importa se são maiúsculas ou minúsculas
        posicoes = [numeroLetras+1 for numeroLetras, letra in enumerate(palavra) if letra.upper() == event.char or (numeroLetras == 0 and letra.upper() == event.char.upper()) or letra.lower() == event.char or (numeroLetras == 0 and letra.lower() == event.char.lower())] 
        
        # Mensagem que aparece da letra e da posição na tela
        mensagemPosicao.config(text=f"Posições da letra {event.char.upper()}: {posicoes}")
        

        # Verifica a letra que o usuário pressionou
        verificaCliques = event.char.upper()

        # Verifica se a letra já foi pressionada antes
        if verificaCliques in depositoLetrasRepetidas: 
            
            
            # Cria uma mensagem
            letrasRepetidas = tk.Label(tela, text=(f"A letra {verificaCliques} já foi utilizada!!!"), bg="white", fg="brown") 

            # Apliaca as coordenadas da mensagem
            letrasRepetidas.place(x = 900, y = 250)

            # Formata a mensagem
            letrasRepetidas.config(font=("Times New Roman", 17))


        # Executará se a condicional de cima não fôr satisfeita    
        else:
            
            # verisifica se a letra que o usuário pressionou não pertence a palavra e nem as posições dela
            if verificaCliques not in palavraSorteada.upper() and not posicoes: 
                    
                # Pega a letra pressionada e manda para uma lista vazia
                depositoLetrasErradas.append(verificaCliques)
                    
                # Mostra o texto antecedente às letras erradas
                letrasErradas = tk.Label(tela, text="Letras Erradas: ", bg="white")
                    
                # Mostra as coordenadas
                letrasErradas.place(x = 620, y = 550)

                # Formata as letras
                letrasErradas.config(font=("Times New Roman", 17))

                
            # Loop que define o índice da letra mais a variável qualquer
            for numeroLoopErro, naoLetra in enumerate(depositoLetrasErradas):

                # Apenas garante que não haja erro de indexação
                if numeroLoopErro < len(listaVaziaErros):
                            
                    # Ele atribui esse loop ao loop de texto vazio que aparece na tela, colocando as letras erradas uma por vez de acordo com a necessidade
                    listaVaziaErros[numeroLoopErro]['text'] = naoLetra
                            
                    # Verifica os erros
                    
                    verificarErros()

            
            # Se a letra não tiver na palavra aleátoria, a condicional é executada
            if verificaCliques not in letrasPalavra:
                    
                # Acrescenta a letra pressionada pelo usuário na lista vazia
                letrasPalavra.append(verificaCliques)

                # Chama a função que verifica a vitória
                verificaVitoria()

                # Adiciona a letra à lista de letras pressionadas que é o "depositoLetrasCertas"
                depositoLetrasRepetidas.append(verificaCliques)
        

        # Verifica se a letra que o usuário pressionou, pertence a palavra randômica
        if event.char.upper() in palavraSorteada.upper() and posicoes == [numeroPosicao+1 for numeroPosicao in range(len(palavraSorteada)) if palavraSorteada[numeroPosicao].upper() == event.char.upper()]: 
            
            # Letra pressionada que será exibida nas posições especificadas
            verificaCliques = event.char.upper() 
        

            # Estrutura de repetição que ira definir as posições das letras
            for posicao in posicoes:
                
                # Modifica o espaço vazio onde se encontra a letra, pela letra selecionada pelo usuário
                listaVazia[posicao-1].config(text=verificaCliques)             
    

    # Executará se a condicional de cima não fôr satisfeita 
    else:
        
        #Mensagem que aparece se a tecla pressionada não for uma letra
        mensagemPosicao.config(text="A tecla pressionada não é uma letra.") 
    return




# Função para fechar programa usando a tecla 'Esc'
def sairJanela(event): 
    
    # Comando que fecha programa
    tela.destroy()
    return

# Função para reiniciar o jogo utilizando módulos
def reiniciar(event=None):

    python = sys.executable
    os.execl(python, python, *sys.argv)


# Função para criar o botão de reiniciar
def criarBotaoReiniciar():
    
    # Cria botão de Reiniciar
    botaoReiniciar = tk.Button(tela, text="Reiniciar", command=lambda:[reiniciar()], bg = "brown", fg = "White")

    # Aplica as coordenadas do botão
    botaoReiniciar.place(x = 645, y = 650)


# Função que mostra a palavra que tinha que ser, na tela
def mostrarPalavraCorreta():

    # Cria a mensagem
    palavraCerta = tk.Label(tela, text=(f"A palavra era '{palavraSorteada.upper()}'!!!"), bg="white", fg="blue", font=("Times New Roman", 20))

    # posiciona a imagem
    palavraCerta.place(x = 880, y = 250)


# Função que verifica a vitória
def verificaVitoria():
    
    
    # Verificar se todas as letras da lista estão presentes na palavra aleatória
    if set(depositoLetrasCertas) == set(letrasSeparadas):
        

        # Cria uma mensagem de vitória
        vitoria = tk.Label(tela, text="PARABÉNS, VOCÊ VENCEU!!!", bg="white", fg="green", font=("Times New Roman", 17))

        # Posiciona a imagem na tela
        vitoria.place(x = 545, y = 50)

        # Chamando função
        criarBotaoReiniciar()

        # Comando que impede a leitura de qual tecla o usuário está pressionando
        tela.unbind("<KeyPress>")


# Função que verifica Erros e monta a forca
def verificarErros():

    # Número de letras erradas pressionadas pela usuário
    numErros = len(depositoLetrasErradas)


    # Mostra a cabeça da forca se a pessoa errar 1 vez
    if escolha == "Normal" and numErros == 1:
        
        # Muda a imagem por outra
        imagemForca.config(image=enderecoImagemCabeca)

    # Mostra o corpo da forca se a pessoa errar 2 vezes
    if escolha == "Normal" and numErros == 2:
        
        # Muda a imagem por outra
        imagemForca.config(image=enderecoImagemCorpo)

    # Mostra um braço da forca se a pessoa errar 3 vezes
    if escolha == "Normal" and numErros == 3:
        
        # Muda a imagem por outra
        imagemForca.config(image=enderecoImagemBraco1)

    # Mostra o outro braço da forca se a pessoa errar 4 vezes
    if escolha == "Normal" and numErros == 4:
        
        # Muda a imagem por outra
        imagemForca.config(image=enderecoImagemBraco2)

    # Mostra a perna da forca se a pessoa errar 5 vezes
    if escolha == "Normal" and numErros == 5:
        
        # Muda a imagem por outra
        imagemForca.config(image=enderecoImagemPerna1)

    # Mostra a outra perna da forca se a pessoa errar 6 vezes
    if escolha == "Normal" and numErros == 6:
        
        # Muda a imagem por outra
        imagemForca.config(image=enderecoImagemPerna2)

        # Chamando função
        mostrarPalavraCorreta()

        # Cria uma mensagem de derrota
        derrota = tk.Label(tela, text="VOCÊ PERDEU!!!", bg="white", fg="red", font = ("Times New Roman", 17))
        
        # Posiciona a mensagem
        derrota.place(x = 627, y = 50)

        # Comando que impede a leitura de qual tecla o usuário está pressionando
        tela.unbind("<KeyPress>")

        # Chamando função
        criarBotaoReiniciar()


    # Mostra a cabeça da forca se a pessoa errar 1 vez
    if escolha == "Tormento" and numErros == 1:
        
        # Muda a imagem por outra
        imagemForca.config(image=enderecoImagemCabeca)

    # Mostra o corpo da forca se a pessoa errar 2 vezes
    if escolha == "Tormento" and numErros == 2:
        
        # Muda a imagem por outra
        imagemForca.config(image=enderecoImagemCorpo)

    # Mostra os dois braços da forca se a pessoa errar 3 vezes
    if escolha == "Tormento" and numErros == 3:
        
        # Muda a imagem por outra
        imagemForca.config(image=enderecoImagemBraco2)
    
    # Mostra as duas pernas da forca se a pessoa errar 4 vezes
    if escolha == "Tormento" and numErros == 4:
        
        # Muda a imagem por outra
        imagemForca.config(image=enderecoImagemPerna2)   

        # Chamando função
        mostrarPalavraCorreta()

        # Cria uma mensagem de derrota
        derrota = tk.Label(tela, text="VOCÊ PERDEU!!!", bg="white", fg="red", font = ("Times New Roman", 17))
        
        # Posiciona a mensagem
        derrota.place(x = 627, y = 150)

        # Comando que impede a leitura de qual tecla o usuário está pressionando
        tela.unbind("<KeyPress>")

        # Chamando função
        criarBotaoReiniciar()


    # Mostra a cabeça da forca se a pessoa errar 1 vez 
    if escolha == "Inferno" and numErros == 1:
        
        # Muda a imagem por outra
        imagemForca.config(image=enderecoImagemCabeca)

    # Mostra a forca completa se errar 2 vezes
    if escolha == "Inferno" and numErros == 2:
        
        # Muda a imagem por outra
        imagemForca.config(image=enderecoImagemPerna2)

        # Chamando função
        mostrarPalavraCorreta()

        # Cria uma mensagem de derrota
        derrota = tk.Label(tela, text="VOCÊ PERDEU!!!", bg="white", fg="red", font = ("Times New Roman", 17))
        
        # Posicona a mensagem
        derrota.place(x = 627, y = 150)

        # Comando que impede a leitura de qual tecla o usuário está pressionando
        tela.unbind("<KeyPress>")

        # Chamando função
        criarBotaoReiniciar()


    # Mostra a forca completa se errar 2 vezes
    if escolha == "Nightmare" and numErros == 1:
        
        # Muda a imagem por outra
        imagemForca.config(image=enderecoImagemPerna2)

        # Chamando função
        mostrarPalavraCorreta()

        # Cria uma mensagem de derrota
        derrota = tk.Label(tela, text="VOCÊ PERDEU!!!", bg="white", fg="red", font = ("Times New Roman", 17))
        
        # Posiciona a mensagem
        derrota.place(x = 627, y = 150)

        # Comando que impede a leitura de qual tecla o usuário está pressionando
        tela.unbind("<KeyPress>")

        # Chamando função
        criarBotaoReiniciar()


# Deposito vazio para letras Certas sem repetir nenhuma
depositoLetrasCertas = []

# Deposito vazio para letras certas
letrasPalavra = []

# Deposito vazio para letras repetidas
depositoLetrasRepetidas = [] 

# Deposito vazio para letras erradas
depositoLetrasErradas = []


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
caminhoAtual = os.path.abspath(os.path.dirname(__file__))

caminhoRelativoForcaTxt = os.path.join(caminhoAtual, 'forca.txt')

# Ler dados de um arquivo
with open(caminhoRelativoForcaTxt, 'r') as arquivo:

    # Organiza o arquivo para ser lido
    palavra = arquivo.readlines()
    
# Retira o símbolo de quebrar linha "/n"
semQuebraLinha = [linha.rstrip() for linha in palavra]

# Palavra sorteada sem a quebra de linha visível
palavraSorteada = choice(semQuebraLinha)


# Todos os caminhos relativos dos arquivos do jogo
caminhoRelativoImagemForca = os.path.join(caminhoAtual, 'madeiraForca.png')
caminhoRelativoImagemCabeca = os.path.join(caminhoAtual, 'cabecaForca.png')
caminhoRelativoImagemCorpo = os.path.join(caminhoAtual, 'corpoForca.png')
caminhoRelativoImagemBraco1 = os.path.join(caminhoAtual, 'braco1Forca.png')
caminhoRelativoSImagemBraco2 = os.path.join(caminhoAtual, 'braco2Forca.png')
caminhoRelativoImagemPerna1 = os.path.join(caminhoAtual, 'perna1Forca.png')
caminhoRelativoImagemPerna2 = os.path.join(caminhoAtual, 'perna2Forca.png')


# Buscar o endereço das imagens
enderecoImagemForca = tk.PhotoImage(file=caminhoRelativoImagemForca) 

enderecoImagemCabeca = tk.PhotoImage(file=caminhoRelativoImagemCabeca)

enderecoImagemCorpo = tk.PhotoImage(file=caminhoRelativoImagemCorpo)

enderecoImagemBraco1 = tk.PhotoImage(file=caminhoRelativoImagemBraco1)

enderecoImagemBraco2 = tk.PhotoImage(file=caminhoRelativoSImagemBraco2)

enderecoImagemPerna1 = tk.PhotoImage(file=caminhoRelativoImagemPerna1)

enderecoImagemPerna2 = tk.PhotoImage(file=caminhoRelativoImagemPerna2)


# Traz a imagem para o parâmetro 'image' através da widget(ferramenta) 'Label'
imagemForca = tk.Label(tela, image=enderecoImagemForca)

# Posiciona a imagem
imagemForca.place(x=250, y=150)


# Define a dificuldade do jogo
if escolha == "Normal":
    
    # Chama a função que irá verificar os erros
    verificarErros()
    
    # Define a quantidade de tentativas do jogador
    tentativas = 6

# Define a dificuldade do jogo
elif escolha == "Tormento":

    # Chama a função que irá verificar os erros
    verificarErros()

    # Define a quantidade de tentativas do jogador
    tentativas = 4


# Define a dificuldade do jogo
elif escolha == "Inferno":

    # Chama a função que irá verificar os erros
    verificarErros()

    # Define a quantidade de tentativas do jogador
    tentativas = 2


# Define a dificuldade do jogo
elif escolha == "Nightmare":

    # Chama a função que irá verificar os erros
    verificarErros()

    # Define a quantidade de tentativas do jogador
    tentativas = 1
 

# Ler quantas letras tem na palavra
letrasQuantidade = len(palavraSorteada)


# Deixam as letras separadas e em maiúsculas
letrasSeparadas = list(palavraSorteada.upper())

caminhoRelativoImagemCaixaLetra = os.path.join(caminhoAtual, 'caixaLetra.png')

# Chama a imagem da caixa da letra para uma variável
caixaLetra = tk.PhotoImage(file=caminhoRelativoImagemCaixaLetra)


# Número incial de um contador que faz adição
c = 0

# Para cada letra da palavra selecionada, chama uma caixa
for cadaLetra in range(1, letrasQuantidade + 1):

    # Soma 40 ao contador
    c += 40

    # Chama a imagem na tela
    letra = tk.Label(tela, image=caixaLetra)

    # Posiciona cada caixa com 40 pixels de distância uma das outras
    letra.place(x=550 + c, y=445)


# Palavra que será lida
palavra = palavraSorteada

# Mensagem vazia antes de ser preenchida
mensagemPosicao = tk.Label(tela, text="", bg="white")

# Chama a função e analisa qual tecla foi pressionada atráves o '<KeyPress>'
tela.bind('<KeyPress>', teclaPressionada)


# Soma 40 ao contador 
c2 = 0

# Lista vazia
listaVaziaErros = []


# Cria um espaço vazio para cada letra errada
for letraErrada in range(1, tentativas + 1):  

    # Soma 40 ao contador  
    c2 += 40

    # Mensagem vazia antes de ser preenchida
    letraErrada = tk.Label(tela, text="", bg="white", fg="red")

    # Mostra as coordenadas
    letraErrada.place(x = 542 + c2, y = 600)
    
    # Formata a letra
    letraErrada.config(font=("Times New Roman", 15))
    
    # Adiciona os erros à lista vazia
    listaVaziaErros.append(letraErrada)


#Cria mensagem de instrução para sair da tela
legenda = tk.Label(tela, text="Presione a tecla 'ESC' para sair do programa", bg='white')

# Associa a tecla 'Esc' à função 'sairJanela'
tela.bind("<Key-Escape>", sairJanela)

# Lista vazia
listaVazia = []

# Número inicial de um contador que faz adição
c3 = 0

# Cria uma letra para cada caixa
for cadaCaixa in range(1, letrasQuantidade + 1):
    
    # Soma 40 ao contador
    c3 += 40
    
    # Cria uma mensagem vazia
    legendasLetras = tk.Label(tela, text="", bg="white")

    # Mostras as coodenadas e define a distância entre as letras
    legendasLetras.place(x = 557.5 + c3, y = 447.5)

    # Formata a letra
    legendasLetras.config(font=("Times New Roman", 17))

    # Acrescenta as letras recebidas por meio da função(para o fim da lista), na variável "legendasLetras"
    listaVazia.append(legendasLetras) 

# Faz o programa ficar aberto e em loop
tela.mainloop()


