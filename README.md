# 📊 Análise de Dados de Mortalidade (SIM 2024)

Este projeto realiza uma análise exploratória dos dados públicos do **Sistema de Informação sobre Mortalidade (SIM)** referentes ao ano de 2024, disponibilizados pelo **Ministério da Saúde (DATASUS)**.  

O objetivo é avaliar a **qualidade e completude** dos registros de óbitos, com foco em variáveis como **idade, ocupação, acidentes de trabalho, escolaridade, sexo, raça/cor e dados maternos**.  
As análises foram desenvolvidas em **Python**, utilizando as bibliotecas **Pandas**, **Matplotlib** e **Seaborn**.

---

## 📁 Estrutura do Projeto

```
📂 top4/
├── SIM2024.csv # Base de dados bruta (extraída do DATASUS)
├── Dicionario_SIM_2025.pdf # Documento oficial com descrição das variáveis
├── main.py # Script principal com as análises
├── Analise_SIM2024.ipynb # Notebook com código e gráficos integrados
└── README.md # Este arquivo
```

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.12+**
- **Pandas** → manipulação e limpeza de dados  
- **Matplotlib** → visualização gráfica  
- **Seaborn** → gráficos estatísticos e comparativos  
- **Jupyter Notebook** (opcional) → execução interativa  

---

## 📦 Instalação

Clone o repositório e instale as dependências necessárias:

```bash
git clone https://github.com/<seu-usuario>/sim2024-analysis.git
cd sim2024-analysis
pip install pandas matplotlib seaborn
```

▶️ Execução
Execute diretamente no terminal:

```
python main.py
```
O script irá:
  - Ler a base SIM2024.csv
  - Exibir estatísticas gerais e metadados
  - Calcular percentuais de dados faltantes
  - Gerar gráficos abertos em novas janelas


📚 Questões Respondidas:

1️⃣ Estrutura e contexto da base
A base SIM (Sistema de Informação sobre Mortalidade) é gerida pelo Ministério da Saúde e reúne registros de óbitos declarados no Brasil.
Cada linha representa uma Declaração de Óbito (DO), com informações sobre o falecido, a mãe (em casos de óbitos fetais/infantis) e as circunstâncias da morte.

Principais variáveis segundo o Dicionário SIM 2025:

TIPOBITO: tipo de óbito (fetal ou não fetal)

IDADE: codificação da idade e unidade de tempo

SEXO: sexo biológico (1=Masculino, 2=Feminino, 9=Ignorado)

RACACOR: cor/raça autodeclarada (1=Branca, 2=Preta, 3=Amarela, 4=Parda, 5=Indígena)

ESC: escolaridade (anos de estudo)

OCUP: ocupação habitual segundo a CBO 2002

ACIDTRAB: indica se o óbito ocorreu por acidente de trabalho (1=Sim, 2=Não)

PESO: peso ao nascer (para óbitos fetais/neonatais)

IDADEMAE: idade da mãe em anos

CAUSABAS: causa básica segundo a CID-10

Esses dados são amplamente usados em estudos epidemiológicos, planejamento de políticas públicas e vigilância de doenças.



2️⃣ Percentual de dados faltantes
O código calcula a porcentagem de valores ausentes em cada campo e plota um gráfico de barras com esses percentuais.

Conclusões:

Campos como PESO e IDADEMAE tendem a ter maior proporção de valores ausentes.

Campos obrigatórios, como IDADE e TIPOBITO, possuem completude quase total.

Isso impacta diretamente análises específicas, como causas de morte por faixa etária ou peso ao nascer.



3️⃣ Relação entre IDADE, OCUP e ACIDTRAB
Foram analisadas as taxas de valores ausentes em cada um desses campos:

Campo	Percentual de Faltantes
IDADE	0%
OCUP	~13%
ACIDTRAB	~96%

Os resultados mostram que:

OCUP e ACIDTRAB estão ausentes, principalmente, em registros de crianças e idosos, que não exercem ocupação formal.

IDADE é obrigatória para quase todos os tipos de óbito, por isso está completa.

➡️ Conclusão: há uma relação lógica e contextual entre os campos faltantes, não um erro de coleta.
Exemplo: crianças não têm ocupação nem acidentes de trabalho registrados.



4️⃣ Preenchimento de dados faltantes
Foram imputados valores nos seguintes campos:

Campo	Método Utilizado	Justificativa
SEXO	Moda	Valor mais frequente é estável e representa a maioria dos casos
RACACOR	Moda	Mantém coerência com a distribuição predominante
ESC	Moda	Evita distorção em faixas de escolaridade
PESO	Média	Preserva a média geral sem enviesar análises contínuas

Após o preenchimento, foi plotado um gráfico de barras comparando a quantidade de valores faltantes antes e depois da imputação, mostrando redução total em todos os campos tratados.



5️⃣ Comparação entre PESO e IDADEMAE
A análise avalia se há padrão entre ausência de PESO e idade da mãe (IDADEMAE).
Foi criado um boxplot para comparar as distribuições de IDADEMAE conforme o campo PESO estar ausente ou não.

Resultados:

Registros com PESO ausente tendem a se concentrar entre mães mais jovens (adolescentes), o que pode indicar subnotificação em determinados grupos.

Onde não há diferença significativa, a ausência pode ser aleatória (MCAR), sem viés sistemático.

📊 Gráficos Gerados
- Gráfico 1: Percentual de dados faltantes por variável

- Gráfico 2: Comparativo de dados faltantes antes e depois da imputação

- Gráfico 3: Boxplot de IDADEMAE conforme presença de PESO

🧠 Metodologia
- Leitura dos dados brutos em formato .csv
- Cálculo e visualização de valores faltantes (isnull())
- Interpretação contextual com base no Dicionário SIM 2025
- Preenchimento de campos com métodos estatísticos simples (média/moda)
- Comparação gráfica antes e depois da imputação
- Análise da relação entre variáveis demográficas e completude de dados



👨‍💻 Autor

Arlen Ferreira da Silva Filho
Curso: Sistemas de Informação – Centro de Informática (CIn/UFPE)
Projeto acadêmico de Análise de Dados – Tópicos avançados em Sistemas de Informação 4 - 2025
