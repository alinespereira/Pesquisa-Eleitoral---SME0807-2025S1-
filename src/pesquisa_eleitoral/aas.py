from dataclasses import dataclass

import numpy as np
from scipy import stats


@dataclass
class AASs:
    erro_amostral: float
    significancia: float

    @property
    def z(self):
        return stats.norm.ppf(1 - self.significancia / 2)

    def tamanho_amostral(self, N: int, P: float = 1 / 2) -> int:
        Q = 1 - P
        erro_padrao = self.erro_amostral / self.z

        return np.ceil(N / ((N - 1) * erro_padrao**2 / (P * Q) + 1))
