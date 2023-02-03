#This Program was inspired by a video made by neural nine

from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import webbrowser

recognizer = speech_recognition.Recognizer() 

speaker = tts.init()
speaker.setProperty('rate', 150)

todo_list = ['Go shopping', 'Clean Room', 'Record  Video']

def create_note():
    global recognizer 

    speaker.say("What do you want to write on your note?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Choose a filename!")

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say(f"I successfully created the note {filename}")
                speaker.runAndWait()


        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand, say it again")
            speaker.runAndWait()

def add_todo(): 

    global recognizer

    speaker.say("What todo do you want to add?")
    speaker.runAndWait()

    done = False
    
    while not done:

        try: 
            
            with speech_recognition.Microphone() as mic: 

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                
                item = recognizer.recognize_google(audio)
                item = item.lower()

                todo_list.append(item)
                done = True
                
                speaker.say(f"I added {item} to the to do list")
                speaker.runAndWait()
       
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand, say it again")
            speaker.runAndWait()
            
def show_todos():

    speaker.say("The items on your to do list are the following")
    for item in todo_list:
        speaker.say(item)

    speaker.runAndWait()

def hello():
    speaker.say("Hello. What can I do for you?")
    speaker.runAndWait()

def dictionary():
   

    global recognizer

    speaker.say("What word would you like me to look up?")
    speaker.runAndWait()    

    done = False
    
    while not done:

        try: 
            
            with speech_recognition.Microphone() as mic: 

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                
                query = recognizer.recognize_google(audio)
                query = query.lower()

                
                if(len(query.split()) == 1):

                    webbrowser.open('https://www.dictionary.com/browse/' + query)
                    done = True
                
                    speaker.say(f"I searched the word up for you")
                    speaker.runAndWait()
       
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand, say it again")
            speaker.runAndWait()

def google():
   

    global recognizer

    speaker.say("What should I search for you?")
    speaker.runAndWait()    

    done = False
    
    while not done:

        try: 
            
            with speech_recognition.Microphone() as mic: 

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                
                query = recognizer.recognize_google(audio)
                query = query.lower()

                query = query.replace(" ", "+")
                

                webbrowser.open('https://www.google.com/search?q=' + query)
                done = True
                
                speaker.say(f"I googled it for you")
                speaker.runAndWait()
       
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand, say it again")
            speaker.runAndWait()

def search_map():

    global recognizer

    speaker.say("What location do you want me to find?")
    speaker.runAndWait()    

    done = False
    
    while not done:

        try: 
            
            with speech_recognition.Microphone() as mic: 

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                
                query = recognizer.recognize_google(audio)
                query = query.lower()

                query = query.replace(" ", "+")
                
                

                webbrowser.open('https://www.google.com/maps/place/?q=' + query)
                done = True
                
                speaker.say(f"I searched the location up for you")
                speaker.runAndWait()
       
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand, say it again")
            speaker.runAndWait()

def quit():
    speaker.say("Bye")
    speaker.runAndWait()
    sys.exit(0)

mappings = {
    'search_google' : google,
    'create_note' : create_note,
    'add_todo' : add_todo,
    'show_todos' : show_todos,
    'find_on_map' : search_map,
    'search_dictionary' : dictionary,
    'exit' : quit
}

assistant = GenericAssistant('intents.json', intent_methods =mappings, model_name="speech_assistant_model")
assistant.train_model()
assistant.save_model()

print("model has finished training")

hello()

while True:

    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()

            assistant.request(message)
    except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            

