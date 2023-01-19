import time
import pyautogui
import os
# primeiro teste usando metodos em um mini projeto!


class MouseLocal:
    def __init__(self):
        self.valor1 = None
        self.atual  # Para o retorno ao menu
        self.i = 0  # para ser usado nos contadores

    def mouselocalization(self):  # Função criada para localizar o mouse:
        while True:
            print(pyautogui.position())
            print('Aperte Enter para prosseguir:')
            input()  # Colocado apenas para facilitar o controle do mouse e dos parametros
            print("------")

    def clicker(self):  # Função criada para o uso do clicker
        # primeira cordenada valor de x
        input('coloque o mouse no local onde ocorrera os clicks e aperte enter! Não clique dentro do app que sera usado!:')
        self.localx, self.localy = pyautogui.position()
        # Quantidade dos Clicks
        self.valorc1 = int(input('Digite a quantidade de Clicks: '))
        pyautogui.click(x=self.localx, y=self.localy,
                        clicks=self.valorc1, interval=0, button='left')
        print('Você foi devolvido a pagina inicial para caso tenha feito merda! ')
        return self.atual()

    def spawndepalavras(self):
        print('Deixe o mouse preparado no local onde sera feito o spam, não sera necessario clicar!: ')
        self.Valor = int(input('Digite o valor de spawns: '))
        self.men = str(input('Digite a mensagem: '))
        input('Aperte Enter quando estiver tudo pronto: ')
        x, y = pyautogui.position()  # Pega a posição do mouse e coloca no dobleclick
        pyautogui.doubleClick(x=x, y=y, button='left')
        time.sleep(1)
        self.cont = 0
        for self.i in range(self.Valor):
            pyautogui.typewrite(self.men)
            pyautogui.press('Enter')
            self.cont += 1
        if self.cont >= self.Valor:  # Criado para não fechar o programa assim que terminar o spawn
            return self.atual()
    #Desenvolver copiar e colar
    def copiar_colar(self):
        quant = int(input('Quantidade por pasta: '))
        input('Posicione o mouse dentro da pasta e dê enter: ')
        x1, y1 = pyautogui.position()
        print(x1,y1)
        input('Posicione o mouse na dentro da segunda pasta: Enter ')
        x2, y2 = pyautogui.position()
        print(x2,y2)
        cord1x = (x1)
        cord1y = (y1) #armazena as cordenadas em uma tupla
        cord2x = (x2)
        cord2y = (y2)
        input('Olá, devido a este programa esta na primeira fase, recomendo testar! Aperte enter para continuar! ')
        i = 0
        for i in range(quant):
            pyautogui.click(x=cord1x, y=cord1y, clicks=1, interval=0, button='left')
            pyautogui.hotkey('ctrl', 'x')
            pyautogui.hotkey('Down')
            pyautogui.click(x=cord2x, y=cord2y, clicks=1, interval=0, button='left')
            pyautogui.hotkey('ctrl', 'v')
            i+=1
            if i == quant:
                resp = input('Digite s caso deseje criar uma nova pasta ou n caso deseje apenas continuar: ')
                if resp == 's':
                    directory = str(input('Digite o diretorio do arquivo: '))
                    namepast = str(input('Digite o nome da pasta: '))
                    os.mkdir(f'{directory}/`{namepast}')
                else:
                    print('Você deseja continuar? a operação? \n 1) Para voltar para o organizador \n 2) para voltar ao menu \n 3)Sair ')
                    rep1 = int(input('>>>'))
                    if rep1 == 1:
                        return self.copiar_colar()
                    elif rep1 == 2:
                        return self.atual()
                    else:
                        exit
#Em desenvolvimento
    def atual(self):  # Usado para o controle das funções
        print("digite um valor para escolher uma função:\n 1) ver localização do mouse! \n 2) Usar o um cliquer! \n 3) Usar o Spawn de Palavras! \n 4) Digite 4 para acessar o organizador de pasta!")
        self.valor1 = int(input('>>>: '))
        key1 = MouseLocal()
        if self.valor1 == 1:
            key1.mouselocalization()
        elif self.valor1 == 2:
            key1.clicker()
        elif self.valor1 == 3:
            key1.spawndepalavras()
        elif self.valor1 == 4:
            key1.copiar_colar()
        else:
            exit


mousekey = MouseLocal()
mousekey.atual()
# Em desenvolvimento....
# by Petryck Slater
