import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()
r.energy_threshold = 700
r.dynamic_energy_threshold = True
start_message = "Hey, I'm Jarvis , your personal assistant. Say 'Hey Jarvis' before your request to activate me."
wakeword = "hey jarvis"
error_message = "Sorry, I don't recognize your voice. Please try again!!!"
print(start_message)
engine.say(start_message)
engine.runAndWait()
print()
print("Listening...")

objects  = ['person', 'phone', 'bottle', 'laptop', 'dog', 'cat']
def VoiceDetect(mic, wakeword = 'hey jarvis'):
    try:
        with mic as source:
            print("...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout = 5)
        output = r.recognize_google(audio).lower()
        if wakeword in output:
            a=True
        else:
            a=False
    except sr.UnknownValueError:
        output = error_message
        a = False
    except sr.WaitTimeoutError:
        output = error_message
        a = False
    return (output, a)

def Commands(inp):
    if 'find' in inp or 'where' in inp:
        for obj in objects:
            if obj in inp:
                return (obj,"clf")
            elif obj not in inp:
                return ("That object is not in my database", "")
    elif "assist" in inp:
        return ("assist", "clf")
    elif "how are you" in inp:
        return ("Hi, I am doing great", "clf")
    elif "exit" in inp:
        return ("Bye, Have a nice day !!", "exit")
    elif "who are you" in inp or "what are you" in inp:
        return (start_message, "")
    else:
        return("Sorry, I did not understand. Please try again !!")

def Output(txt = ""):
    engine.say(txt)
    engine.runAdWait()


    
            
    

















        
        
        
