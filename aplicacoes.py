def program(x,y):
    if (x<=10 or x>=0) and (x<10 and y>=0):
        
        return 'Valores entre 0 e 10'
    else:
        return 'Fora da faixa'
    
def par_impar(n):
    if n%2 == 0:
        return 'Número par'
    else:
        return 'Número ímpar'

def acesso(user, senha):
    login = 'glauco'
    password = '123'
    if user == login and senha == password:
        return 'Seja bem vindo'
    else:
        return 'Login ou senha inválidos'    

