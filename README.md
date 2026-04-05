# Classificação de Instrumentos Musicais (Piano vs Violino vs Clarinete)

Projeto da disciplina de **Processamento Digital de Imagens (PDI)**, ministrada pelo professor **Leoanrdo**, desenvolvido pelos alunos **Adriel** e **Kamily**.

## Contexto do problema

Este trabalho propõe um sistema de classificação para três classes instrumentais:

- Piano
- Violino
- Clarinete

Embora o problema seja de áudio, a estratégia segue a lógica de PDI ao converter sinais unidimensionais em representações tempo-frequência tratadas como imagens (espectrogramas), permitindo o uso de técnicas clássicas de processamento e aprendizado supervisionado.

## Base de dados

Dataset utilizado:

- IRMAS Training Data (Kaggle): https://www.kaggle.com/datasets/urvishp80/irmas-training-data

## Fundamentação técnica

O pipeline é construído com base em conceitos fundamentais discutidos em aula:

- **Amostragem e discretização** do sinal de áudio
- **Análise no domínio da frequência** por Transformada Discreta de Fourier (DCT) e IDCT
- **Análise tempo-frequência** via STFT para gerar espectrogramas
- **Convolução** como operador central para extração de padrões locais
- Relação entre **resolução temporal vs resolução espectral** (efeito do tamanho de janela)
- Interpretação de fenômenos como **harmônicos**, **timbre**, energia espectral e distribuição de frequências

## Metodologia geral

1. Pré-processamento dos sinais (normalização e padronização de entrada).
2. Transformação para o domínio da frequência e construção de representações espectrais.
3. Extração/aprendizado de características com modelos de classificação, incluindo arquiteturas baseadas em **convolução (CNN)**.
4. Avaliação por métricas de classificação (ex.: acurácia, matriz de confusão, precisão e revocação por classe).

## Objetivo acadêmico do projeto

O foco principal não é apenas maximizar desempenho numérico, mas produzir uma explicação **matemática e física** para cada etapa do processamento e para cada resultado observado.

Assim, o trabalho enfatiza o entendimento do processo de decisão do modelo e a interpretação técnica dos resultados, em vez de tratar a classificação como uma caixa-preta.
