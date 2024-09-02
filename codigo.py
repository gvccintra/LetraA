def verificar_letra_a(texto):
    # Conta a ocorrência de minúscula e maiúscula
    count_a = texto.count('a')
    count_A = texto.count('A')
    
    # Soma as contagens para obter o total de letras A
    total_a = count_a + count_A
    
    # Verifica se existe a letra A na string
    if total_a > 0:
        print(f"A letra 'a' aparece {total_a} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")


string = input("Digite uma frase: ")
verificar_letra_a(string)