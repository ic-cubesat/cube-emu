#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"

RF24 radio(9,10);
// Radio pipe addresses for the 2 nodes to communicate.
const uint64_t pipes[2] = {0xF0F0F0F0E1LL, 0xF0F0F0F0D2LL };

//for Serial input
String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

//NRF Packages
byte SendPackage[32];
byte ReceivePackage[32];
boolean sending=0;

void setup(void)
{
  //
  // Print preamble
  //

  Serial.begin(57600);
  radio.begin();
  // optionally, increase the delay between retries & # of retries
  radio.setRetries(15,15);
  radio.setPayloadSize(32);
  radio.openWritingPipe(pipes[1]);
  radio.openReadingPipe(1,pipes[0]);
  radio.startListening();
  
  radio.printDetails();
  Serial.println("Ready");
}

void loop(void)
{
  //check for NRF received
  NRFreceive();
  //check for Serial received (or filled by NRF)
  Serialreceive();  
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read(); 
    inputString += inChar;
    if (inChar == '\n') {
      stringComplete = true;
    } 
  }
}

byte NRFsend(String NRFPack = ""){
  NRFPack.getBytes(SendPackage, 32);
  radio.stopListening();
  radio.openWritingPipe(pipes[0]);
  radio.openReadingPipe(1,pipes[1]);
  bool ok = radio.write(SendPackage,sizeof(SendPackage));
  if (!ok) Serial.println("NRFerror");
  radio.startListening();
  unsigned long started_waiting_at = millis();
  bool timeout = false;
  while ( ! radio.available() && ! timeout )
    if (millis() - started_waiting_at > 200 )
      timeout = true;
  if ( timeout )
  {
    Serial.println("NRFerror");
  }
  radio.openWritingPipe(pipes[1]);
  radio.openReadingPipe(1,pipes[0]);
}

void NRFreceive(){
  if ( radio.available() )
  {
    //byte ReceivePackage[32];
    bool done = false;
    while (!done)
    {
      done = radio.read( &ReceivePackage, sizeof(ReceivePackage) );
      delay(5);
    }
    radio.stopListening();
    inputString = ((char *)ReceivePackage);
    stringComplete = true;
    radio.write( "1", 1 );
    radio.startListening();
  }
}

void Serialreceive(){
  if (stringComplete) {
    if (inputString.startsWith("T:")) {
      NRFsend(inputString.substring(2));
    }
    if (inputString.startsWith("S:")) {
      Serial.print(inputString.substring(2));
    }

    //    ####  TEST FUNCTIONS ###
    if (inputString == "P\n") {
      Serial.println("Pong");  
      NRFsend("S:Pong\n");   
    }
    if (inputString == "R\n"){
      double starttest = millis();
      int x = 1;
      while ((millis()-starttest) < 1000){
        NRFsend("11111111111111111111111111111111");
        x++;
      }
      Serial.print("Packet test 1000 millis: ");
      Serial.println(x);
      NRFsend("S:Remote Test: Packet test ");
      NRFsend("S:1000 millis: ");
      NRFsend("S:" + String(x) + "\n");
    }
    //    ####  TEST FUNCTIONS - END ###

    inputString = "";
    stringComplete = false;
  }
}
