from typing import List
from SRC.scheduler import Scheduler, GanttEntry
from SRC.proceso import Proceso

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