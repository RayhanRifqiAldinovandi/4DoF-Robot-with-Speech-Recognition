from pyfirmata import Arduino
import speech_recognition as sr
from movements import Movements 

#Create an object of the speech recognition class
r = sr.Recognizer()
#Create microphone object
mic = sr.Microphone(device_index=1)

#Board initialization
board = Arduino("COM6")
#pin
servoClaw = board.get_pin("d:3:s")
servoBody = board.get_pin("d:4:s")
servoArm1 = board.get_pin("d:6:s")
servoArm2 = board.get_pin("d:9:s")
#Create an object of the movements class
move = Movements()

#Dictionary containing a list of commands
speech_dict = {'grab':lambda:move.grab(servoClaw),
               'open':lambda:move.open(servoClaw),
               'rotate':lambda:move.rotate(servoBody),
               'monitor':lambda:move.monitor(servoBody),
               'higher':lambda:move.lift(servoArm1),
               'lower':lambda:move.down(servoArm1),
               'down up':lambda:move.updown(servoArm1)}


servoArm1.write(180)
servoClaw.write(0)
while True:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Say something....")
        audio = r.listen(source,timeout=5,phrase_time_limit=3)
    try:
        text = r.recognize_google(audio)
        if text in speech_dict: #If the spoken text is in the dictionary
            print(f"Executing command: {text}")
            speech_dict[text]() #Do the action
        else:
            #kalo kata yang diucapkan nggak ada di speech_dict
            print(f"Command unrecognized: {text}")
    except KeyboardInterrupt:
        # servoArm1.write(120)
        # servoArm2.write(180)
        print("Application exited")
    except:
        #kalo gak ada suara
        print("No Audio")