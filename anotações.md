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

## 📅 Aula: 08/05

### 📌 Conceitos

- **IQR (Intervalo Interquartil):** Região com maior concentração de dados.
- **Mediana:** Representa o **2º quartil (50%)** dos dados.
- **Outliers:** Valores fora do padrão esperado.
