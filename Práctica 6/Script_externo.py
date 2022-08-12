#librerias nesesarias
import sim
import numpy as np
import time
#Establecer la conexión
def connect(port):
# Establece la conexión a CoppeliaSim
# port debe coincidir con el puerto de conexión en CoppeliaSim
# retorna el número de cliente o -1 si no puede establecer conexión
    sim.simxFinish(-1) # just in case, close all opened connections
    clientID=sim.simxStart('127.0.0.1',port,True,True,2000,5) # Conectarse
    if clientID == 0: print("conectado a", port)
    else: print("no se pudo conectar")
    return clientID
# Conectarse al servidor de CoppeliaSim
# *** ejecutar cada vez que se reinicia la simulación ***
clientID = connect(19999)
# importamos nuevas librerías
import cv2                      # opencv
import matplotlib.pyplot as plt # pyplot
import numpy as np
#necesario para ver la imagen

try:
    while True:
        # Obtenemos el manejador del sensor de visión
        retCode, sensorHandle = sim.simxGetObjectHandle(clientID, 'Vision_sensor', sim.simx_opmode_blocking)

        # Obtenemos la imagen
        retCode, resolution, image = sim.simxGetVisionSensorImage(clientID, sensorHandle, 0,
                                                                  sim.simx_opmode_oneshot_wait)

        len(image)

        img = np.array(image, dtype=np.uint8)
        img.resize([resolution[1], resolution[0], 3])
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
except KeyboardInterrupt:
    pass


#
