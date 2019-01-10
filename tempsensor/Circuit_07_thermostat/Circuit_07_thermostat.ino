/*

Example sketch 07

TEMPERATURE SENSOR

  Use the "serial monitor" window to read a temperature sensor.
  
  The TMP36 is an easy-to-use temperature sensor that outputs
  a voltage that's proportional to the ambient temperature.
  You can use it for all kinds of automation tasks where you'd
  like to know or control the temperature of something.
  
  More information on the sensor is available in the datasheet:
  http://dlnmh9ip6v2uc.cloudfront.net/datasheets/Sensors/Temp/TMP35_36_37.pdf

  Even more exciting, we'll start using the Arduino's serial port
  to send data back to your main computer! Up until now, we've 
  been limited to using simple LEDs for output. We'll see that
  the Arduino can also easily output all kinds of text and data.
  
Hardware connections:

  Be careful when installing the temperature sensor, as it is
  almost identical to the transistors! The one you want has 
  a triangle logo and "TMP" in very tiny letters. The
  ones you DON'T want will have "222" on them.

  When looking at the flat side of the temperature sensor
  with the pins down, from left to right the pins are:
  5V, SIGNAL, and GND.
  
  Connect the 5V pin to 5 Volts (5V).
  Connect the SIGNAL pin to ANALOG pin 0.
  Connect the GND pin to ground (GND).

This sketch was written by SparkFun Electronics,
with lots of help from the Arduino community.
This code is completely free for any use.
Visit http://www.arduino.cc to learn about the Arduino.

Version 2.0 6/2012 MDG
*/

// We'll use analog input 0 to measure the temperature sensor's
// signal pin.

const int temperaturePin = 0;
const int ledPin = 13;
float setTemp = 25.0; // degress C, STP

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete


void setup()
{
  // In this sketch, we'll use the Arduino's serial port
  // to send text back to the main computer. For both sides to
  // communicate properly, they need to be set to the same speed.
  // We use the Serial.begin() function to initialize the port
  // and set the communications speed.
  
  // The speed is measured in bits per second, also known as
  // "baud rate". 9600 is a very commonly used baud rate,
  // and will transfer about 10 characters per second.
  
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}


void loop()
{

  float voltage, degreesC, degreesF;

  voltage = getVoltage(temperaturePin);
  
  // Now we'll convert the voltage to degrees Celsius.
  // This formula comes from the temperature sensor datasheet:

  degreesC = (voltage - 0.5) * 100.0;
  
  // While we're at it, let's convert degrees Celsius to Fahrenheit.
  // This is the classic C to F conversion formula:
  
  degreesF = degreesC * (9.0/5.0) + 32.0;
  
  Serial.print("voltage: ");
  Serial.print(voltage);
  Serial.print("  deg C: ");
  Serial.print(degreesC);
  Serial.print("  deg F: ");
  Serial.println(degreesF);

  if (degreesC < setTemp)  // could add hystersis here 
  {
    Serial.println("turn heater on");  
  } else
  {
    Serial.println("turn heater off");
  }

   if (stringComplete) {
    Serial.print("Setting Temperature to: ");
    setTemp = inputString.toFloat();
    Serial.println(setTemp);
    // clear the string:
    inputString = "";
    stringComplete = false;
  }

  // These statements will print lines of data like this:
  // "voltage: 0.73 deg C: 22.75 deg F: 72.96"

  // Note that all of the above statements are "print", except
  // for the last one, which is "println". "Print" will output
  // text to the SAME LINE, similar to building a sentence
  // out of words. "Println" will insert a "carriage return"
  // character at the end of whatever it prints, moving down
  // to the NEXT line.
   
  delay(1000); // repeat once per second (change as you wish!)
}


float getVoltage(int pin)
{
  // This function has one input parameter, the analog pin number
 
  return (analogRead(pin) * 0.004882814);
  
  // This equation converts the 0 to 1023 value that analogRead()
  // returns, into a 0.0 to 5.0 value that is the true voltage
  // being read at that pin.
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
// Other things to try with this code:

//   Turn on an LED if the temperature is above or below a value.

//   Read that threshold value from a potentiometer - now you've
//   created a thermostat!

