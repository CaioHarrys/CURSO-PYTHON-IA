# 📚 Anotações de Estudo - Data Analysis com Python

## 🔍 Pesquisas Recomendadas

### Bibliotecas:
- `Seaborn`
- `Pandas`
- `Matplotlib`

### Tipos de Gráficos:
- Histograma
- Boxplot
- Dispersão
- Barras
- Linhas

### Outros Recursos:
- [PyPI.org](https://pypi.org) — Site oficial para bibliotecas Python

## 📘 Termos Estatísticos Comuns

- **Média**
- **Mediana**
- **Moda**
- **Estatísticas descritivas**:
  - `count`, `min`, `max`

### Anotações Extras:
- **Quartil**: Divide os dados em quatro partes
- **Interquartil (IQR)**: Intervalos de 25%, 50%, 75%
- **Normalização**: Colocar dados em uma mesma escala (ex: conversão de tipos)

---

## 📅 Aula: 30/04

**Objetivos de Análise:**
- Nota média por curso
- Quantidade de alunos (homens e mulheres) por curso
- Nota média por gênero
- Média de semestre por curso
- Idade média por curso
- Média de idade por semestre

---

## 📅 Aula: 05/05

**Tratamentos de Dados:**
- Dados nulos (poucos): excluir
- Outliers: tratar com **mediana**
- Distribuição normal: usar **média**
- Variáveis categóricas: tratar com **moda**

---

## 📅 Aula: 07/05

### 🧠 Mapeamentos:

```python
mapeamento_genero = {'Masculino': 0, 'Feminino': 1, 'Outro': 2}
mapeamento_uf = {'BA': 10, 'RS': 11, 'SC': 12, 'DF': 13, 'PE': 14, 'PR': 15, 'CE': 16, 'RJ': 17, 'SP': 18, 'MG': 19}
mapeamento_formação = {
    'Tecnólogo': 20, 'Ensino Médio': 21, 'Graduação': 22,
    'Mestrado': 23, 'Doutorado': 24, 'Não informado': 25
}
mapeamento_area_atuação = {
    'Tecnologia': 30, 'Recursos Humanos': 31, 'Administração': 32, 
    'Financeiro': 33, 'Marketing': 34, 'Educação ': 35, 
    'Engenharia ': 36, 'Saúde': 37, 'Não informado': 38
}
mapeamento_idioma = {
    'Nenhum': 40, 'Alemão': 41, 'Francês': 42, 
    'Inglês': 43, 'Espanhol': 44
}

# 📄 Relatório de Análise

## 📁 Dataset: `candidatos_tecnologia`

- **Entradas:** 1000
- **Colunas:** 17
  - 10 colunas do tipo `object`
  - 6 colunas do tipo `float`
  - 1 coluna do tipo `int64`

### 📌 Observações Iniciais
- Séries não normalizadas.
- Datas armazenadas como `object`.
- Necessidade de renomear e padronizar colunas.

---

## 📊 Análises Visuais

### 📍 UF
- Mais candidatos da **Bahia**.
- Menor número de candidatos de **Minas Gerais**.

### 🌐 Idioma
- Maioria **não fala idioma estrangeiro**.
- Em seguida: **Alemão**, **Francês**, **Inglês** e **Espanhol**.

### ⚧️ Gênero
- Leve maioria **masculina**.
- Distribuição relativamente equilibrada entre os gêneros.

### 📈 Status de Contratação
- **72.4%** não contratados.
- **27.6%** contratados.

### ♿ PCD
- Apenas **5%** dos candidatos se declararam PCD.

### 🎓 Formação
- Tecnólogo: **21.6%**
- Ensino Médio: **20.3%**
- Graduação: **19.9%**
- Mestrado: **19.4%**
- Doutorado: **18.8%**

### 🧑‍💼 Área de Atuação
- Maioria atua na área de **Tecnologia**.
- Menor número de candidatos na área da **Saúde**.
- Cerca de **290** candidatos **não informaram**.

### 🕒 Experiência
- A maioria possui entre **4 e 6 anos** de atuação.

---

## 🔧 Tratamento de Dados

### 🔄 Ações realizadas:
- Renomeadas as colunas dos **3 datasets** e unificados em um único `DataFrame`.
- Corrigidos dados nulos e convertidos tipos.

### 🧹 Correções por tipo:

| 🧭 Colunas com Moda                          | 🧮 Colunas com Média                                         | 🧷 Colunas com Mediana |
|---------------------------------------------|-------------------------------------------------------------|-------------------------|
| `uf`, `idioma`, `pcd`, `status_contratação`, `genero`, `disponivel_viagens`, `disponivel_mudança` | `salario_vaga`, `pretenção_salarial`, `anos_experiencia`, `certificações` | `idade`                |

- Coluna `data_inscricao` convertida de `object` para `datetime`.
- Coluna `nome` considerada **não relevante** para análise.
- Adicionados valores **"Não informado"** para `formação` e `área de atuação`.

---

## 📅 Aula: 08/05

### 📌 Conceitos

- **IQR (Intervalo Interquartil):** Região com maior concentração de dados.
- **Mediana:** Representa o **2º quartil (50%)** dos dados.
- **Outliers:** Valores fora do padrão esperado.
