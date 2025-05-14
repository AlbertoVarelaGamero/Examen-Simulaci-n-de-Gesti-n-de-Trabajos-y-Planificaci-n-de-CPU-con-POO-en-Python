import pytest
import os
from SRC.proceso import Proceso
from SRC.repositorio import RepositorioProcesos

def test_agregar_proceso():
    repo = RepositorioProcesos()
    proceso = Proceso("P1", 5, 1)
    repo.agregar_proceso(proceso)
    assert len(repo.listar_procesos()) == 1

def test_pid_duplicado():
    repo = RepositorioProcesos()
    repo.agregar_proceso(Proceso("P1", 5, 1))
    with pytest.raises(ValueError):
        repo.agregar_proceso(Proceso("P1", 3, 2))

def test_guardar_cargar_json(tmp_path):
    repo = RepositorioProcesos()
    repo.agregar_proceso(Proceso("P1", 5, 1))
    archivo = tmp_path / "test.json"
    repo.guardar_json(archivo)
    nuevo_repo = RepositorioProcesos()
    nuevo_repo.cargar_json(archivo)
    assert len(nuevo_repo.listar_procesos()) == 1