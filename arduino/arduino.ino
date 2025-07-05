#include <FastLED.h>

#define LED_PIN     2
#define NUM_LEDS    8
CRGB leds[NUM_LEDS];

boolean runPrideEffect = false; // Глобальный флаг, определяющий, запущен ли pride2015

void setup() {
  FastLED.addLeds<NEOPIXEL, LED_PIN>(leds, NUM_LEDS);
  Serial.begin(9600); // Инициализируем последовательный порт для приема команд
}

void loop() {
  checkForCommands(); // Регулярно проверяем, не поступил ли новый запрос

  if(runPrideEffect) {
    pride2015(); // Воспроизводим эффект pride2015, если включен
  }
}

// Проверка порта на наличие запросов
void checkForCommands() {
  if (Serial.available() > 0) {
    String incomingCommand = Serial.readStringUntil('\\n');
    incomingCommand.trim(); // очищаем от пробелов и переводов строки

    if(incomingCommand.equalsIgnoreCase("red")) {
      runPrideEffect = true; // включить бесконечное воспроизведение pride2015
    } else {
      runPrideEffect = false; // любая другая команда отменяет эффект pride2015
    }
  }
}

// Встроенный эффект pride2015 из FastLED
void pride2015() {
  static uint8_t startIndex = 0;
  for(int i = 0; i < NUM_LEDS; i++) {
    leds[i] = CHSV(startIndex + i * 16, 255, 255);
  }
  FastLED.show();
  startIndex += 1;
  delay(10); // скорость воспроизведения эффекта
}
