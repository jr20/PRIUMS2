int humidity; 
int temperature;
char buffer[60];
void setup() {
  Serial.begin(9600);
}

void loop() {
  humidity = random(0,100);
  temperature = random(0,50);
  sprintf(buffer,"%d  %d\n",humidity,temperature);
  Serial.write(buffer);
  delay(1000);
}
