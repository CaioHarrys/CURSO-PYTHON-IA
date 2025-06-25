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
