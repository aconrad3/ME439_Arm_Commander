int turntable_A0_pin = A0; 
int shoulder_A1_pin = A1; 
int elbow_A2_pin = A2; 
int forearm_A3_pin = A3; 
int wristud_A4_pin = A4; 
int wristrot_A5_pin = A5; 


int turntable_A0 = 0;
int shoulder_A1 = 0;
int elbow_A2 = 0;
int forearm_A3 = 0;
int wristud_A4 = 0;
int wristrot_A5 = 0;

int shoulder_Servo = 0;
int elbow_Servo = 0;
int forearm_Servo = 0;
int wristud_Servo = 0;

void setup(){
  Serial.begin(9600);
}

void loop(){
  turntable_A0 = analogRead(turntable_A0_pin);
  shoulder_A1 = analogRead(shoulder_A1_pin);
  elbow_A2 = analogRead(elbow_A2_pin);
  forearm_A3 = analogRead(forearm_A3_pin);
  wristud_A4 = analogRead(wristud_A4_pin);
  wristrot_A5 = analogRead(wristrot_A5_pin);

  turntable_A0 = turntable_A0 - 151;
  
  if(shoulder_A1 > 635){
    shoulder_A1 = 635;
  }
  else if (shoulder_A1 < 320){
    shoulder_A1 = 320;
  }

  elbow_A2 = elbow_A2-500;
  if(elbow_A2 <=0){
    elbow_A2 = 0;
  }

  if(wristud_A4 > 930){
    wristud_A4 = 930;
  }
  else if (wristud_A4 < 215){
    wristud_A4 = 215;
  }


  elbow_A2 = 500-elbow_A2;

  wristud_A4 = 1023 - wristud_A4;

  wristrot_A5 = wristrot_A5 - 162;
  
  if(wristrot_A5 <=0){
    wristrot_A5 = 0;
  }
  

  shoulder_Servo = (((((shoulder_A1/10) - 32)*23)/31.5)+25)*10;
  elbow_Servo = (((((elbow_A2/10) - 23)*26)/23)+14)*10;
  forearm_Servo = (((((forearm_A3/10) - 21)*41)/70.5)+14.5)*10;
  wristud_Servo = (((((wristud_A4/10) - 21.5)*45.5)/71.5)+14.5)*10;
  
  
  // Serial.println(shoulder_Servo);
  // Serial.println(elbow_Servo);
  // delay(100);

  //  if(turntable_A0 > 600){
  //    turntable_A0 = 600;
  //  }
  //  else if (turntable_A0 < 135){
  //    turntable_A0 = 135;
  //  }
  //
  //  if(shoulder_A1 > 500){
  //    shoulder_A1 = 500;
  //  }
  //  else if (shoulder_A1 < 280){
  //    shoulder_A1 = 280;
  //  }
  //
  //  if(elbow_A2 > 420){
  //    elbow_A2 = 420;
  //  }
  //  else if (elbow_A2 < 190){
  //    elbow_A2 = 190;
  //  }
  //
  //  if(forearm_A3 > 600){
  //    forearm_A3 = 600;
  //  }
  //  else if (forearm_A3 < 100){
  //    forearm_A3 = 100;
  //  }
  //
  //  if(wristud_A4 > 640){
  //    wristud_A4 = 640;
  //  }
  //  else if (wristud_A4 < 160){
  //    wristud_A4 = 160;
  //  }
  //
  //  if(wristrot_A5 > 650){
  //    wristrot_A5 = 650;
  //  }
  //  else if (wristrot_A5 < 140){
  //    wristrot_A5 = 160;
  //  }




  Serial.println(String(turntable_A0) + "_" + String(shoulder_Servo) + "_" + String(elbow_Servo) + "_" + String(forearm_Servo) + "_" + String(wristud_Servo) + "_" + String(wristrot_A5));
  delay(50);
}


