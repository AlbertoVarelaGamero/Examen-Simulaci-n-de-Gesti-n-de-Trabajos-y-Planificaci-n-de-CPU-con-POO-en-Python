from typing import List
from SRC.scheduler import Scheduler, GanttEntry
from SRC.proceso import Proceso

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