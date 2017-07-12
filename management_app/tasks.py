#management/tasks.py
from management.celery import app
import subprocess
 
@app.task
# falta agregar parametros desde la vista y arreglar la autenticacion
def Procesado_Datos():
    #self.update_state(state="PROGRESS", meta={'progress': "Limpiando los datos ..."})
    subprocess.call(['./run_container.sh',"renting","viajes"])

