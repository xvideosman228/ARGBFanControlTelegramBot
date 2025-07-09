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
    def blue():
        logger.info("Отправлен сигнал Blue на Arduino")
        arduino.write(b'BLUE')
        time.sleep(1)  # Пауза в секунду после отправки сигнала

    @staticmethod
    def yellow():
        logger.info("Отправлен сигнал Yellow на Arduino")
        arduino.write(b'YELLOW')
        time.sleep(1)

    @staticmethod
    def yelloworange():
        logger.info("Отправлен сигнал Yellow-Orange на Arduino")
        arduino.write(b'YELLOWORANGE')
        time.sleep(1)

    @staticmethod
    def orangered():
        logger.info("Отправлен сигнал Orange-Red на Arduino")
        arduino.write(b'ORANGERED')
        time.sleep(1)

    @staticmethod
    def orange():
        logger.info("Отправлен сигнал Orange на Arduino")
        arduino.write(b'ORANGE')
        time.sleep(1)

    @staticmethod
    def lightblue():
        logger.info("Отправлен сигнал Light Blue на Arduino")
        arduino.write(b'LIGHTBLUE')
        time.sleep(1)

    @staticmethod
    def darkblue():
        logger.info("Отправлен сигнал Dark Blue на Arduino")
        arduino.write(b'DARKBLUE')
        time.sleep(1)

    @staticmethod
    def violet():
        logger.info("Отправлен сигнал Violet на Arduino")
        arduino.write(b'VIOLET')
        time.sleep(1)

    @staticmethod
    def white():
        logger.info("Отправлен сигнал White на Arduino")
        arduino.write(b'WHITE')
        time.sleep(1)

    @staticmethod
    def black():
        logger.info("Отправлен сигнал BLACK на Arduino")
        arduino.write(b'BLACK')
        time.sleep(1)

    @staticmethod
    def fadeinout(color):
        logger.info("Отправлен сигнал BLACK на Arduino")
        arduino.write(b'FADEINOUT' + b' ' + color.encode('utf-8'))
        time.sleep(1)

    @staticmethod
    def colorwipe(color1, color2):
        logger.info("Отправлен сигнал BLACK на Arduino")
        print(color1, color2)
        arduino.write(f'COLORWIPE {color1} {color2}'.encode("utf-8"))
        time.sleep(1)

    @staticmethod
    def rainbow():
        logger.info("Отправлен сигнал Rainbow на Arduino")
        arduino.write(b'RAINBOW')
        time.sleep(1)

    @staticmethod
    def cylon():
        logger.info("Отправлен сигнал Cylon на Arduino")
        arduino.write(b'CYLON')
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

