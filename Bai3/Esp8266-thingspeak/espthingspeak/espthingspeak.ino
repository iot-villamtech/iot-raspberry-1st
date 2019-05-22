#include <ESP8266WiFi.h>
#include "DHT.h"


//DHT config
#define DHTPIN D3     // what digital pin we're connected to ESP
//#define DHTTYPE DHT11   // DHT 11
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21   // DHT 21 (AM2301)
DHT dht(DHTPIN, DHTTYPE);

// Wi-Fi Settings
const char* ssid = "Lab"; // your wireless network name (SSID)
const char* password = "Villamtech"; // your Wi-Fi network password

WiFiClient client;

// ThingSpeak Settings
const int channelID = 785404; //
String writeAPIKey = "UH0N9516FXS4FGD4"; // write API key for your ThingSpeak Channel
const char* server = "api.thingspeak.com";
const int postingInterval = 2000; // post data every 2 seconds

void setup() {
  Serial.begin(115200);
  dht.begin();
  Serial.print("Connecting");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(100);
  }
  Serial.println("\r\nWiFi connected");
}

void loop() {
  // Wait a few seconds between measurements.
  delay(2000);

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  if (client.connect(server, 80)) {
    // Construct API request body
    String body = "field1=" + String(t, 1) + "&field2=" + String(h, 1);

    client.print("POST /update HTTP/1.1\n");
    client.print("Host: api.thingspeak.com\n");
    client.print("Connection: close\n");
    client.print("X-THINGSPEAKAPIKEY: " + writeAPIKey + "\n");
    client.print("Content-Type: application/x-www-form-urlencoded\n");
    client.print("Content-Length: ");
    client.print(body.length());
    client.print("\n\n");

    client.print(body);

    client.print("\n\n");
    
    Serial.printf("Nhiet do %s - Do am %s\r\n", String(t, 1).c_str(), String(h, 1).c_str());
  }
  client.stop();
}
