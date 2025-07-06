import serial
import json
import time
from config.loggingConfig import logger

# Загрузка конфигурации
with open('./config/arduino.json') as file:
    conf = json.load(file)

# Подключение к Arduino
arduino = serial.Serial(port=conf['port'], baudrate=conf['baudrate'], timeout=conf['timeout'])

class FanController:
    @staticmethod
    def red():
        logger.info("Отправлен сигнал Red на Arduino")
        arduino.write(b'RED')
        time.sleep(1) # Пауза в секунду после отправки сигнала

    @staticmethod
    def green():
        logger.info("Отправлен сигнал Green на Arduino")
        arduino.write(b'GREEN')
        time.sleep(1) # Пауза в секунду после отправки сигнала

    @staticmethod
    def brightnessplusplus():
        logger.info("Отправлен сигнал Brightness ++ на Arduino")
        arduino.write(b'BRIGHTNESS++')
        time.sleep(1)  # Пауза в секунду после отправки сигнала

    @staticmethod
    def brightnessminusminus():
        logger.info("Отправлен сигнал Brightness -- на Arduino")
        arduino.write(b'BRIGHTNESS--')
        time.sleep(1)  # Пауза в секунду после отправки сигнала

