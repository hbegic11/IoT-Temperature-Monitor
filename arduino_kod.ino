int sensorPin = A0;

int zelena = 8;
int crvena = 9;
int buzzer = 10;

void setup() {
  Serial.begin(9600);
  pinMode(zelena, OUTPUT);
  pinMode(crvena, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  int value = analogRead(sensorPin);
  float voltage = value * (5.0 / 1023.0);
  float temperature = voltage * 100;

  Serial.println(temperature); // šalje Pythonu

  if (temperature < 25.0) {
    digitalWrite(zelena, HIGH);
    digitalWrite(crvena, LOW);
    digitalWrite(buzzer, LOW);
  } else {
    digitalWrite(zelena, LOW);
    digitalWrite(crvena, HIGH);
    digitalWrite(buzzer, HIGH);
    delay(200);
    digitalWrite(buzzer, LOW);
  }

  delay(2000);
}