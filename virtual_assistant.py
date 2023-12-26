import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1 ].id)

class bella:
    def speak(self,audio):
            engine.say(audio)
            engine.runAndWait()
            
    def wishme(self):
            print("The phrases in the program: \nwho are you\nwhat can you do\nopen google\nopen youtube\ntime now\nplay rockpaperscissors\n")
            hour = int(datetime.datetime.now().hour)
            if hour >=0 and hour<12:
                self.speak("good morning")
            elif hour >= 12 and hour<18:
                self.speak ("good afternoon")
            else:
                self.speak("good evening")
            self.speak("i am bella sir")
            self.speak("how can i help you")
            
    def takecommand(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration = 2)
            print("listening...")
            audio = r.listen(source)
        try:
            print("recognizing..")
            query = r.recognize_google(audio,language = "en-in")
            print(f"user said:{query}")
        except:
            print("say that again")
            return "None"
        return query

import random

class stonepaperscissor(bella):
    def __inint__(self):
        self.user_score=0
        self.computer_score=0

    def play(self):
        while True:
            print(f"user score= {self.user_score},computer score = {self.user_score}")
            choice = self.takecommand().lower()

            options = ["stone","paper","scissors"]

            if "quit game" in choice :
                break
            elif choice in options:
                print("invalid entry")
                continue
            computer_choice = random.choice(options)
            print(f"computer = {computer_choice}")
            self.speak(f"computer choice = {computer_choice}")

            if choice== computer_choice:
                print("tie")
            elif choice =="stone" and computer_choice == "scissors":
                    print("user won")
                    self.user_score+=1
                
            elif choice =="paper" and computer_choice == "stonr":
                    print("user won")
                    self.user_score+=1
            elif choice =="scissors" and computer_choice == "paper":
                    print("user won")
                    self.user_score+=1
            else:
                    print("computer won")
                    self.computer_score+=1

            if self.user_score == 3:
                    print("congrats,you won")
                    self.speak("congrats,you won")
                    break
            elif self.computer_score == 3:
                    print("congrats,computer won")
                    self.speak("congrats,computer won")
                    break
ai= bella()

ai.wishme()
while True:
    query = ai.takecommand().lower()

    if "who are you" in query :
        ai.speak("i am your virtual assistant sir ,my name is bella")
    elif "what can you do" in query:
        ai.speak("i can search google ")
    elif "sleep" in query :
        break
    elif "open youtube" in query :
        webbrowser.open("youtube.com")
        ai.speak("DO YOU WANT ME to search")
        a = ai.takecommand().lower()
        if "yes" in a:
            while True:
                ai.speak("listening..")
                s= ai.takecommand().lower()
                if "close" in s:
                    ai.speak("exiting google..")
                    break
                elif "none" not in s:
                    webbrowser.open_new_tab(f"http://www.youtube.com/search?q={s}")
    elif "open google" in query :
        webbrowser.open("google.com")
        ai.speak("DO YOU WANT ME to search")
        a = ai.takecommand().lower()
        if "yes" in a:
            while True:
                ai.speak("listening..")
                s= ai.takecommand().lower()
                if "close" in s:
                    ai.speak("exiting google..")
                    break
                elif "none" not in s:
                    webbrowser.open_new_tab(f"http://www.google.com/search?q={s}")
    elif "time now" in query :
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        ai.speak(f"sir the time now is {time_now}")

    elif "play game" in query:
        ai.speak("lets play stone paper scissor game")
        game = stonepaperscissor()
        game.play()
