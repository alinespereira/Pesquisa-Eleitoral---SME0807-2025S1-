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

### Tamanho da amostra

$\begin{align}
\operatorname{Var}(P_{es})
    &= \operatorname{Var}\left(\sum_{h=1}^H W_h P_h\right) \\
    &= \sum_{h=1}^H W_h^2 \operatorname{Var}(P_h) \\
    &= \sum_{h=1}^H W_h^2 (1 - f_h)
        \frac{N_h}{N_h - 1}
        \frac{P_h Q_h}{n_h} \\
B &= z_{\alpha/2} \sqrt{\operatorname{Var}(P_{es})} \\
\therefore n &=
\frac{N z_{\alpha/2}^2 \sum_{h=1}^H \frac{N_h^2 P_h Q_h}{N_h - 1}}
{B^2 N^2 + z_{\alpha/2}^2 \sum_{h=1}^H \frac{N_h^2 P_h Q_h}{N_h - 1}} \\
&= \frac{N}
{\left(\frac{B}{z_{\alpha/2}}\right)^2
    \frac{N^2}{\sum_{h=1}^H \frac{N_h^2 P_h Q_h}{N_h - 1}} + 1} \\
&= \frac{N}
{\left(\frac{B}{z_{\alpha/2}}\right)^2
    \frac{1}{\sum_{h=1}^H \frac{W_h^2 P_h Q_h}{N_h - 1}} + 1}
\end{align}$
