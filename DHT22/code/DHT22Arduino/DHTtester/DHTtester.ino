// Example testing sketch for various DHT humidity/temperature sensors
// Written by ladyada, public domain

#include "DHT.h"


#define DHTPIN1 2     // Inside Cloth
#define DHTPIN2 3     //Outside Cloth


// Uncomment whatever type you're using!
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321

// Connect pin 1 (on the left) of the sensor to +5V
// NOTE: If using a board with 3.3V logic like an Arduino Due connect pin 1
// to 3.3V instead of 5V!
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

// Initialize DHT sensor.
// Note that older versions of this library took an optional third parameter to
// tweak the timings for faster processors.  This parameter is no longer needed
// as the current DHT reading algorithm adjusts itself to work on faster procs.
DHT dht1(DHTPIN1, DHTTYPE);
DHT dht2(DHTPIN2, DHTTYPE);

void setup() {
  Serial.begin(115200);
//  Serial.println("DHT22 test!");

  dht1.begin();
  dht2.begin();
}

void loop() {

  // Reading temperature or humidity takes about 250 milliseconds!
  // Read temperature as Celsius (the default)
  float t1 = dht1.readTemperature();
  float t2 = dht2.readTemperature();
  
  // Check if any reads failed and exit early (to try again).
  if (isnan(t1) || isnan(t2)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  
  Serial.print(t1);
  Serial.print(",");
  Serial.println(t2);

 // Wait a few seconds between measurements.
  delay(30000); //wait for 30 secs
}
