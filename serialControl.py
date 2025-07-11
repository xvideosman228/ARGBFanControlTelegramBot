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
    def color(color):
        logger.info(f"Отправлен сигнал {color} на Arduino")
        print(f"{color.upper()}")
        arduino.write(f'{color.upper()}'.encode("utf-8"))
        time.sleep(1)

    @staticmethod
    def fadeinout(color, time):
        logger.info("Отправлен сигнал BLACK на Arduino")
        arduino.write(f'FADEINOUT {color} {time}'.encode('utf-8'))
        time.sleep(1)

    @staticmethod
    def colorwipe(color1, color2, time):
        logger.info("Отправлен сигнал BLACK на Arduino")
        print(f'COLORWIPE {color1} {color2} {time}')
        arduino.write(f'COLORWIPE {color1} {color2} {time}'.encode("utf-8"))
        time.sleep(1)

    @staticmethod
    def gradient(color1, color2):
        logger.info("Отправлен сигнал BLACK на Arduino")
        print(f'GRADIENT {color1} {color2}')
        arduino.write(f'GRADIENT {color1} {color2}'.encode("utf-8"))
        time.sleep(1)

    @staticmethod
    def gradient4(color1, color2, color3, color4):
        logger.info("Отправлен сигнал BLACK на Arduino")
        print(f'GRADIENT4 {color1} {color2} {color3} {color4}')
        arduino.write(f'GRADIENT4 {color1} {color2} {color3} {color4}'.encode("utf-8"))
        time.sleep(1)

    @staticmethod
    def smoothGradient(color1, color2):
        logger.info("Отправлен сигнал BLACK на Arduino")
        print(f'SMOOTHGRADIENT {color1} {color2}')
        arduino.write(f'SMOOTHGRADIENT {color1} {color2}'.encode("utf-8"))
        time.sleep(1)

    @staticmethod
    def rainbow():
        logger.info("Отправлен сигнал Rainbow на Arduino")
        arduino.write(b'RAINBOW')
        time.sleep(1)

    @staticmethod
    def cylon(time):
        logger.info("Отправлен сигнал Cylon на Arduino")
        arduino.write(f'CYLON {time.upper()}'.encode("utf-8"))
        time.sleep(1)

    @staticmethod
    def pacific():
        logger.info("Отправлен сигнал Pacific на Arduino")
        arduino.write(b'PACIFIC')
        time.sleep(1)

    @staticmethod
    def runninglight():
        logger.info("Отправлен сигнал Running Light на Arduino")
        arduino.write(b'RUNNINGLIGHT')
        time.sleep(1)

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

    @staticmethod
    def brightnessplus():
        logger.info("Отправлен сигнал Brightness ++ на Arduino")
        arduino.write(b'BRIGHTNESS+')
        time.sleep(1)  # Пауза в секунду после отправки сигнала

    @staticmethod
    def brightnessminus():
        logger.info("Отправлен сигнал Brightness -- на Arduino")
        arduino.write(b'BRIGHTNESS-')
        time.sleep(1)  # Пауза в секунду после отправки сигнала

