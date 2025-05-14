import pytest
from SRC.proceso import Proceso
from SRC.fcfs_scheduler import FCFSScheduler
from SRC.round_robin_scheduler import RoundRobinScheduler

def test_fcfs_scheduler():
    procesos = [
        Proceso("P1", 3, 1),
        Proceso("P2", 2, 2)
    ]
    scheduler = FCFSScheduler()
    gantt = scheduler.planificar(procesos)
    assert gantt == [("P1", 0, 3), ("P2", 3, 5)]

def test_round_robin_scheduler():
    procesos = [
        Proceso("P1", 3, 1),
        Proceso("P2", 2, 2)
    ]
    scheduler = RoundRobinScheduler(quantum=1)
    gantt = scheduler.planificar(procesos)
    assert len(gantt) == 5  # 3 + 2 unidades de tiempo divididas en quantum de 1