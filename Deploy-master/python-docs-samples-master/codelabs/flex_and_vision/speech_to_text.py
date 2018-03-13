import speech_recognition as sr

import random
from gtts import gTTS
from time import sleep
import time
import os




#--method to convert text from speech----#
def speech_to_text_():
    msg=""
    try:
        print("A moment of silence, please...")
        r = sr.Recognizer()
        print(sr)

        m = sr.Microphone()
        
        with m as source: r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            print("Say something!")
            with m as source: audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)

                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                    print(u"You said {}".format(value).encode("utf-8"))
                    msg=value
                    break
                    
                else:  # this version of Python uses unicode for strings (Python 3+)
                    print("You said {}".format(value))
                    msg=value
                    break   

                    
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
                break
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
                break
    except KeyboardInterrupt:
        pass
    except:
        #return "cannot find microphone"
        pass
    return msg

#----method to convert speech from texr---#
def text_to_speech(value):
    
    print(format(value).encode("utf-8"))
    tts = gTTS(value, lang='en')
    str1 =str(random.random())
    str2 = ".mp3"
    filename=str1+str2
    print(filename)

    tts.save(filename)
    os.system(filename)
    os.remove(filename)
    
        
