import time


#Ini class buat gerakannya aja
#Bukan ini yang bakal di run
class Movements:
    def __init__(self) :
        pass
    def grab(self,servo):
        for i in range(0,360):
            servo.write(i)
            time.sleep(0.015)
    def open(self,servo):
       for i in range(360,1,-1):
           servo.write(i)
           time.sleep(0.015)
    def clawTest(self,servo):
        for i in range(0,180):
            servo.write(i)
            time.sleep(0.015)
        for i in range(180,1-1):
            servo.write(i)
            time.sleep(0.015)
    def rotate(self,servo):
        for i in range(0,90):
            servo.write(i)
            time.sleep(0.015)
    def monitor(self,servo):
        for i in range(0,2): #jalan dua kali
            for i in range(0,90):
                servo.write(i)
                time.sleep(0.015)
            for i in range(90,1,-1):
                servo.write(i)
                time.sleep(0.015)     
    def lift(self,servo):
         for i in range(120,180):
                servo.write(i)
                time.sleep(0.0015) 
    def down(self,servo):
        for i in range(180,120,-1):
                servo.write(i)
                time.sleep(0.0015)    
    def updown(self,servo):
        for i in range(0,2):
            for i in range(180,120,-1):
                servo.write(i)
                time.sleep(0.0015)   
            for i in range(120,180):
                servo.write(i)
                time.sleep(0.0015)   
         
        