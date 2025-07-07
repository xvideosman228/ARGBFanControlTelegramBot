#define FASTLED_ALLOW_INTERRUPTS 0
#include <FastLED.h>
FASTLED_USING_NAMESPACE

#define PIN    13
#define LED_TYPE    WS2811
#define COLOR_ORDER GRB
#define NUM 8
int BRIGHTNESS = 0;
#define BRIGHTNESSPLUSPLUS 50

CRGB leds[NUM];       // Массив для хранения состояния каждого диода

void setup() {
  delay(2000);
  FastLED.addLeds<WS2811, PIN, GRB>(leds, NUM).setCorrection( TypicalLEDStrip);

  
          // Задержка перед инициализацией, позволяет подключить монитор порт
  Serial.begin(9600);     // Начинаем работу последовательного порта
}

// Функция для показа стандартной анимации Pride 2015
void showPride() {
  fill_rainbow(leds, NUM, millis() / 20, 7);
  FastLED.show();
}

CRGB colorPick(const String& color)
{
  if(color == "RED"){return CRGB::Red;}
  else if(color == "ORANGE"){return CRGB::DarkOrange;}
  else if(color == "GREEN"){return CRGB::Green;}
  
  else if(color == "YELLOW"){return CRGB::Yellow;}
  else if(color == "YELLOWORANGE"){return CRGB::Gold;}
  else if(color == "ORANGERED"){return CRGB::OrangeRed;}

  else if(color == "LIGHTBLUE"){return CRGB::Turquoise;}
  else if(color == "DARKBLUE"){return CRGB::MidnightBlue;}
  else if(color == "VIOLET"){return CRGB::Purple;}

  else if(color == "WHITE"){return CRGB::Snow;}
  else if(color == "BLUE"){return CRGB::Blue;}

}

// Очистка всех светодиодов


// Тестирование отдельных групп светодиодов

void staticColor(CRGB color) {
  fill_solid( leds, NUM, color );
  FastLED.show();
}

// 

//FadeInOut(0xff, 0x77, 0x00);

//colorWipe(0x00,0xff,0x00, 50);
//colorWipe(0x00,0x00,0x00, 50);

// RunningLights(0xff,0xff,0x00, 100);


// theaterChaseRainbow(50);
// testGroups(); 

// Основной цикл обработки
void loop() {
  if(Serial.available()) {           // Проверяем наличие данных в последовательном порту
    String command = Serial.readStringUntil('\\n');
    Serial.println(command);
    String cmd = command.substring(0, command.indexOf(' '));
    if(command == "RED") 
    {          
      while(true) {     
        Serial.println("RED");            
        staticColor(CRGB::Red);
        if(Serial.available()) {   
          break;                   
        }
      }
    }

    else if(command == "GREEN") 
    {          
      while(true) {     
        Serial.println("GREEN");            
        staticColor(CRGB::Green);
        if(Serial.available()) {   
          break;                   
        }
      }
    }
  
    else if(command == "BLUE") 
    {          
      while(true) {     
        Serial.println("BLUE");            
        staticColor(CRGB::Blue);
        if(Serial.available()) {   
          break;                   
        }
      }
    }

    else if(command == "YELLOW") 
    {          
      while(true) {     
        Serial.println("YELLOW");                 
        staticColor(CRGB::Yellow);
        if(Serial.available()) {   
          break;                   
        }
      }
    }

    else if(command == "YELLOWORANGE") 
    {          
      while(true) {     
        Serial.println("YELLOWORANGE");                 
        staticColor(CRGB::Gold);
        if(Serial.available()) {   
          break;                   
        }
      }
    }

    else if(command == "ORANGE") 
    {          
      while(true) {     
        Serial.println("ORANGE");                 
        staticColor(CRGB::DarkOrange);
        if(Serial.available()) {   
          break;                   
        }
      }
    }

    else if(command == "ORANGERED") 
    {          
      while(true) {     
        Serial.println("ORANGERED");            
        staticColor(CRGB::OrangeRed);  
        if(Serial.available()) {   
          break;                   
        }
      }
    }

    else if(command == "LIGHTBLUE") 
    {          
      while(true) {     
        Serial.println("LIGHT BLUE");            
        staticColor(CRGB::Turquoise); 
        if(Serial.available()) {   
          break;                   
        }
      }
    }

    else if(command == "DARKBLUE") 
    {          
      while(true) {     
        Serial.println("DARKBLUE");  
        staticColor(CRGB::MidnightBlue);         
        if(Serial.available()) {   
          break;                   
        }
      }
    }

    else if(command == "VIOLET") 
    {          
      while(true) {     
        Serial.println("VIOLET");  
        staticColor(CRGB::Purple);         
        if(Serial.available()) {   
          break;                   
        }
      }
    }

    else if(command == "WHITE") 
    {          
      while(true) {     
        Serial.println("WHITE");  
        staticColor(CRGB::Snow);         
        if(Serial.available()) {   
          break;                   
        }
      }
    }

    else if(command == "BLACK") 
    {          
      while(true) {     
        Serial.println("BALCK");  
        staticColor(CRGB::Black);         
        if(Serial.available()) {   
          break;                   
        }
      }
    }

    else if(cmd == "FADEINOUT") 
    {          
      Serial.println("FADE IN & OUT");
      String color = command.substring(command.indexOf(' ') + 1, -1);
      Serial.println(color);
      while(true) 
      {   
        Serial.println("FADE IN & OUT " + color);  
        FadeInOut(colorPick(color));         
        if(Serial.available()) 
        {   
          break;                   
        }
      }
    }

    else if(cmd == "COLORWIPE") 
    {          

      int firstSpace = command.indexOf(' ') + 1;
      int secondSpace = command.indexOf(' ', firstSpace) + 1;
      String color1 = command.substring(firstSpace, secondSpace);
      String color2 = command.substring(secondSpace);
      while(true) {     
        Serial.println("COLORWIPE " + color1 + color2);   
        colorWipe(colorPick(color1), 50);
        colorWipe(colorPick(color2), 50);     
        if(Serial.available()) {   
          break;                   
        }
      }
    }
    // 
    else if(command == "RAINBOW") 
    {          
      while(true) {     
        Serial.println("RAINBOW");       
        rainbowCycle(10);
        if(Serial.available()) {   
          break;                   
        }
      }
    }

    else if(command == "RUNNINGLIGHT") 
    {          
      while(true) {     
        Serial.println("RUNNING LIGHT");       
        theaterChaseRainbow(40);
        if(Serial.available()) {   
          break;                   
        }
      }
    }

    else if(command == "CYLON") 
    {          
      while(true) {     
        Serial.println("CYLON");       
        showPride();
        if(Serial.available()) {   
          break;                   
        }
      }
    }
    
    else if(command == "PACIFIC") 
    {          
      while(true) {     
        pacifica_loop();
        FastLED.show();
        if(Serial.available()) {   
          break;                   
        }
      }
    }

    else if(command == "BRIGHTNESS++") 
    {          
      Serial.println("BRIGHTNESS++");                 
      BRIGHTNESS += BRIGHTNESSPLUSPLUS;
    }  

    else if(command == "BRIGHTNESS--") 
    {          
      Serial.println("BRIGHTNESS--");                 
      BRIGHTNESS -= BRIGHTNESSPLUSPLUS;
    }
  }
  
}


void CylonBounce(byte red, byte green, byte blue, int EyeSize, int SpeedDelay, int ReturnDelay){

  for(int i = 0; i < NUM-EyeSize-2; i++) {
    setAll(0,0,0);
    setPixel(i, red/10, green/10, blue/10);
    for(int j = 1; j <= EyeSize; j++) {
      setPixel(i+j, red, green, blue);
    }
    setPixel(i+EyeSize+1, red/10, green/10, blue/10);
    showStrip();
    delay(SpeedDelay);
  }

  delay(ReturnDelay);

  for(int i = NUM-EyeSize-2; i > 0; i--) {
    setAll(0,0,0);
    setPixel(i, red/10, green/10, blue/10);
    for(int j = 1; j <= EyeSize; j++) {
      setPixel(i+j, red, green, blue);
    }
    setPixel(i+EyeSize+1, red/10, green/10, blue/10);
    showStrip();
    delay(SpeedDelay);
  }
 
  delay(ReturnDelay);
}

void colorWipe(CRGB color, int SpeedDelay) 
{
  uint8_t red = color.r;
  uint8_t green = color.g;
  uint8_t blue = color.b;
  for(uint16_t i=0; i<NUM; i++) {
      setPixel(i, red, green, blue);
      showStrip();
      delay(SpeedDelay);
  }
}

void FadeInOut(CRGB color){
  uint8_t red = color.r;
  uint8_t green = color.g;
  uint8_t blue = color.b;
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

void RunningLights(byte red, byte green, byte blue, int WaveDelay) {
  int Position=0;
 
  for(int j=0; j<NUM*4; j++)
  {
    if(Serial.available()) {   
          break;                   
        }
      Position++; // = 0; //Position + Rate;
      for(int i=0; i<NUM; i++) {
        // sine wave, 3 offset waves make a rainbow!
        //float level = sin(i+Position) * 127 + 128;
        //setPixel(i,level,0,0);
        //float level = sin(i+Position) * 127 + 128;
        setPixel(i,((sin(i+Position) * 127 + 128)/255)*red,
                   ((sin(i+Position) * 127 + 128)/255)*green,
                   ((sin(i+Position) * 127 + 128)/255)*blue);
      }
     
      showStrip();
      delay(WaveDelay);
  }
}

void rainbowCycle(int SpeedDelay) {
  byte *c;
  uint16_t i, j;

  for(j=0; j<256*5; j++) { // 5 cycles of all colors on wheel
    for(i=0; i< NUM; i++) {
      c=Wheel(((i * 256 / NUM) + j) & 255);
      setPixel(i, *c, *(c+1), *(c+2));
    }
    if(Serial.available()) {   
          break;                   
        }
    showStrip();
    delay(SpeedDelay);
  }
}

void theaterChaseRainbow(int SpeedDelay) {
  byte *c;
 
  for (int j=0; j < 256; j++) {     // cycle all 256 colors in the wheel
    for (int q=0; q < 3; q++) {
        for (int i=0; i < NUM; i=i+3) {
          c = Wheel( (i+j) % 255);
          setPixel(i+q, *c, *(c+1), *(c+2));    //turn every third pixel on
        }
        showStrip();
        if(Serial.available()) {   
          break;                   
        }
        delay(SpeedDelay);
       
        for (int i=0; i < NUM; i=i+3) {
          setPixel(i+q, 0,0,0);        //turn every third pixel off
        }
    }
  }
}


byte * Wheel(byte WheelPos) {
  static byte c[3];
 
  if(WheelPos < 85) {
   c[0]=WheelPos * 3;
   c[1]=255 - WheelPos * 3;
   c[2]=0;
  } else if(WheelPos < 170) {
   WheelPos -= 85;
   c[0]=255 - WheelPos * 3;
   c[1]=0;
   c[2]=WheelPos * 3;
  } else {
   WheelPos -= 170;
   c[0]=0;
   c[1]=WheelPos * 3;
   c[2]=255 - WheelPos * 3;
  }

  return c;
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
  for(int i = 0; i < NUM; i++ ) {
    setPixel(i, red, green, blue);
  }
  showStrip();
}

CRGBPalette16 pacifica_palette_1 = 
    { 0x000507, 0x000409, 0x00030B, 0x00030D, 0x000210, 0x000212, 0x000114, 0x000117, 
      0x000019, 0x00001C, 0x000026, 0x000031, 0x00003B, 0x000046, 0x14554B, 0x28AA50 };
CRGBPalette16 pacifica_palette_2 = 
    { 0x000507, 0x000409, 0x00030B, 0x00030D, 0x000210, 0x000212, 0x000114, 0x000117, 
      0x000019, 0x00001C, 0x000026, 0x000031, 0x00003B, 0x000046, 0x0C5F52, 0x19BE5F };
CRGBPalette16 pacifica_palette_3 = 
    { 0x000208, 0x00030E, 0x000514, 0x00061A, 0x000820, 0x000927, 0x000B2D, 0x000C33, 
      0x000E39, 0x001040, 0x001450, 0x001860, 0x001C70, 0x002080, 0x1040BF, 0x2060FF };


void pacifica_loop()
{
  // Increment the four "color index start" counters, one for each wave layer.
  // Each is incremented at a different speed, and the speeds vary over time.
  static uint16_t sCIStart1, sCIStart2, sCIStart3, sCIStart4;
  static uint32_t sLastms = 0;
  uint32_t ms = GET_MILLIS();
  uint32_t deltams = ms - sLastms;
  sLastms = ms;
  uint16_t speedfactor1 = beatsin16(3, 179, 269);
  uint16_t speedfactor2 = beatsin16(4, 179, 269);
  uint32_t deltams1 = (deltams * speedfactor1) / 256;
  uint32_t deltams2 = (deltams * speedfactor2) / 256;
  uint32_t deltams21 = (deltams1 + deltams2) / 2;
  sCIStart1 += (deltams1 * beatsin88(1011,10,13));
  sCIStart2 -= (deltams21 * beatsin88(777,8,11));
  sCIStart3 -= (deltams1 * beatsin88(501,5,7));
  sCIStart4 -= (deltams2 * beatsin88(257,4,6));

  // Clear out the LED array to a dim background blue-green
  fill_solid( leds, NUM, CRGB( 2, 6, 10));

  // Render each of four layers, with different scales and speeds, that vary over time
  pacifica_one_layer( pacifica_palette_1, sCIStart1, beatsin16( 3, 11 * 256, 14 * 256), beatsin8( 10, 70, 130), 0-beat16( 301) );
  pacifica_one_layer( pacifica_palette_2, sCIStart2, beatsin16( 4,  6 * 256,  9 * 256), beatsin8( 17, 40,  80), beat16( 401) );
  pacifica_one_layer( pacifica_palette_3, sCIStart3, 6 * 256, beatsin8( 9, 10,38), 0-beat16(503));
  pacifica_one_layer( pacifica_palette_3, sCIStart4, 5 * 256, beatsin8( 8, 10,28), beat16(601));

  // Add brighter 'whitecaps' where the waves lines up more
  pacifica_add_whitecaps();

  // Deepen the blues and greens a bit
  pacifica_deepen_colors();
}

// Add one layer of waves into the led array
void pacifica_one_layer( CRGBPalette16& p, uint16_t cistart, uint16_t wavescale, uint8_t bri, uint16_t ioff)
{
  uint16_t ci = cistart;
  uint16_t waveangle = ioff;
  uint16_t wavescale_half = (wavescale / 2) + 20;
  for( uint16_t i = 0; i < NUM; i++) {
    waveangle += 250;
    uint16_t s16 = sin16( waveangle ) + 32768;
    uint16_t cs = scale16( s16 , wavescale_half ) + wavescale_half;
    ci += cs;
    uint16_t sindex16 = sin16( ci) + 32768;
    uint8_t sindex8 = scale16( sindex16, 240);
    CRGB c = ColorFromPalette( p, sindex8, bri, LINEARBLEND);
    leds[i] += c;
  }
}

// Add extra 'white' to areas where the four layers of light have lined up brightly
void pacifica_add_whitecaps()
{
  uint8_t basethreshold = beatsin8( 9, 55, 65);
  uint8_t wave = beat8( 7 );
  
  for( uint16_t i = 0; i < NUM; i++) {
    uint8_t threshold = scale8( sin8( wave), 20) + basethreshold;
    wave += 7;
    uint8_t l = leds[i].getAverageLight();
    if( l > threshold) {
      uint8_t overage = l - threshold;
      uint8_t overage2 = qadd8( overage, overage);
      leds[i] += CRGB( overage, overage2, qadd8( overage2, overage2));
    }
  }
}

// Deepen the blues and greens
void pacifica_deepen_colors()
{
  for( uint16_t i = 0; i < NUM; i++) {
    leds[i].blue = scale8( leds[i].blue,  145); 
    leds[i].green= scale8( leds[i].green, 200); 
    leds[i] |= CRGB( 2, 5, 7);
  }
}





