#include <SoftwareSerial.h>
int RXPin = 2;
int TXPin = 3;
int GPSBaud = 9600;
int data;
SoftwareSerial gpsSerial(RXPin, TXPin);

void setup()
{
  Serial.begin(9600);
  gpsSerial.begin(GPSBaud);
}


void loop()
{
  Serial.print('.');
  while (gpsSerial.available() > 0)
  {
    data = gpsSerial.read();
    Serial.print(char(data));
   
  }
  delay(1000);
  Serial.print("\n");
}
