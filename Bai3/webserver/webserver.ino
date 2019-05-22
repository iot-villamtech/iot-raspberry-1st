#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

//ten wifi, pass
const char* ssid = "Lab";
const char* password = "123456778";

ESP8266WebServer server(80);   //mo port 80 phuc vu tao webserver

String page = "";
int LEDPin1 = D1;
int LEDPin2 = D2;

void setup(void)
{
  //the HTML of the web page
  page ="<!DOCTYPE html><html><head><title>WEBSERVER VILLAMTECH</title><style>h1{background-color:rgb(255, 217, 71);color: red; text-align: center;}h3{color: green;}button{color: red}</style></head><body><h1>Web Server</h1><h3>LED 1</h3><p><a href=\"LEDOn1\"><button>ON</button></a>&nbsp;<a href=\"LEDOff1\"><button>OFF</button></a></p><br><h3>LED 2</h3><p><a href=\"LEDOn2\"><button>ON</button></a>&nbsp;<a href=\"LEDOff2\"><button>OFF</button></a></p></p></body></html>";
//  page = "<h1>Web Server</h1><h3>LED 1</h3><p><a href=\"LEDOn1\"><button>ON</button></a>&nbsp;<a href=\"LEDOff1\"><button>OFF</button></a></p><br><h3>LED 2</h3><a href=\"LEDOn2\"><button>ON</button></a>&nbsp;<a href=\"LEDOff2\"><button>OFF</button></a></p>";
  //make the LED pin output and initially turned off
  pinMode(LEDPin1, OUTPUT);
  digitalWrite(LEDPin1, LOW);
  pinMode(LEDPin2, OUTPUT);
  digitalWrite(LEDPin2, LOW);
  
  delay(1000);
  Serial.begin(115200); //baud rate cho viec hien thi du lieu
  
  WiFi.begin(ssid, password); //begin WiFi connection
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
   
  server.on("/", [](){
    server.send(200, "text/html", page);
  });
  server.on("/LEDOn1", [](){
    server.send(200, "text/html", page);
    digitalWrite(LEDPin1, HIGH);
    delay(1000);
  });
  server.on("/LEDOff1", [](){
    server.send(200, "text/html", page);
    digitalWrite(LEDPin1, LOW);
    delay(1000); 
  });
  server.on("/LEDOn2", [](){
    server.send(200, "text/html", page);
    digitalWrite(LEDPin2, HIGH);
    delay(1000);
  });
  server.on("/LEDOff2", [](){
    server.send(200, "text/html", page);
    digitalWrite(LEDPin2, LOW);
    delay(1000); 
  });
  server.begin();
  Serial.println("Web server started!");
}
 
void loop(void){
  server.handleClient();
}
