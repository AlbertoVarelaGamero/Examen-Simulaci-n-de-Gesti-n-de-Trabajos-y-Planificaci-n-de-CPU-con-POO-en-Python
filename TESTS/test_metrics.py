import pytest
from SRC.proceso import Proceso
from SRC.metrics import Metrics

def test_calcular_metricas():
    procesos = [
        Proceso("P1", 3, 1, tiempo_llegada=0, tiempo_inicio=0, tiempo_fin=3),
        Proceso("P2", 2, 2, tiempo_llegada=0, tiempo_inicio=3, tiempo_fin=5)
    ]
    metricas = Metrics.calcular_metricas(procesos)
    assert metricas['tiempo_respuesta_medio'] == 1.5
    assert metricas['tiempo_espera_medio'] == 0.5
    assert metricas['tiempo_retorno_medio'] == 4