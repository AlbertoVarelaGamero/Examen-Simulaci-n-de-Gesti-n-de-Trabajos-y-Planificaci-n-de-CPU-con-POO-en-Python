from typing import List, Tuple
from SRC.proceso import Proceso

class Metrics:
    @staticmethod
    def calcular_metricas(procesos: List[Proceso]) -> dict:
        if not procesos:
            return {
                'tiempo_respuesta_medio': 0,
                'tiempo_espera_medio': 0,
                'tiempo_retorno_medio': 0
            }

        tiempos_respuesta = []
        tiempos_espera = []
        tiempos_retorno = []

        for proceso in procesos:
            if proceso.tiempo_inicio is not None and proceso.tiempo_fin is not None:
                tiempo_respuesta = proceso.tiempo_inicio - proceso.tiempo_llegada
                tiempo_retorno = proceso.tiempo_fin - proceso.tiempo_llegada
                tiempo_espera = tiempo_retorno - proceso.duracion
                
                tiempos_respuesta.append(tiempo_respuesta)
                tiempos_espera.append(tiempo_espera)
                tiempos_retorno.append(tiempo_retorno)

        n = len(tiempos_respuesta)
        return {
            'tiempo_respuesta_medio': sum(tiempos_respuesta) / n if n > 0 else 0,
            'tiempo_espera_medio': sum(tiempos_espera) / n if n > 0 else 0,
            'tiempo_retorno_medio': sum(tiempos_retorno) / n if n > 0 else 0
        }