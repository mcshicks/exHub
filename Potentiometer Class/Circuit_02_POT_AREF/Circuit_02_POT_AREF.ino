/*

Example sketch 02

POTENTIOMETER analogReference example

  
*/


// 
int sensorPin = 0;    // The potentiometer is connected to
                      // analog pin 0
                      
int ledPin = 13;      // The LED is connected to digital pin 13



void setup() // this function runs once when the sketch starts up
{
  
  Serial.begin(9600); // for printing analog read values
  pinMode(ledPin, OUTPUT);
  //uncomment below to change analog reference
  //analogReference(EXTERNAL); 
  // 5V through 10K ohm resistor approx 5V*32k/(10k + 32k) = approx 3.8V 
  //analogReference(INTERNAL); // 1.1 V
}


void loop() // this function runs repeatedly after setup() finishes
{
  // First we'll declare another integer variable
  // to store the value of the potentiometer:

  int sensorValue;

  // The potentiometer is set up as a voltage divider, so that
  // when you turn it, the voltage on the center pin will vary
  // from 0V to 5V. We've connected the center pin on the
  // potentiometer to the Arduino's analog input 0.

  // The Arduino can read external voltages on the analog input
  // pins using a built-in function called analogRead(). This
  // function takes one input value, the analog pin we're using
  // (sensorPin, which we earlier set to 0). It returns an integer
  // number that ranges from 0 (0 Volts) to 1023 (5 Volts).
  // We're sticking this value into the sensorValue variable:

  sensorValue = analogRead(sensorPin);    

  // Now we'll blink the LED like in the first example, but we'll
  // use the sensorValue variable to change the blink speed
  // (the smaller the number, the faster it will blink).

  // Note that we're using the ledPin variable here as well:
  Serial.print("read value: ");
  Serial.println(sensorValue);
  digitalWrite(ledPin, HIGH);     // Turn the LED on

  delay(1023-sensorValue);             // Pause for sensorValue
                                  // milliseconds
  
  digitalWrite(ledPin, LOW);      // Turn the LED off

  delay(1023-sensorValue);             // Pause for sensorValue
                                  // milliseconds
  
  // Remember that loop() repeats forever, so we'll do all this
  // again and again.
}

