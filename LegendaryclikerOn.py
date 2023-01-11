import time
import pyautogui
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
        self.local1 = int(input('Digite a primeira cordenada: '))
        # segunda cordenada valor de y
        self.local2 = int(input('Digite a Segunda: '))
        # Quantidade dos Clicks
        self.valorc1 = int(input('Digite a quantidade de Clicks: '))
        pyautogui.click(x=self.local1, y=self.local2,
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

    def atual(self):  # Usado para o controle das funções
        print("digite um valor para escolher uma função:\n 1) ver localização do mouse! \n 2) Usar o um cliquer! \n 3) Usar o Spawn de Palavras!")
        self.valor1 = int(input('>>>: '))
        key1 = MouseLocal()
        if self.valor1 == 1:
            key1.mouselocalization()
        elif self.valor1 == 2:
            key1.clicker()
        elif self.valor1 == 3:
            key1.spawndepalavras()
        else:
            return 0


mousekey = MouseLocal()
mousekey.atual()
# Em desenvolvimento....
# by Petryck Slater
