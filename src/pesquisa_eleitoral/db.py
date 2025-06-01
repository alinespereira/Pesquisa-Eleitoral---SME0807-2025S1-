from typing import TypedDict
import pandas as pd


class Stats(TypedDict):
    nome: str
    votos: int

def generate_population(stats: Stats, estado: str) -> pd.DataFrame:
    pd.DataFrame({
        "nome": [
            candidato
            for candidato, votos in stats.items()
            for _ in range(votos)
        ],
        "estado": [
            estado
            for _, votos in stats.items()
            for _ in range(votos)
        ]
    })
