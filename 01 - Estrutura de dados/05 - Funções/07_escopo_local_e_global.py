salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_bonus(500)  # 2500

def salario_bonus2(bonus, lista):
    global salario
    
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux = {lista_aux}")

    salario += bonus
    return salario

lista = [1]
salario_bonus2(500, lista)  # 2500