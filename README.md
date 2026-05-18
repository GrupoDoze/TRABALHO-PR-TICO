# Sistema de Recomendação de Filmes

Sistema simples de recomendação de filmes desenvolvido em Python, utilizando métricas de similaridade para sugerir filmes semelhantes com base em tags e géneros.

## 📚 Sobre o Projeto

Este projeto foi desenvolvido como Trabalho Prático 1.9 da disciplina de Linguagem de Programação, no curso de Engenharia Informática da Universidade Kimpa Vita.

O sistema implementa duas abordagens de recomendação:

* Similaridade de Jaccard
* Similaridade de Cosseno

O objetivo é identificar filmes semelhantes com base nas tags associadas a cada filme.

---

## 👥 Integrantes do Grupo

* Rosa Sozinho Garcia
* António Lopes Tamba
* Jeremias Manuel
* Maria David Kiala
* Feliz Miguel

**Turma:** 101
**Período:** Manhã
**Ano:** 3º

**Docente:** Moyo Kanivengidio

---

## 🚀 Funcionalidades

* Catálogo com 15 filmes
* Sistema de recomendação baseado em tags
* Cálculo de Similaridade de Jaccard
* Cálculo de Similaridade de Cosseno
* Exibição formatada das recomendações
* Comparação entre métricas de similaridade

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Biblioteca padrão `math`

O projeto não utiliza bibliotecas externas.

---

## 📂 Estrutura do Projeto

```bash
📦 sistema-recomendacao
 ┣ 📜 sistema_recomendacao.py
 ┣ 📜 README.md
 ┗ 📜 Relatorio_TP1_9_Sistema_Recomendacao.pdf
```

---

## ▶️ Como Executar

### 1. Instalar Python

Baixe e instale o Python:

[Python Oficial](https://www.python.org/downloads/?utm_source=chatgpt.com)

---

### 2. Executar o Projeto

Abra o terminal na pasta do projeto e execute:

```bash
python sistema_recomendacao.py
```

---

## 📊 Exemplo de Saída

```bash
=======================================================
   SISTEMA DE RECOMENDAÇÃO DE FILMES
=======================================================

Filme de referência : Inception
Método              : Jaccard

1. The Dark Knight        Similaridade: 0.4286
2. The Matrix             Similaridade: 0.4286
3. Parasite               Similaridade: 0.4286
4. Interstellar           Similaridade: 0.2500
5. Avengers: Endgame      Similaridade: 0.2500
```

---

## 🧠 Métricas Utilizadas

### Similaridade de Jaccard

Mede a relação entre interseção e união de conjuntos.

J(A,B)=\frac{|A \cap B|}{|A \cup B|}

---

### Similaridade de Cosseno

Mede o ângulo entre dois vetores.

\cos(\theta)=\frac{A\cdot B}{|A||B|}

---

## 🎬 Filmes Disponíveis

* Inception
* Interstellar
* The Dark Knight
* Avengers: Endgame
* The Matrix
* Forrest Gump
* The Shawshank Redemption
* Pulp Fiction
* The Godfather
* Toy Story
* Spirited Away
* Parasite
* Gladiator
* The Lion King
* Doctor Strange

---

## 📖 Objetivos do Trabalho

* Aplicar estruturas de dados em Python
* Trabalhar com conjuntos (`set`) e dicionários
* Implementar algoritmos de similaridade
* Simular um sistema de recomendação simples

---

## 📌 Conclusão

O projeto demonstrou de forma prática como funcionam sistemas básicos de recomendação utilizados em plataformas modernas como:

* Netflix
* Spotify
* Amazon

A implementação permitiu compreender conceitos fundamentais de recomendação baseada em similaridade e manipulação de dados em Python.

---

## 📚 Referências

* [Documentação Python](https://docs.python.org/3/?utm_source=chatgpt.com)
* Mining of Massive Datasets — Jure Leskovec
* Recommender Systems Handbook — Francesco Ricci

---

## 📄 Licença

Projeto académico desenvolvido para fins educativos.
