#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

MFRC522 mfrc522(SS_PIN, RST_PIN);
MFRC522::MIFARE_Key key;

unsigned long lastUID = 0;
const int intervalUID = 1000;

String input = "";

bool cartePresente = false;

void setup() {
  Serial.begin(9600);
  SPI.begin();
  mfrc522.PCD_Init();

  // Clé par défaut
  for (byte i = 0; i < 6; i++) {
    key.keyByte[i] = 0xFF;
  }

  Serial.println("RFID prêt !");
  Serial.println("Commandes : read | write:texte");
}

void loop() {

  // 📥 Lecture commande série
  if (Serial.available()) {
    input = Serial.readStringUntil('\n');
    input.trim();
  }

  // 📡 Détection carte (sans bloquer)
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    cartePresente = true;
  }

  // 📡 Envoi UID toutes les 1 seconde
  if (millis() - lastUID >= intervalUID) {
    lastUID = millis();

    if (cartePresente) {
      Serial.print("UID : ");
      for (byte i = 0; i < mfrc522.uid.size; i++) {
        Serial.print(mfrc522.uid.uidByte[i], HEX);
        Serial.print(" ");
      }
      Serial.println();
    }
  }

  // 🔐 READ ou WRITE uniquement si demandé
  if (cartePresente && input != "") {

    byte block = 4;
    MFRC522::StatusCode status;

    // Authentification
    status = mfrc522.PCD_Authenticate(
      MFRC522::PICC_CMD_MF_AUTH_KEY_A,
      block, &key, &(mfrc522.uid)
    );

    if (status != MFRC522::STATUS_OK) {
      Serial.println("Erreur auth");
    } 
    else {

      // 📖 LECTURE
      if (input == "read") {
        byte buffer[18];
        byte size = sizeof(buffer);

        status = mfrc522.MIFARE_Read(block, buffer, &size);

        if (status == MFRC522::STATUS_OK) {
          Serial.print("Contenu : ");
          for (byte i = 0; i < 16; i++) {
            Serial.write(buffer[i]);
          }
          Serial.println();
        } else {
          Serial.println("Erreur lecture");
        }
      }

      // ✍️ ÉCRITURE
      else if (input.startsWith("write:")) {
        String texte = input.substring(6);

        byte dataBlock[16];

        // Remplir avec espaces
        for (int i = 0; i < 16; i++) dataBlock[i] = ' ';

        // Copier texte
        for (int i = 0; i < texte.length() && i < 16; i++) {
          dataBlock[i] = texte[i];
        }

        status = mfrc522.MIFARE_Write(block, dataBlock, 16);

        if (status == MFRC522::STATUS_OK) {
          Serial.println("Ecriture OK !");
        } else {
          Serial.println("Erreur ecriture");
        }
      }

      else {
        Serial.println("Commande inconnue");
      }
    }

    // Stop communication
    mfrc522.PICC_HaltA();
    mfrc522.PCD_StopCrypto1();

    // Reset commande (important)
    input = "";
  }
}
