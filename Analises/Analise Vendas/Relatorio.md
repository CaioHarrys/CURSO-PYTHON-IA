#  Análise Exploratória de Dados (EDA)

## Importação de Bibliotecas e Dataset

- **Bibliotecas**: `pandas`, `numpy`, `matplotlib`, `seaborn`.
- **Carregamento** do CSV com separador `;`.

---

##  Visão Geral do Dataset

- Verificação de colunas, tipos de dados, primeiras e últimas linhas.
- Checagem da quantidade de linhas e colunas.

---

##  Tratamento de Dados Faltantes

- Identificação de valores ausentes.
- Remoção de linhas com `NaN`.

---

##  Estatísticas Descritivas

- Resumo estatístico das variáveis numéricas e categóricas com `.describe()`.

---

##  Visualizações Numéricas

- Histogramas por coluna.
- Boxplots para detectar outliers.

---

##  Variáveis Categóricas

- Contagem de frequências por categoria.

---

##  Mapa de Correlação

- Análise de correlação entre variáveis numéricas.

---

##  Relações entre Variáveis

- `pairplot` para explorar padrões e possíveis clusters.

---

##  Informações que Conseguimos Levantar

##  Categorias de Produto Mais Vendidas

- As categorias com maior número de registros foram:
  - **Roupas**
  - **Beleza**
- Outras categorias como **Eletrônicos** e **Casa** aparecem com menor frequência.

- Essa informação foi obtida com `value_counts()` na coluna `Categoria_Produto`.

---

##  Variação de Valor Total por Quantidade

- A maior parte dos pedidos apresenta **valores baixos e quantidades pequenas**.
- Existe uma **tendência crescente entre `Quantidade` e `Valor_Total`**.
- A relação faz sentido: mais itens = pedido mais caro.

---

##  Outliers em Valores e Quantidades

- Foram detectados **outliers** em:
  - `Valor_Total`
  - `Quantidade`
- Os gráficos de boxplot revelam **valores muito acima do esperado**.
- Pode indicar:
  - Pedidos legítimos mas fora do padrão
  - Erros de cadastro
  - Compras empresariais ou atípicas

---

##  Correlações Entre Variáveis

- O **heatmap de correlação** mostrou:
  - Correlação **positiva entre `Quantidade` e `Valor_Total`**
- Outras variáveis numéricas não apresentaram correlações relevantes.

---

##  Distribuições de Variáveis

### Numéricas:
- `Valor_Total` e `Quantidade` têm **distribuições assimétricas**.
- A maior parte dos valores está concentrada em faixas baixas.
- Há uma **cauda longa com poucos pedidos muito altos**.

### Categóricas:
- `Categoria_Produto` é **desbalanceada**, com algumas categorias dominando.

---

##  Ausência de Dados

- A coluna `Data_Compra` tinha **datas inválidas** como `2024-02-30`.
- Foram convertidas em `NaT` e **as linhas foram removidas** com `dropna()`.
- Após isso, a base ficou limpa para análises temporais e visuais.

---