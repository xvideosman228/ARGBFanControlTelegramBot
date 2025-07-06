#include <FastLED.h>

#define PIN     2      // ПИН, подключенный к ленте
#define LED_TYPE    WS2811
#define COLOR_ORDER GRB
#define NUM_LEDS    8
#define BRIGHTNESS 255

CRGB leds[NUM_LEDS];       // Массив для хранения состояния каждого диода

void setup() {
  delay(2000);
  FastLED.addLeds<WS2811, PIN, GRB>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );            // Задержка перед инициализацией, позволяет подключить монитор порта
  Serial.begin(9600);     // Начинаем работу последовательного порта
}

// Функция для показа стандартной анимации Pride 2015
void showPride() {
  fill_rainbow(leds, NUM_LEDS, millis() / 20, 7);
  FastLED.show();
}

void showP() {
  fill_solid( leds, NUM_LEDS, CRGB::Red );
  FastLED.show();
}

// Основной цикл обработки
void loop() {
  if(Serial.available()) {           // Проверяем наличие данных в последовательном порту
    String command = Serial.readStringUntil('\\n');
    Serial.println(command);
    if(command == "RED") 
    {          // Если команда равна 'red', запускаем режим Rainbow Pride
      while(true) {     
        Serial.println("RED");            // Бесконечный цикл воспроизведения анимации
        showPride();                // Показываем анимацию
        
        if(Serial.available()) {   // Ожидаем новую команду
          break;                   // Выходим из бесконечного цикла при получении новой команды
        }
      }
    }

    else if(command == "GREEN") 
    {          // Если команда равна 'red', запускаем режим Rainbow Pride
      while(true) {     
        Serial.println("GREEN");            // Бесконечный цикл воспроизведения анимации
        FadeInOut(0xff, 0x77, 0x00);                // Показываем анимацию
        
        if(Serial.available()) {   // Ожидаем новую команду
          break;                   // Выходим из бесконечного цикла при получении новой команды
        }
      }
    }
  // Другие возможные команды можно добавить аналогично
  }
  
}

void FadeInOut(byte red, byte green, byte blue){
  float r, g, b;
     
  for(int k = 0; k < 256; k=k+1) {
    r = (k/256.0)*red;
    g = (k/256.0)*green;
    b = (k/256.0)*blue;
    setAll(r,g,b);
    showStrip();
  }
     
  for(int k = 255; k >= 0; k=k-2) {
    if(Serial.available()) 
    {   
      break;
    }
    r = (k/256.0)*red;
    g = (k/256.0)*green;
    b = (k/256.0)*blue;
    setAll(r,g,b);
    showStrip();
  }
}

void showStrip() {
 #ifdef ADAFRUIT_NEOPIXEL_H
   // NeoPixel
   strip.show();
 #endif
 #ifndef ADAFRUIT_NEOPIXEL_H
   // FastLED
   FastLED.show();
 #endif
}

void setPixel(int Pixel, byte red, byte green, byte blue) {
 #ifdef ADAFRUIT_NEOPIXEL_H
   // NeoPixel
   strip.setPixelColor(Pixel, strip.Color(red, green, blue));
 #endif
 #ifndef ADAFRUIT_NEOPIXEL_H
   // FastLED
   leds[Pixel].r = red;
   leds[Pixel].g = green;
   leds[Pixel].b = blue;
 #endif
}

void setAll(byte red, byte green, byte blue) {
  for(int i = 0; i < NUM_LEDS; i++ ) {
    setPixel(i, red, green, blue);
  }
  showStrip();
}
