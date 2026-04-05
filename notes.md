Boas pr]aticas

plotar os instrumentos no dominio da frequencia

violino -> rico em harmonicos, ataque suave (energia distribuida em altas frequencias)
piano -> ataque percursivo nítido, decaimento longo (transiente forte)
clarinete -> harmonicos ímpares dominante (padrao espectral muito distinto dos outros)

eh bom pegar, dps q treinar, amostras de teste q classificaram corretamente e pq.



------------
PERGUNTAS INTERNAS


# Passo 1 (Pré-processamento)

-Oq é y?
y é o array com as amostras do sinal de áudio — cada valor representa a amplitude do sinal em um instante discreto de tempo.

-Pq utilizar sr=22050?
Pq o ouvido humano só consegue captar até 20KHz
e pelo teorema de nyquist. sr (frequencia de amostragem) > 2*f_max
quando nós chamamos o librosa.load e setamos o sr para esse valor, o librosa aplica um filtro anti-aliasing ao fazer o resample.

- Teorema de Nyquist
Para reconstruir um sinal sem aliasing, a taxa de amostragem deve ser estritamente maior que o dobro da maior frequência presente no sinal.
sr > 2 × f_max

-Pq normalizar amplitude?
Analogamente à equalização de histograma em PDI, que normaliza a distribuição de intensidades de uma imagem para remover variações de iluminação, a normalização de amplitude remove variações de dinâmica entre gravações, permitindo que o classificador foque nas características espectrais do timbre.

exemplos de variação: volume/intensidade ao longo do tempo.


# Passo 2 (Extração de Features)

- Centroide espectral = a frequência média ponderada pela magnitude.
centroide = Σ(frequência × magnitude) / Σ(magnitude)

O que ele captura fisicamente:

Som com muita energia nos agudos → centroide alto
Som com muita energia nos graves → centroide baixo

clarinete → harmônicos ímpares dominantes → centroide característico
violino   → rico em harmônicos altos      → centroide mais alto
piano     → amplo espectro                → centroide intermediário


- Spectral Bandwidth (Largura de Banda Espectral)
É a largura do espectro em torno do centroide — o quanto as frequências se dispersam em relação ao centro de massa.

O que ele captura fisicamente:

Espectro concentrado em poucas frequências → bandwidth baixo
Espectro espalhado por muitas frequências → bandwidth alto

- Spectral_contrast (Contraste Espectral)
É a diferença de intensidade entre os picos e os vales do espectro

pico
/\  /\/\
  \/
 vale

- Spectral Flux = Quanto o espectro muda de um frame para o outro.
Num cenário de visão computacional, seria como se fosse detecção de movimento entre frames 

O que ele captura fisicamente:

Onset de nota (quando o instrumento começa a tocar) → flux alto
Sinal estacionário (nota sustentada) → flux baixo

piano     → ataque percussivo forte → flux alto no onset, cai rápido
violino   → ataque gradual (arco)   → flux cresce devagar
clarinete → ataque de sopro         → flux intermediário

- Zero Crossing
Quantas vezes o sinal cruza y = 0

PLUS
- O que é escala mel?
É uma escala de frequência que imita a percepção auditiva humana.



# Passo 3 (Montar o dataset)

# Passo 4 (Treino e Validação)