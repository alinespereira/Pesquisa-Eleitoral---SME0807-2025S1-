# Pesquisa Eleitoral

Erro amostral: $B = 2\%$

Nível de significância: $\alpha = 5\%$

## Governador e Senador (por turno)

Plano: AASs
Tamanho da população
Tamanho da amostra

$Var(\hat{P}) = (1 - f)\frac{PQ}{n}$

$P(|\hat{P} - P| \le B) \approx 1 - \alpha$

$B = z_{\frac{\alpha}{2}} \cdot \sqrt{Var(\hat{P})}$

$\begin{align}
    Var(\hat{P}) &= (1 - f)\frac{S_N^2}{n} \\
    &= (1 - f) \frac{N}{N - 1} \frac{PQ}{n} \\
    &= \left(1 - \frac{n}{N}\right) \frac{N}{N - 1} \frac{PQ}{n} \\
    &= \frac{N - n}{N - 1} \frac{PQ}{n}
\end{align}$

Abordagem: conservativa $\left(PQ = \frac{1}{4}\right)$

Tamanho amostral:

$\begin{align}
    n &= \frac{N}{\frac{N-1}{PQ}\left(\frac{B}{z_{\alpha/2}}\right)^2 + 1}
\end{align}$

## Presidente (por turno)

Plano: AEpr + AASs
Estratos: estados
Tamanho da população
Tamanho da amostra
