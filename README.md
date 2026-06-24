# 🌳 Help Desk Priority Queue (BST)

Projeto final desenvolvido para a disciplina de Estruturas de Dados. Este repositório contém a implementação de um sistema interativo de **Help Desk**, onde a fila de chamados é gerenciada por uma **Árvore Binária de Busca (Binary Search Tree - BST)** construída do zero em Python.

## 🎯 O Desafio
Em vez de utilizar as listas convencionais do Python (`list` ou estruturas prontas de `queue`), o objetivo do projeto foi aplicar os conceitos matemáticos e algorítmicos de Árvores Binárias para criar uma **Fila de Prioridade** customizada. 

O sistema organiza os chamados automaticamente no momento da inserção, garantindo que o ticket com a maior urgência seja sempre o próximo a ser resolvido.

## ✨ Funcionalidades e Aprendizados Técnicos

* **Auto-organização (Inserção):** O algoritmo aloca chamados de menor prioridade à esquerda e de maior prioridade à direita, proporcionando um tempo de busca eficiente.
* **Lógica Completa de Deleção:** A parte mais complexa da estrutura. Implementação dos 3 cenários de remoção para resolver um chamado sem quebrar a árvore:
  1. Remoção de nó folha (0 filhos).
  2. Remoção de nó com 1 filho (reconexão direta).
  3. Remoção de nó com 2 filhos (busca pelo menor valor da subárvore à direita, o "nó sucessor", para substituição).
* **Travessia In-Order Inversa:** Criação de um método de leitura customizado que percorre a árvore da Direita -> Raiz -> Esquerda, permitindo imprimir a fila no terminal de forma perfeitamente decrescente (do mais urgente para o menos urgente).

## 🚀 Como executar o projeto

Certifique-se de ter o [Python](https://www.python.org/) instalado em sua máquina (versão 3.6 ou superior recomendada).

1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
