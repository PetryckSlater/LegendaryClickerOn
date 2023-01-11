import pyautogui
# primeiro teste usando metodos em um mini projeto!


class MouseLocal:
    def __init__(self):
        self.valor1 = None
        self.atual

    def mouselocalization(self): #Função criada para localizar o mouse:
        while True:
            print(pyautogui.position())
            print('Aperte Enter para prosseguir:')
            input() #Colocado apenas para facilitar o controle do mouse e dos parametros
            print("------")

    def clicker(self): #Função criada para o uso do clicker
        self.local1 = int(input('Digite a primeira cordenada: '))
        self.local2 = int(input('Digite a Segunda: '))
        pyautogui.click(x=self.local1, y=329, clicks=200, interval=0, button='left')
        print('Você foi devolvido a pagina inicial para caso tenha feito merda! ')
        return self.atual()

    def atual(self):# Usado para o controle
        print("digite um valor para escolher uma função:\n 1) ver localização do mouse! \n 2) Usar o um cliquer")
        self.valor1 = int(input('>>>: '))
        key1 = MouseLocal()
        if self.valor1 == 1:
            key1.mouselocalization()
        elif self.valor1 == 2:
            key1.clicker()
        else:
            return 0


mousekey = MouseLocal()
mousekey.atual()
#Em desenvolvimento....
#by Petryck Slater