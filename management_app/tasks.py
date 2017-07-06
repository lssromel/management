#management/tasks.py
from management.celery import app
import subprocess
 
@app.task
def Procesado_Datos():
    #self.update_state(state="PROGRESS", meta={'progress': "Limpiando los datos ..."})
    subprocess.call(['./task_scripts/limpieza.sh'])
    #self.update_state(state="PROGRESS", meta={'progress': "Preprocesando datos..."})
    subprocess.call(['./task_scripts/procesado.sh'])
    #self.update_state(state="PROGRESS", meta={'progress': "Visualizacion lista..."})
    
