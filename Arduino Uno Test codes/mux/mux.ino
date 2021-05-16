//Mux control pins
int s0 = 8;
int s1 = 9;
int s2 = 10;
int s3 = 11;

//Mux in "SIG" pin
int SIG_pin = A3;

bool F = true;
  
void setup(){
  pinMode(s0, OUTPUT); 
  pinMode(s1, OUTPUT); 
  pinMode(s2, OUTPUT); 
  pinMode(s3, OUTPUT); 
  pinMode(SIG_pin, INPUT_PULLUP);
  pinMode(13, OUTPUT);
  digitalWrite(s0, LOW);
  digitalWrite(s1, LOW);
  digitalWrite(s2, LOW);
  digitalWrite(s3, LOW);
  
  Serial.begin(9600);

}


void loop(){
while(F)
{
  //Loop through and read all 16 values
  //Reports back Value at channel 6 is: 346
  for(int k = 0; k<2 ; k++){ 
  for(int i = 0; i < 8; i ++){

    Serial.print(readMux((k*8) + i));
    Serial.print(" ");
    delay(50);
  }
  Serial.println();
  }
  F = false;
}
}


int readMux(int channel){
  int controlPin[] = {s0, s1, s2, s3};

  int muxChannel[16][4]={
    {0,0,0,0}, //channel 0
    {1,0,0,0}, //channel 1
    {0,1,0,0}, //channel 2
    {1,1,0,0}, //channel 3
    {0,0,1,0}, //channel 4
    {1,0,1,0}, //channel 5
    {0,1,1,0}, //channel 6
    {1,1,1,0}, //channel 7
    {0,0,0,1}, //channel 8
    {1,0,0,1}, //channel 9
    {0,1,0,1}, //channel 10
    {1,1,0,1}, //channel 11
    {0,0,1,1}, //channel 12
    {1,0,1,1}, //channel 13
    {0,1,1,1}, //channel 14
    {1,1,1,1}  //channel 15
  };

  //loop through the 4 sig
  for(int i = 0; i < 4; i ++){
    digitalWrite(controlPin[i], muxChannel[channel][i]);
  }
  digitalWrite(13, HIGH);
delay(1000);
digitalWrite(13, LOW);
  //read the value at the SIG pin
  int val = !digitalRead(SIG_pin);

  //return the value
  return val;
}
