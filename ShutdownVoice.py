#ALL THE LIBRARIES USED
import os
import pyttsx3
import speech_recognition as sr


#CLASS
class AutoSHUT:
    
    #choices command as input
    def takeCommands(self):

        r = sr.Recognizer
        with sr.Microphone as source:
            print('Listening')

            r.pause_threshold = 0.7
            audio = r.listen(source)

            #Voice is Identified
            try:


                print("Recognizing")
                Query = r.recognize_google(audio,language='en-in')

                print("The Query Is Printed",Query,"'")

            except Exception as e:

                print(e)

                print("Please Say It Again")
                return "None"
        return Query

    #Method For Voice Output
    def Speak(self,audio):

        #Constructor Call for pyttsx3.init
        engine = pyttsx3.init('sapi5')

        #Setting Voice Typed And ID
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    def quitSelf(self):
        self.Speak("Would You Like To Shut Down Your PC ?")

        #Input Voice Command
        take = self.takeCommands()
        choise = take
        if choise == 'Yes':

            #For SHutdown
            print("Wait A Moment,Shutting Down Your Computer")
            self.Speak("Shutting Down The Computer")
            os.system("shutdown /s /t 30")
        if choise == 'No':
             # Idle
            print("Shutdown Cancelled")
            self.Speak("Shut Down Cancelled")


#Driver Code
if __name__ == '__main__':
    Maam = AutoSHUT()
    Maam.quitSelf()

