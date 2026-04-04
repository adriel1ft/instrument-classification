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