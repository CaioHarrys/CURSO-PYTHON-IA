✅ Etapas da Análise Exploratória em Python
# 1. 📦 Instalar e importar bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Estilo de gráficos
sns.set(style="whitegrid")
# 2. 📂 Carregar o CSV
df = pd.read_csv("seuarquivo.csv")
# 3. 🔍 Visão geral do dataset
df.shape               # Linhas e colunas
df.columns             # Nome das colunas
df.dtypes              # Tipos de dados
df.info()              # Info geral
df.head()              # Primeiras linhas
# 4. 🧼 Verificação e tratamento de dados faltantes
df.isnull().sum()                # Contagem de valores nulos
df.dropna(inplace=True)          # (Exemplo) remove linhas com valores nulos
# 5. 📊 Estatísticas descritivas
df.describe(include='all')       # Estatísticas gerais (para todos os tipos de dados)
# 6. 🔢 Análise de variáveis numéricas
df.select_dtypes(include='number').hist(figsize=(15, 10), bins=30)
plt.tight_layout()
plt.show()
# 7. 🔠 Análise de variáveis categóricas
for col in df.select_dtypes(include='object'):
    print(df[col].value_counts())
    print("-" * 40)
# 8. 📉 Correlações
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Mapa de Correlação")
plt.show()
# 9. 📌 Outliers (usando boxplots)
for col in df.select_dtypes(include='number'):
    sns.boxplot(data=df[col])
    plt.title(f"Boxplot de {col}")
    plt.show()
# 10. 📈 Relacionamentos entre variáveis
sns.pairplot(df.select_dtypes(include='number'))
plt.show()