import string, random

class GeradorDeSenha():
    def __init__(self):
        self.letters = string.ascii_letters
        self.numbers = string.digits
        self.specials = string.punctuation
        senha = self.gerar_senha()
        self.comparar_senha(senha)

    def gerar_senha(self):
        senha=(
            random.choices(self.letters,k=7) +
            random.choices(self.numbers, k=7) +
            random.choices(self.specials,k=6)
            )
        
        random.shuffle(senha)
        senha = ''.join(senha)
        return senha

    def comparar_senha(self, senha):
        arquivo = open('senhas_geradas.txt','r')

        if f'{senha}\n' in arquivo:
            print('Senha já existente')
        else:
            arquivo = open('senhas_geradas.txt','a')
            arquivo.write(f'{senha}\n')

        arquivo.close