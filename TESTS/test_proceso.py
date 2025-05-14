import pytest
from SRC.proceso import Proceso

def test_crear_proceso_valido():
    proceso = Proceso("P1", 5, 1)
    assert proceso.pid == "P1"
    assert proceso.duracion == 5
    assert proceso.prioridad == 1
    assert proceso.tiempo_restante == 5

def test_proceso_pid_invalido():
    with pytest.raises(ValueError):
        Proceso("", 5, 1)

def test_proceso_duracion_invalida():
    with pytest.raises(ValueError):
        Proceso("P1", 0, 1)