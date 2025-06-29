# 📊 Relatório de Análise Exploratória dos Alunos

Este relatório apresenta as principais descobertas da análise exploratória realizada com um conjunto de 100 alunos contendo informações como idade, curso, semestre, nota final, faltas e gênero.

## 📌 Informações Gerais
- Total de alunos analisados: **100**
- Cursos incluídos: ADS, Arquitetura, Direito, Engenharia, Medicina
- Gêneros representados: Masculino (M) e Feminino (F)
- Nota de corte utilizada para aprovação: **6.0**

## 📈 Estatísticas Relevantes
- **Curso com maior média de nota:** Direito (7.87)
- **Curso com maior média de faltas:** Direito (16.18)
- **Gênero com maior média de faltas:** Feminino (15.27 faltas)
- **Semestres com mais faltas:** 8º e 9º semestres (>19 faltas)
- **Faixa etária predominante:** 23 a 30 anos
- **Correlação entre faltas e nota:** Negativa, como esperado (mais faltas → tendência a nota mais baixa)

## 📊 Gráficos e Visualizações
### Boxplot Nota por Curso
![Boxplot Nota por Curso](./boxplot_nota_por_curso.png)

### Faltas por Semestre
![Faltas por Semestre](./barplot_faltas_por_semestre.png)

### Faltas vs Nota Final (Dispersão)
![Faltas vs Nota Final (Dispersão)](./scatter_faltas_nota.png)

### Mapa de Correlação
![Mapa de Correlação](./heatmap_correlacoes.png)

### Nota por Situação
![Nota por Situação](./boxplot_situacao_nota.png)

### Radar de Cursos
![Radar de Cursos](./radar_chart_cursos.png)

### Violin por Curso
![Violin por Curso](./violinplot_nota_por_curso.png)

### Violin por Gênero
![Violin por Gênero](./violinplot_nota_por_genero.png)

### Violin Curso x Semestre
![Violin Curso x Semestre](./violinplot_nota_por_curso_semestre.png)

### Violin Gênero x Semestre
![Violin Gênero x Semestre](./violinplot_nota_por_genero_semestre.png)

### Violin Faixa Etária x Situação
![Violin Faixa Etária x Situação](./violinplot_nota_por_faixa_situacao.png)

### Violin Curso x Situação
![Violin Curso x Situação](./violinplot_nota_por_curso_situacao.png)

## 🔍 Insights Importantes
- Apesar de alunos reprovados terem notas baixas, a média de faltas entre eles foi **menor** que entre os aprovados.
- A distribuição das notas por curso e por gênero não apresenta grandes distorções, indicando equilíbrio de desempenho.
- A análise por faixa etária mostra que alunos entre 23 e 30 anos concentram maior parte das reprovações.
- Os gráficos de violino e radar ajudaram a visualizar claramente a densidade, variações e padrões por grupo.

---
### Feito por Caio Harrys