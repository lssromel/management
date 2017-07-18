#management/tasks.py
from management.celery import app
import subprocess
 
@app.task
# falta agregar parametros desde la vista y arreglar la autenticacion
def run_sh(directory):
    subprocess.call(['./home/romel/management/tmp/run_container.sh'])
    #handle_uploaded_file(f,"/workspace/management_app/tmp/run_container.sh")

    #subprocess.call(['/workspace/management_app/tmp/run_container.sh'])
    return directory




def handle_uploaded_file(f,ruta):
    with open(ruta, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return "archivo Catgado"

def up_file_start_task(f):
    directory ="/home/romel/management/tmp/run_container.sh"
    a=handle_uploaded_file(f,directory)
    result=run_sh.delay(directory)
    return result

