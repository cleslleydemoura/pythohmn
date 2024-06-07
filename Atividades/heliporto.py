# Complexo ou complicado?
# Faça um programa que informe o número de loops para um contador que imprima todos os números primos de 1 a 100.

import this

def primo(number):

#Verifica se o número é primo
    if number < 2:
        return False
#Contador = 'i'
    for contador in range(2, int(math.sqrt(number)) + 1):
      # range(2, int(math.sqrt(number)) + 1): Esta é uma função que cria um intervalo de números.
      # No caso, começa em 2 (pois os números primos são maiores que 1) e termina em int(math.sqrt(number)) + 1.
      # O int(math.sqrt(number)) calcula a raiz quadrada de number, e a função int() arredonda esse valor para o inteiro mais próximo.
      # Adicionamos 1 para garantir que o último número seja incluído no intervalo.
        if number % contador == 0:
            return False
    return True

def main():
#Imprime todos os números primos de 1 a 100.
    print("Os números primos de 1 a 100 são:")
    count = 0  #Contador de loops
    for num in range(1, 101):
        if primo(num):
            count += 1
            print(num)
    print(f"Número de loops: {count}")

if __name__ == "__main__":
    main()

#Utilizei o método FOR por ser mais rápido por que ele já tem mais velocidade pelo range.

#Exemplo da professora:

import this

for contador in range (1, 101):
  print(contador)

contador = 0;

while contador <= 100:
  print(contador)
  contador = contador + 1

#O que é busca?
#Criar DataFrame bidimensional de Heliportos em Brasília com Pandas e Python

import pandas as pd

heliporto_nome = ["Heliponto - Autódromo Internacional de Brasília - SWWR", "Heliponto Parque Cidade (SNCN, DF0016)", "Heliponto - Palácio da Alvorada", "Heliponto - PCDF - SWSW", "Heliponto - Brasil XXI - SIIY", "Heliponto - HFA", "Heliporto da Granja do Torto", "Heliponto - Águas Claras - SIHQ", "Heliponto - Parkway - SJWY", "Heliponto - Presídio Papuda", "Heliporto - HRC", "Heliponto - Hospital Anchieta - SJDF", "Batalhão de Aviação Operacional - PMDF", "Grupamento de Aviação Operacional - GAvOp - CBMDF", "Heliponto HRG", "Heliporto - Hospital Regional de Santa Maria"]
heliporto_endereco = ["SRPN Trecho 1 - Brasília, DF, 70655-775", "SCS Q. 6 BL A - Asa Sul, Brasília - DF, 70740-610", "Zona Cívico-Administrativa Palacio da Alvorada, Brasília - DF", "SGO - Brasília, DF", "St. Hoteleiro - Águas Claras, Brasília - DF", "St. Sudoeste - Cruzeiro / Sudoeste / Octogonal, Brasília - DF", "Lago Norte, Brasília - DF", "Águas Claras, Brasília - DF", "Park Way Q 26 Conj. 1 - Núcleo Bandeirante, Brasília - DF", "São Sebastião, Brasília - DF", "St. M QNM 28 - Ceilândia, Brasília - DF", "St. C Norte QNC AE - Taguatinga, Brasília - DF", "Guará II AE 10 - Guará, Brasília - DF", "SAM Lote D, módulo E, Brasília - DF", "St. Central EQ 47/49 - Gama, Brasília - DF", "Santa Maria, Brasília - DF"]

dados_heliporto = {
    'Nome do Heliporto' : heliporto_nome,
    'Endereço do Heliporto' : heliporto_endereco
}

heliportos_df = pd.DataFrame(dados_heliporto)
print(dados_heliporto)
print()
print(heliportos_df.shape)
display(heliportos_df)
