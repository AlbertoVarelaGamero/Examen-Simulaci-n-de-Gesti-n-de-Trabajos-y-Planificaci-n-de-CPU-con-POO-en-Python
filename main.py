import gradio as gr
from SRC.proceso import Proceso
from SRC.repositorio import RepositorioProcesos
from SRC.fcfs_scheduler import FCFSScheduler
from SRC.round_robin_scheduler import RoundRobinScheduler
from SRC.metrics import Metrics

# Inicializar repositorio
repo = RepositorioProcesos()

def agregar_proceso(pid, duracion, prioridad):
    try:
        duracion = int(duracion)
        prioridad = int(prioridad)
        proceso = Proceso(pid, duracion, prioridad)
        repo.agregar_proceso(proceso)
        return "Proceso agregado exitosamente.", listar_procesos()
    except ValueError as e:
        return f"Error: {e}", listar_procesos()

def listar_procesos():
    procesos = repo.listar_procesos()
    if not procesos:
        return "No hay procesos registrados."
    return [[p.pid, p.duracion, p.prioridad] for p in procesos]

def ejecutar_fcfs():
    try:
        scheduler = FCFSScheduler()
        gantt = scheduler.planificar(repo.listar_procesos())
        metricas = Metrics.calcular_metricas(repo.listar_procesos())
        return f"Diagrama de Gantt: {gantt}\nMétricas: {metricas}", listar_procesos()
    except Exception as e:
        return f"Error: {e}", listar_procesos()

def ejecutar_round_robin(quantum):
    try:
        quantum = int(quantum)
        if quantum <= 0:
            raise ValueError("Quantum debe ser positivo")
        scheduler = RoundRobinScheduler(quantum)
        gantt = scheduler.planificar(repo.listar_procesos())
        metricas = Metrics.calcular_metricas(repo.listar_procesos())
        return f"Diagrama de Gantt: {gantt}\nMétricas: {metricas}", listar_procesos()
    except ValueError as e:
        return f"Error: {e}", listar_procesos()

def guardar_json():
    try:
        repo.guardar_json("procesos.json")
        return "Procesos guardados en JSON.", listar_procesos()
    except Exception as e:
        return f"Error: {e}", listar_procesos()

def cargar_json():
    try:
        repo.cargar_json("procesos.json")
        return "Procesos cargados desde JSON.", listar_procesos()
    except Exception as e:
        return f"Error: {e}", listar_procesos()

def guardar_csv():
    try:
        repo.guardar_csv("procesos.csv")
        return "Procesos guardados en CSV.", listar_procesos()
    except Exception as e:
        return f"Error: {e}", listar_procesos()

def cargar_csv():
    try:
        repo.cargar_csv("procesos.csv")
        return "Procesos cargados desde CSV.", listar_procesos()
    except Exception as e:
        return f"Error: {e}", listar_procesos()

# Crear interfaz Gradio
with gr.Blocks(title="Sistema de Planificación de Procesos") as demo:
    gr.Markdown("# Sistema de Planificación de Procesos")
    
    # Sección para agregar proceso
    gr.Markdown("## Agregar Proceso")
    with gr.Row():
        pid_input = gr.Textbox(label="PID")
        duracion_input = gr.Textbox(label="Duración")
        prioridad_input = gr.Textbox(label="Prioridad")
    agregar_btn = gr.Button("Agregar Proceso")
    agregar_output = gr.Textbox(label="Resultado")
    
    # Tabla de procesos
    gr.Markdown("## Lista de Procesos")
    procesos_table = gr.Dataframe(headers=["PID", "Duración", "Prioridad"], label="Procesos Registrados")
    
    # Sección para planificación
    gr.Markdown("## Planificación")
    with gr.Row():
        with gr.Column():
            fcfs_btn = gr.Button("Ejecutar FCFS")
            fcfs_output = gr.Textbox(label="Resultado FCFS")
        with gr.Column():
            quantum_input = gr.Textbox(label="Quantum")
            rr_btn = gr.Button("Ejecutar Round-Robin")
            rr_output = gr.Textbox(label="Resultado Round-Robin")
    
    # Sección para persistencia
    gr.Markdown("## Persistencia")
    with gr.Row():
        with gr.Column():
            guardar_json_btn = gr.Button("Guardar JSON")
            cargar_json_btn = gr.Button("Cargar JSON")
            json_output = gr.Textbox(label="Resultado JSON")
        with gr.Column():
            guardar_csv_btn = gr.Button("Guardar CSV")
            cargar_csv_btn = gr.Button("Cargar CSV")
            csv_output = gr.Textbox(label="Resultado CSV")

    # Conectar eventos
    agregar_btn.click(
        fn=agregar_proceso,
        inputs=[pid_input, duracion_input, prioridad_input],
        outputs=[agregar_output, procesos_table]
    )
    fcfs_btn.click(
        fn=ejecutar_fcfs,
        outputs=[fcfs_output, procesos_table]
    )
    rr_btn.click(
        fn=ejecutar_round_robin,
        inputs=quantum_input,
        outputs=[rr_output, procesos_table]
    )
    guardar_json_btn.click(
        fn=guardar_json,
        outputs=[json_output, procesos_table]
    )
    cargar_json_btn.click(
        fn=cargar_json,
        outputs=[json_output, procesos_table]
    )
    guardar_csv_btn.click(
        fn=guardar_csv,
        outputs=[csv_output, procesos_table]
    )
    cargar_csv_btn.click(
        fn=cargar_csv,
        outputs=[csv_output, procesos_table]
    )

if __name__ == "__main__":
    try:
        print("Iniciando la interfaz Gradio...")
        demo.launch(server_name="127.0.0.1", server_port=7860)
        print("Interfaz Gradio iniciada con éxito.")
    except Exception as e:
        print(f"Error al iniciar Gradio: {e}")