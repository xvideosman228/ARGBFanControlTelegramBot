import serial
import json
import time
from config.loggingConfig import logger

# Загрузка конфигурации
with open('./config/arduino.json') as file:
    conf = json.load(file)

# Подключение к Arduino
arduino = serial.Serial(port=conf['port'], baudrate=conf['baudrate'], timeout=conf['timeout'])

def button1():
    logger.info("Отправлен сигнал 1 на Arduino")
    arduino.write(b'A')
    time.sleep(1) # Пауза в секунду после отправки сигнала

def button2():
    logger.info("Отправлен сигнал 2 на Arduino")
    arduino.write(b'B')
    time.sleep(1) # Пауза в секунду после отправки сигнала