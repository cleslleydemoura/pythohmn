
# 1) O que é um Dado?
# Dados são valores atribuídos a algo. Onde se armazena uma informação de um determinado tipo de dado pela simples referência a um nome simbólico.

# 2) Qual a importância de um algorítimo na área da tecnologia?
# Os algoritmos servem como base e orientação das ações que um programa precisa realizar para cumprir o que se espera dele.

# 3) Quais são as partes que definem um algoritimo?
# Entrada, processamento e saída.

# 4) Construa um algoritimo que recebe uma lista com "CINEMAS", solicite a um usuário que informe três tipos de filmes da área de TI e apresente quais foram os filmes.
jobs = input("Adicione o primeiro filme: ")
o_quinto_poder = input("Adicione o segundo filme: ")
o_jogo_da_imitacao = input("Adicione o terceiro filme: ")

cinemas = [jobs, o_quinto_poder, o_jogo_da_imitacao]
print(cinemas)
len(cinemas)

# 5) Insira um elemento na lista de CINEMAS.
animais = ["coala", "cavalo", "flamingo"]
animais.append("baleia")
print(animais)
len(animais)

# 6) Troque a posição dos elementos no índice [0] para [1].
animais = ["coala", "cavalo", "flamingo"]
animais.pop(0)
animais.insert(1,"coala")
print(animais)

# 7) Apague o primeiro dado da lista.
animais.remove("coala")
print(animais)

# 8) Informe o maior valor da lista.
max(animais)

# 9) Informe o menor valor da lista.
min(animais)

# 10) Apague o conteúdo da lista.
cinemas.clear()
animais.clear()
