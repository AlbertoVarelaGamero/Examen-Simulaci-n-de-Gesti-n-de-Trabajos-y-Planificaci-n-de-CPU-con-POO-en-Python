from SRC.proceso import Proceso
from SRC.repositorio import RepositorioProcesos
from SRC.scheduler import FCFSScheduler, RoundRobinScheduler
from SRC.metrics import Metrics

def mostrar_menu():
    print("\nSistema de Planificación de Procesos")
    print("1. Agregar proceso")
    print("2. Listar procesos")
    print("3. Ejecutar FCFS")
    print("4. Ejecutar Round-Robin")
    print("5. Guardar procesos (JSON)")
    print("6. Cargar procesos (JSON)")
    print("7. Guardar procesos (CSV)")
    print("8. Cargar procesos (CSV)")
    print("9. Salir")

def main():
    repo = RepositorioProcesos()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        try:
            if opcion == "1":
                pid = input("PID: ")
                duracion = int(input("Duración: "))
                prioridad = int(input("Prioridad: "))
                proceso = Proceso(pid, duracion, prioridad)
                repo.agregar_proceso(proceso)
                print("Proceso agregado.")
                
            elif opcion == "2":
                procesos = repo.listar_procesos()
                for p in procesos:
                    print(f"PID: {p.pid}, Duración: {p.duracion}, Prioridad: {p.prioridad}")
                    
            elif opcion == "3":
                scheduler = FCFSScheduler()
                gantt = scheduler.planificar(repo.listar_procesos())
                print("Diagrama de Gantt:", gantt)
                metricas = Metrics.calcular_metricas(repo.listar_procesos())
                print("Métricas:", metricas)
                
            elif opcion == "4":
                quantum = int(input("Quantum: "))
                scheduler = RoundRobinScheduler(quantum)
                gantt = scheduler.planificar(repo.listar_procesos())
                print("Diagrama de Gantt:", gantt)
                metricas = Metrics.calcular_metricas(repo.listar_procesos())
                print("Métricas:", metricas)
                
            elif opcion == "5":
                repo.guardar_json("procesos.json")
                print("Procesos guardados en JSON.")
                
            elif opcion == "6":
                repo.cargar_json("procesos.json")
                print("Procesos cargados desde JSON.")
                
            elif opcion == "7":
                repo.guardar_csv("procesos.csv")
                print("Procesos guardados en CSV.")
                
            elif opcion == "8":
                repo.cargar_csv("procesos.csv")
                print("Procesos cargados desde CSV.")
                
            elif opcion == "9":
                print("Saliendo...")
                break
                
            else:
                print("Opción inválida.")
                
        except ValueError as e:
            print(f"Error: {e}")
            
if __name__ == "__main__":
    main()