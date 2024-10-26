import random 

# Função que gera a introdução da história 
def gerar_introducao():
    introducoes = ["Em uma noite chuvosa na metropole", "Num campo de trigo ao sul do texas"]
    return random.choice(introducoes)

# Função que gera o desenvolvimento da história 
def gerar_desenvolvimento():
    desenvolvimentos = ["a população clama por seu heroi", "um garoto muito especial é deixado na porta de um casal"]
    return random.choice(desenvolvimentos)

# Função que gera o final de toda a história
def gerar_final():
    finais = ["na esperança que o crime seja combatido.","afinal ele está destinado a salvar o mundo."]
    return random.choice(finais)

# Função principal que gera toda a história
def gerar_historia():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao} {desenvolvimento} {final}"
    return historia

# Exibe a história gerada 
if __name__=="__main__":
    print(gerar_historia())

