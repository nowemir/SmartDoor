import board
import busio as io
import adafruit_mlx90614
from time import sleep 

i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)

def temp():
    sleep(1)
    targetTemp = "{:.2f}".format(mlx.object_temperature)
    return targetTemp
#temp()
