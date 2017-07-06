#!/bin/bash
docker create --name tmp -it procesado
docker start tmp

sudo docker cp /home/romel/management/task_scripts/renting/viajes/prueba.py tmp:/workspace/Procesado/prueba.py

sudo docker exec tmp python /workspace/Procesado/prueba.py

sudo docker cp tmp:/workspace/Procesado/prueba.html /home/romel/management/tmp/prueba.html

sudo docker stop tmp
sudo docker rm tmp
sudo docker cp /home/romel/management/tmp/prueba.html result_container:/workspace/result_app/web/templates/web/data/renting/consultoria.html
