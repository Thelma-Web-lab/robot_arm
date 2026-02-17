#include <Servo.h>

Servo myServo;

void setup() {
  myServo.attach(9); // Attach servo signal to Pin 9
}

void loop() {
  // Swing to 0 degrees
  myServo.write(0);
  delay(1000);

  // Swing to 90 degrees
  myServo.write(90);
  delay(1000);

  // Swing to 180 degrees
  myServo.write(180);
  delay(1000);
}
