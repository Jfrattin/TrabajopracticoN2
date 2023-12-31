class Paciente:
    def __init__(self, tiempo, nivel_riesgo):
        self.tiempo = tiempo
        self.nivel_riesgo = nivel_riesgo

    def __lt__(self, otro_paciente):
        if self.nivel_riesgo < otro_paciente.nivel_riesgo:
            return True
        elif self.nivel_riesgo == otro_paciente.nivel_riesgo:
            return self.tiempo > otro_paciente.tiempo
        else:
            return False
        
    def __gt__(self, otro_paciente):
        if self.nivel_riesgo > otro_paciente.nivel_riesgo:
            return True
        elif self.nivel_riesgo == otro_paciente.nivel_riesgo:
            print(self.tiempo )
            print(otro_paciente.tiempoself.tiempo )
            return self.tiempo > otro_paciente.tiempo
        else:
            return False

    def __str__(self):
        return f"Entrada: {self.tiempo},  Nivel de Riesgo: {self.nivel_riesgo}"

    def __gt__(self, otro_paciente):
        return self.nivel_riesgo > otro_paciente.nivel_riesgo



   