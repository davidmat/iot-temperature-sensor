// These constants won't change.  They're used to give names
// to the pins used:
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to

float sensorValue = 0.0;        // value read from the pot

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600); 
  analogReference(EXTERNAL);
  
}

void loop() {
  // read the analog in value:
              
  sensorValue = readTemp(); 
  float millivolts = (sensorValue * 3300.0) / 1024.0;
  float temperature = (millivolts - 500.0) / 10.0;

  // print the results to the serial monitor:
  //Serial.print("sensor = " );                       
  //Serial.println(sensorValue); 
  //Serial.print("millivolts = " );                       
  //Serial.println(millivolts, 2);      
  //Serial.print("temperature = " );                       
  Serial.println(temperature, 2);        

  // wait 2 seconds before the next loop
  // for the analog-to-digital converter to settle
  // after the last reading:
  delay(2000);  
}

float readTemp(){
  int tempValue = 0;
  for (int i=0;i<30;i++){
    tempValue+=analogRead(analogInPin);
    delay(10);
   } 
   float averagedValue = tempValue / 30.0;
 return averagedValue;
}

