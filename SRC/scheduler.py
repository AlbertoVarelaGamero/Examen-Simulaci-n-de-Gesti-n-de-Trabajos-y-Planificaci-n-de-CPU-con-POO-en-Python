from abc import ABC, abstractmethod
from typing import List, Tuple
from SRC.proceso import Proceso

GanttEntry = Tuple[str, int, int]

class Scheduler(ABC):
    @abstractmethod
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        pass

class FCFSScheduler(Scheduler):
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        gantt = []
        tiempo_actual = 0
        for proceso in sorted(procesos, key=lambda p: p.tiempo_llegada):
            proceso.tiempo_inicio = tiempo_actual
            proceso.tiempo_fin = tiempo_actual + proceso.duracion
            gantt.append((proceso.pid, proceso.tiempo_inicio, proceso.tiempo_fin))
            tiempo_actual = proceso.tiempo_fin
        return gantt

class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum: int):
        if quantum <= 0:
            raise ValueError("Quantum debe ser positivo")
        self.quantum = quantum

    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        gantt = []
        tiempo_actual = 0
        cola = [p for p in procesos]
        for p in cola:
            p.tiempo_restante = p.duracion

        while cola:
            proceso = cola.pop(0)
            tiempo_ejecucion = min(self.quantum, proceso.tiempo_restante)
            
            if proceso.tiempo_inicio is None:
                proceso.tiempo_inicio = tiempo_actual
                
            gantt.append((proceso.pid, tiempo_actual, tiempo_actual + tiempo_ejecucion))
            proceso.tiempo_restante -= tiempo_ejecucion
            tiempo_actual += tiempo_ejecucion
            
            if proceso.tiempo_restante > 0:
                cola.append(proceso)
            else:
                proceso.tiempo_fin = tiempo_actual
                
        return gantt