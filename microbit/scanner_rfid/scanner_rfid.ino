/*

| RC522 | Arduino |
| ----- | ------- |
| SDA   | D10     |
| SCK   | D13     |
| MOSI  | D11     |
| MISO  | D12     |
| RST   | D9      |
| 3.3V  | 3.3V    |
| GND   | GND     |


*/
#include <SPI.h>
#include <RFID.h>

#define SDA_PIN 10
#define RST_PIN 9

RFID rfid(SDA_PIN, RST_PIN);

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.init();

  Serial.println("Lecteur RFID prêt !");
  Serial.println("Approche une carte...");
}

void loop() {
  // Si une carte est détectée
  if (rfid.isCard()) {
    // Si le numéro de la carte est lisible
    if (rfid.readCardSerial()) {
      Serial.print("UID de la carte : ");

      for (int i = 0; i < 5; i++) {
        Serial.print(rfid.serNum[i], HEX);
        Serial.print(" ");
      }
      Serial.println();
    }

    // Stop la communication avec la carte
    rfid.halt();
  }
}
