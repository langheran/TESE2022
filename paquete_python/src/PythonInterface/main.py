import os
import pandas as pd

class HolaTESE:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.alumnos_df = pd.read_csv(
            os.path.join(
                os.path.dirname(__file__),
                'data/alumnos.csv'
            )
        )
    
    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre

    def __iter__(self):
        self.n = 0
        self.alumnos = self.alumnos_df[
            self.alumnos_df.apply(
                lambda x:
                len(
                    [
                        1 for c in self.alumnos_df.columns
                        if self.nombre in x[c]
                    ]
                ) > 0,
                axis=1
            )
        ].reset_index(drop=True).to_dict('records')
        return self

    def __next__(self):
        if self.n < len(self.alumnos) and len(self.alumnos):
            result = self.alumnos[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration
