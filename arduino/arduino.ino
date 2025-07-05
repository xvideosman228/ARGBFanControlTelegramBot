void setup() {
  pinMode(2, OUTPUT);            // Настроить вывод 2 как выход
  pinMode(3, OUTPUT);            // Настроить вывод 3 как выход
  Serial.begin(9600);            // Начало обмена данными через последовательный порт
}

void loop() {
  if (Serial.available() > 0) {  // Если данные доступны
    String receivedStr = Serial.readStringUntil('\\n');  // Чтение строки до перевода строки (\\n)
    receivedStr.trim();                                 // Удаляем возможные лишние пробелы и переводы строки

    if (receivedStr.equalsIgnoreCase("A")) {           // Проверка полученной строки
      digitalWrite(2, HIGH);                           // Включаем светодиод на выводе 2
      delay(1000);                                     // Пауза 1 секунду
      digitalWrite(2, LOW);                            // Выключаем светодиод
    }

    if (receivedStr.equalsIgnoreCase("A")) {           // Проверка второй строки
      digitalWrite(3, HIGH);                           // Включаем светодиод на выводе 3
      delay(1000);                                     // Пауза 1 секунду
      digitalWrite(3, LOW);                            // Выключаем светодиод
    }
  }
}
