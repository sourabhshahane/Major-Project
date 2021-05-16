//Mux control pins
const int S0 = 8;
const int S1 = 9;
const int S2 = 10;
const int S3 = 11;

//Mux in "SIG" pin
const int SIG_1 = A1;
const int SIG_2 = A2;
const int SIG_3 = A3;
const int SIG_4 = A4;

bool F = true;

bool output[4][16];

void setup(){
  pinMode(S0, OUTPUT); 
  pinMode(S1, OUTPUT); 
  pinMode(S2, OUTPUT); 
  pinMode(S3, OUTPUT); 

  digitalWrite(S0, LOW);
  digitalWrite(S1, LOW);
  digitalWrite(S2, LOW);
  digitalWrite(S3, LOW);

  Serial.begin(9600);

}


void loop(){
while(F)
{

  for(int i = 0 ; i < 16 ; i++)
  {
    readMux(i);
  }
  
  for(int j = 0 ; j < 4 ; j++)
  {
    for(int k = 0; k < 2 ; k++)
    { 
      for(int i = 0; i < 8; i ++)
      {
        Serial.print(output[j][(8*k) + i]);
        Serial.print("  ");
      }
      Serial.println();
    }
    F = false;
     
    }
    Serial.println();
  }
 
}

int readMux(int channel)
{
  int controlPin[] = {S0, S1, S2, S3};
  int signalPin[] = {SIG_1, SIG_2, SIG_3, SIG_4};

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
  for(int i = 0; i < 4; i ++)
  {
    digitalWrite(controlPin[i], muxChannel[channel][i]);
  }
  delay(50);
  //read the value at the SIGNAL pins
  for(int i = 0; i < 4; i ++)
  { 
    output[i][channel] = !digitalRead(signalPin[i]);
  }
}
