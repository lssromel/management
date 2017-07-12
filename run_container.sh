#!/bin/bash

# Variables
# $1 Nombre cliente
# $2 Nombre tabla
# $3 Nombre resultado e.j. prueba.html

# FALTA CORREGIR LA FORMA DE LIMPIAR DATOS DE LA BD
#docker create --name $1$2 -it procesado
#docker start $1$2
#docker exec ./workspace/Procesado/scripts/run_limpieza.sh $1 $2
#sudo docker stop $1$2
#sudo docker rm $1$2

docker create --name $1$2 -it procesado
docker start 
docker exec $1$2 sh scripts/run_procesado.sh $1 $2 
docker cp tmp:/workspace/Procesado/prueba.html /home/romel/prueba.html
docker stop $1$2
docker rm $1$2



