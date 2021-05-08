/*
 * A library for the 4 digit display
 *
 * Copyright (c) 2012 seeed technology inc.
 * Website    : www.seeed.cc
 * Author     : Frankie.Chu
 * Create Time: 9 April,2012
 * Change Log :
 *
 * The MIT License (MIT)
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
 
#include <TimerOne.h>
#include "TM1637.h"
#define ON 1
#define OFF 0

int8_t WhiteTimeDisp[] = {0x00,0x00,0x00,0x00};
int8_t BlackTimeDisp[] = {0x00,0x00,0x00,0x00};
bool isWhite = 1;
bool WhiteLost = false;
bool BlackLost = false;
unsigned char WhiteClockPoint = 1;
unsigned char BlackClockPoint = 1;
unsigned char WhiteUpdate;
unsigned char BlackUpdate;
unsigned char WhitetenthOfSecond = 0;
unsigned char BlacktenthOfSecond = 0;
unsigned char Whitesecond = 0;
unsigned char Blacksecond = 0;
unsigned char Whiteminute = 1;
unsigned char Blackminute = 1;


#define WhiteCLK 6         //pins definitions for TM1637 and can be changed to other ports
#define WhiteDIO 7
#define BlackCLK 8        
#define BlackDIO 9

TM1637 WhiteClock(WhiteCLK,WhiteDIO);
TM1637 BlackClock(BlackCLK,BlackDIO);

void setup()
{
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
  WhiteClock.set();
  WhiteClock.init();
  
  BlackClock.set();
  BlackClock.init();
  
  WhiteTimeDisp[0] = Whiteminute / 10;
  WhiteTimeDisp[1] = Whiteminute % 10;
  WhiteTimeDisp[2] = Whitesecond / 10;
  WhiteTimeDisp[3] = Whitesecond % 10;
  WhiteClock.display(WhiteTimeDisp);
  
  BlackTimeDisp[0] = Blackminute / 10;
  BlackTimeDisp[1] = Blackminute % 10;
  BlackTimeDisp[2] = Blacksecond / 10;
  BlackTimeDisp[3] = Blacksecond % 10;
  BlackClock.display(BlackTimeDisp);

  attachInterrupt(digitalPinToInterrupt(2), turnChange, FALLING ); 
  delay(1000);
  
  Timer1.initialize(100000);              //timing for 100ms
  Timer1.attachInterrupt(TimingISR);     //declare the interrupt serve routine:TimingISR
}

void loop()
{
  if(WhiteLost == true)
  {
    Serial.println("White lost the game on time");
    /*
    digitalWrite(LED_BUILTIN, HIGH);   
    delay(500);                       
    digitalWrite(LED_BUILTIN, LOW);  
    delay(500);
    */
  }
  
  if(BlackLost == true)
  {
    Serial.println("Black lost the game on time");
    /*
    digitalWrite(LED_BUILTIN, HIGH);   
    delay(1000);                       
    digitalWrite(LED_BUILTIN, LOW);  
    delay(1000);
    */
  }
  if(isWhite == 1)
  {
    if(WhiteUpdate == ON)
      {
        TimeUpdate();
        WhiteClock.display(WhiteTimeDisp);
      }
  }
  else
  {
    if(BlackUpdate == ON)
      {
        TimeUpdate();
        BlackClock.display(BlackTimeDisp);
      }
  }
  
}

void turnChange()
{
  if (isWhite) isWhite = 0;
  else isWhite = 1;
}

void TimingISR()
{ 
  if(isWhite == 1 and BlackLost == false and WhiteLost == false)
    {
      WhitetenthOfSecond ++;
      WhiteUpdate = ON;
      if(WhitetenthOfSecond == 10){
        
        if(Whitesecond == 0)
        {
          
          if(Whiteminute == 0  and Whitesecond == 0)
          {
            WhiteLost = true;
            Whitesecond = 0;
            Whiteminute = 0;
          }
          else
          {
            Whiteminute --;
            Whitesecond = 59;
          }
        }
        else{
        Whitesecond --;}
        WhitetenthOfSecond = 0;
      }
     // Serial.println(second);
      WhiteClockPoint = (~WhiteClockPoint) & 0x01;
    }
  else if(BlackLost == false and WhiteLost == false)
    {
      BlacktenthOfSecond ++;
      BlackUpdate = ON;
      if(BlacktenthOfSecond == 10){
        
        if(Blacksecond == 0)
        {
          
          if(Blackminute == 0 and Blacksecond == 0)
          {
            BlackLost = true;
            Blacksecond = 0;
            Blackminute = 0;
          }
          else
          {
            Blackminute --;
            Blacksecond = 59;
          }
          
        }
        else{
        Blacksecond --;}
        BlacktenthOfSecond = 0;
      }
     // Serial.println(second);
      BlackClockPoint = (~BlackClockPoint) & 0x01;
    }
}

void TimeUpdate(void)
{
  if(isWhite == 1)
    { 
      if(WhiteClockPoint)WhiteClock.point(POINT_ON);
      else WhiteClock.point(POINT_OFF);
      WhiteTimeDisp[0] = Whiteminute / 10;
      WhiteTimeDisp[1] = Whiteminute % 10;
      WhiteTimeDisp[2] = Whitesecond / 10;
      WhiteTimeDisp[3] = Whitesecond % 10;
      WhiteUpdate = OFF;
    }
  else
    { 
      if(BlackClockPoint)BlackClock.point(POINT_ON);
      else BlackClock.point(POINT_OFF);
      BlackTimeDisp[0] = Blackminute / 10;
      BlackTimeDisp[1] = Blackminute % 10;
      BlackTimeDisp[2] = Blacksecond / 10;
      BlackTimeDisp[3] = Blacksecond % 10;
      BlackUpdate = OFF;
    }
}
