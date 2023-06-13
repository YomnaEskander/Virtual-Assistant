from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts #covert text into speech
import sys #part of python used to exist 
import pyjokes
import webbrowser
import os
import random
import datetime

recognizer = speech_recognition.Recognizer() #recognizer is a method in the speech recognition class

speaker = tts.init() #this is for speaking the text 
speaker.setProperty('rate', 150)

todo_list=['']


def create_note():
    global recognizer
    print("what do you want to write in your note?")
    speaker.say("what do you want to write in your note?")
    speaker.runAndWait()

    done = False
     
    while not done :
        try:
            with speech_recognition.Microphone() as mic:
                
               recognizer.adjust_for_ambient_noise(mic,duration=0.6)#will recognize if we're talking aslun wala la
               audio =  recognizer.listen(mic)# once it recognizes that we are talking, it saves the talking fel variable audio
               #this loop takes input from us using.mic and try block processes the input
               #recognizer.listen(mic) takes our input
               note = recognizer.recognize_google(audio)#this one extracts the text from the audio using google
               note = note.lower()#this makes all the text in lower case
               
               speaker.say("choose a filename")
               speaker.runAndWait()
               
               recognizer.adjust_for_ambient_noise(mic,duration=0.6)
               audio = recognizer.listen(mic)
               
               filename = recognizer.recognize_google(audio)
               filename = filename.lower() #n7awwel el note l file
               #this loop creates a note by making a file that has a note or text in i
            with open(filename,"w") as f :
                f.write(note)
                done = True
                speaker.say(f"I succeefully created the note {filename}")
                speaker.runAndWait()
               
        except speech_recognition.UnknownValueError:
           recognizer=speech_recognition.Recognizer()
           speaker.say("i didn't understand you!please try again!")
           speaker.runAndWait()
    
def add_todo():

    global recognizer
    print("what task do you want to add?")
    speaker.say("what task do you want to add?")
    speaker.runAndWait()

    done = False
    
    while not done :   
        try:
        
            with speech_recognition.Microphone() as mic:
               
               recognizer.adjust_for_ambient_noise(mic,duration=0.2)
               audio =  recognizer.listen(mic)
               
               item = recognizer.recognize_google(audio)
               item = item.lower()
               
               todo_list.append(item)
               done = True
               
            speaker.say(f"I added {item} to the to do list!")
            speaker.runAndWait() 
            
        except speech_recognition.UnknownValueError:
         recognizer = speech_recognition.Recognizer()
         print("I did not understand please say again")
         speaker.say("I did not understand please say again")
         speaker.runAndWait()            


def show_todo_list():
    
    print("The items in your todo list are the following")
    speaker.say("The items in your todo list are the following")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()

def tellDay():
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
      
    #this line tells the number 
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speaker.say("Today is " + day_of_the_week)

def function_of_greetings():
    print("Hello Ms")
    speaker.say("Hello Miss")
    print("Hope you're having a good day")
    speaker.say("Hope you're having a good day")
    tellDay()
    speaker.say("how may i help you")
    speaker.runAndWait()

def function_joke():
    print("here's a really funny one")
    speaker.say("here's a really funny one")
    My_joke = pyjokes.get_joke(language="en", category="all")
    speaker.say(My_joke)
    speaker.runAndWait()

def function_google():
    print("Opening Google ")
    speaker.say("Opening Google ")
    webbrowser.open("www.google.com")
    speaker.runAndWait()   
    
def function_music():
    print('Playing music...')
    speaker.say("Here's an amazing tune...")
    path = 'C:/Users/PC/Desktop/my stuff/My media/Songs/songsoldies'
    song = os.listdir(path)
    rand_No = random.randint(0, 55)
    os.startfile(os.path.join(path, song[rand_No]))
    speaker.runAndWait()
    
def function_whou():
    print("I am Salem, your really smart assistant Ms")
    speaker.say("I am Salm, your really smart assistant Miss")
    speaker.runAndWait()    
    

def function_goodbye():
    print("Goodbye Ms")
    speaker.say("Goodbye Miss")
    speaker.runAndWait()
    sys.exit(0)

   

mappings = {
"greeting": function_of_greetings,
"exit": function_goodbye,
"create_note":create_note,
"add_todo": add_todo,
"show_todo": show_todo_list,
"joke": function_joke,
"google":function_google,
"music":function_music,+
"whou":function_whou, 
"tellDay": tellDay,
}    


#to train the model b2a ML
Salem = GenericAssistant('C:/Users/PC/Desktop/my stuff/SalemModel/myintents.json', intent_methods=mappings)
Salem.train_model() #the model is trained


while True:

    try:
        with speech_recognition.Microphone() as mic:
    
            recognizer.adjust_for_ambient_noise(mic,duration=0.6)
            audio = recognizer.listen(mic)
    
            message = recognizer.recognize_google(audio)
            message = message.lower()
            print("listening")
    
        Salem.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
