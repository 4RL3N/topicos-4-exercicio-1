'''
Dependências:
pandas (pip install pandas)
matplotlib (pip install matplotlib)
seaborn (pip install seaborn)
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def info(n):
    mensagem = f'{n}ª questão \n'
    return mensagem


n = 1
print("Análise do conjunto de dados SIM2024")
print("Data: 15-10-2025")
print("\n")


# 1ª questão #####

print(info(n))
n += 1

df = pd.read_csv("SIM2024.csv", sep=";", encoding="latin1")

# (i) Quantidade total de registros e campos
total_dados = len(df)
total_campos = len(df.columns)

descricao = """
A base SIM (Sistema de Informação sobre Mortalidade) é gerida pelo Ministério da Saúde
e reúne registros de óbitos declarados no Brasil. Cada linha representa uma Declaração
de Óbito (DO), com informações do falecido, da mãe (em casos de óbitos fetais/infantis),
e das circunstâncias da morte.

De acordo com o Dicionário SIM 2025, os principais campos incluem:
- TIPOBITO: indica se o óbito é fetal (1) ou não fetal (2);
- IDADE: codifica idade e unidade (minutos, horas, dias, meses ou anos);
- SEXO: sexo biológico (1/M = masculino, 2/F = feminino, 9 = ignorado);
- RACACOR: cor/raça autodeclarada (1=Branca, 2=Preta, 3=Amarela, 4=Parda, 5=Indígena);
- ESC: escolaridade em faixas de anos de estudo;
- OCUP: ocupação habitual conforme CBO 2002;
- ACIDTRAB: indica se o óbito ocorreu por acidente de trabalho (1=Sim, 2=Não);
- PESO: peso ao nascer (apenas para óbitos fetais ou neonatais);
- IDADEMAE: idade da mãe em anos;
- CAUSABAS: código da causa básica segundo a CID-10.

Esses dados são essenciais para estudos epidemiológicos, vigilância de doenças e
planejamento de políticas públicas de saúde. \n
"""

print(f"Total de registros: {total_dados}")
print(f"Total de campos: {total_campos}")
print(descricao)
#################



# 2ª questão #####

print(info(n))
n += 1
print("Gráfico de barras da porcentagem de dados faltantes por campo aberto em outra janela \n")

# Porcentagem de dados faltantes
faltantes = df.isnull().mean() * 100

# Gráfico
plt.figure(figsize=(12,6))
faltantes.sort_values(ascending=False).plot(kind='bar', color='steelblue')
plt.title("2ª Questão: Percentual de dados faltantes por campo")
plt.ylabel("Porcentagem (%)")
plt.xlabel("Campos")
plt.show()

# Identificar maior e menor taxa
maior = faltantes.idxmax(), faltantes.max()
menor = faltantes.idxmin(), faltantes.min()
print(f"Campo com mais dados faltantes: {maior}\n")
print(f"Campo com menos dados faltantes: {menor}\n")
#################



# 3ª questão #####

print(info(n))
n += 1

campos = ["IDADE", "OCUP", "ACIDTRAB"]

# Percentual de faltantes
faltantes = df[campos].isnull().mean() * 100
print("Percentuais de dados faltantes (%):")
print(faltantes)

# Correlação lógica entre faltantes
faltas_combinadas = df[campos].isnull().sum(axis=1).value_counts().sort_index()
print("\nContagem de registros com 0, 1, 2 ou 3 campos faltantes:")
print(faltas_combinadas)

# Exemplo de correlação entre campos faltantes
exemplo = df[df["OCUP"].isnull() & df["ACIDTRAB"].isnull()].head()
print("\nExemplo de registros com OCUP e ACIDTRAB ausentes simultaneamente:")
print(exemplo[campos])
print("\n")
'''
Segundo o dicionário SIM, OCUP só é preenchido quando o indivíduo tem 5 anos ou mais, e ACIDTRAB se refere a acidente de trabalho. Logo, é esperado que registros de crianças e idosos apresentem ambos os campos vazios.
A IDADE é obrigatória para óbitos não fetais, portanto deve ter poucos ou nenhum valor ausente.
Isso mostra uma relação contextual e lógica entre as variáveis faltantes, e não um erro de coleta.
'''
#################



# 4ª questão

print(info(n))
n += 1
print("Gráfico de barras mostrando dados faltantes antes e depois da imputação será exibido em outra janela\n")

# Criar variável de controle para PESO faltante (antes de preencher)
df["peso_faltante"] = df["PESO"].isnull()

# Contagem inicial de faltantes
antes = df[["SEXO", "RACACOR", "ESC", "PESO"]].isnull().sum()
print("Antes do preenchimento:")
print(antes)

# Preenchimento sem warnings
df["SEXO"] = df["SEXO"].fillna(df["SEXO"].mode()[0])
df["RACACOR"] = df["RACACOR"].fillna(df["RACACOR"].mode()[0])
df["ESC"] = df["ESC"].fillna(df["ESC"].mode()[0])
df["PESO"] = df["PESO"].fillna(df["PESO"].mean())

# Contagem após o preenchimento
depois = df[["SEXO", "RACACOR", "ESC", "PESO"]].isnull().sum()
print("\nDepois do preenchimento:")
print(depois)

# Comparar visualmente antes e depois
faltantes_df = pd.DataFrame({"Antes": antes, "Depois": depois})
faltantes_df.plot(kind="bar", figsize=(8,5))
plt.title("4ª Questão: Comparativo de dados faltantes antes e depois do preenchimento")
plt.ylabel("Quantidade de valores faltantes")
plt.show()





# 5ª questão

print('\n')
print(info(n))
n += 1
print("Boxplot mostrando a relação entre PESO faltante e IDADEMAE aberto em outra janela.\n")

plt.figure(figsize=(8,5))
sns.boxplot(data=df, x="peso_faltante", y="IDADEMAE")
plt.title("5ª Questão: Distribuição de IDADEMAE conforme PESO faltante ou não")
plt.xlabel("PESO faltante (True = faltante)")
plt.ylabel("Idade da mãe")
plt.show()

# Estatísticas descritivas
comparativo = df.groupby("peso_faltante")["IDADEMAE"].describe()
print("\nResumo estatístico de IDADEMAE conforme PESO faltante ou não:")
print(comparativo)
