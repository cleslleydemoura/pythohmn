import pandas as pd

nome_musicas = ["Sick Love", "WORTH IT", "DICE", "Midas Touch", "Nothing", "Californication", "Controllah", "The Blonde", "Ma Boo", "Wae ironi", "Yayaya"]
artistas = ["Red Hot Chilli Peppers", "Rex Orange County", "NMIXX", "Kiss Of Life", "Kiss Of Life", "Red Hot Chilli Peppers", "Gorillaz", "TV Girl", "T-ARA", "T-ARA", "T-ARA"]
genero = ["Rock/Alternative", "Pop", "K-pop", "Pop", "Pop", "Rock/Alternative", "Rock/Alternative", "Rock", "Pop", "Pop", "Pop"]
nome_album = ["The Getaway", "who Cares?", "ENTWURF", "Midas Touch", "Midas Touch", "Californication", "Cracker Island", "French Exit", "Temptastic", "Temptastic", "Temptastic"]
ano_lancamento = [2016, 2022, 2022, 2024, 2024, 1999, 2023, 2024, 2011, 2011, 2011]
duracao_musica = [3.4, 2.4, 2.4, 2.4, 3.3, 5.2, 2.3, 3.4, 3.2, 3.5, 3.2]

dados_musicais = {
    'Música': nome_musicas,
    'Artista': artistas,
    'Álbum' : nome_album,
    'Ano de lançamento': ano_lancamento,
    'Duração (segundos)' : duracao_musica,
    'Gênero': genero
}

# 1. Apresente em tela (output) toda a base de dados. Pontuação: 0,5 pontos
print("1. Apresente em tela (output) toda a base de dados.")
musica_df = pd.DataFrame(dados_musicais)
print(musica_df)
display(musica_df)
print()
# 2. Apresente o tamanho do seu dataframe (quantas colunas x linhas). Pontuação: 0,5 pontos
print("2. Apresente o tamanho do seu dataframe (quantas colunas x linhas).")
print(musica_df.shape)
print()
# 3. Acesse a linha (x) e apresente em tela todas as características do item. Pontuação: 0,5 pontos
print("3. Acesse a linha (x) e apresente em tela todas as características do item.")
df = pd.DataFrame(dados_musicais)
line = df.iloc[4]
print(line)
print()
# 4. Verifique se o dataframe está vazio. Pontuação: 0,5 pontos
print("4. Verifique se o dataframe está vazio.")
print(df.empty)
print()
# 5. Apresente em tela os 5 primeiros registros da base de dados. Pontuação: 0,5 pontos
print("5. Apresente em tela os 5 primeiros registros da base de dados.")
head = pd.DataFrame(dados_musicais)
print(musica_df.head())
print()
# 6. Exclua um item (linha) de sua base de dados. Pontuação: 0,5 pontos
print("6. Exclua um item (linha) de sua base de dados.")
delete_indice = 6
musica_df = musica_df.drop(delete_indice)
print(musica_df)
print()
# 7. Adicione um item (linha) na sua base de dados. Pontuação: 0,5 pontos
print("7. Adicione um item (linha) na sua base de dados.")
new_item = {
    'Música': "A",
    'Artista': "Rainbow",
    'Álbum' : "A - Digital Single",
    'Ano de lançamento': "2010",
    'Duração (segundos)' : '3.2',
    'Gênero': "pop"
}

musica_df = pd.concat([musica_df, pd.DataFrame(new_item, index=[0])], ignore_index=True)
print(musica_df)

# 8. Transponha a coluna para a linha em sua base de dados. Pontuação: 0,5 pontos
print("8. Transponha a coluna para a linha em sua base de dados.")
df = pd.DataFrame(dados_musicais)
df_transpor = df.T
print(df_transpor)
print(musica_df.shape)
display(df_transpor)

# 9. Apresente em tela somente a 1ª e a 2ª coluna (rótulo) da base de dados. Pontuação: 0,5 pontos
print("9. Apresente em tela somente a 1ª e a 2ª coluna (rótulo) da base de dados.")
display(df.loc[:, ['Música', 'Artista']])
print()

# 10. Informe como foi desenvolvido o Projeto. Pontuação: 0,5 pontos
