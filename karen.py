import pyttsx3
import speech_recognition as sr
import karen_training as kt

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=3000
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print("You said", query)
        speak(f"You said {query}")
    except Exception:
        print("Can you please rephrase it sir?")
        speak("Can you please rephrase it sir?")
        return "Null"
    return query

if __name__=="__main__":
    kt.wishme()
    
    while True:
        query=takecommand()
        query=query.lower()

        if 'stop execution' in query:
            speak("Execution set to halt")
            speak(kt.stop())
            exit()
            continue

        if 'open google' in query:
            kt.open_google()
            continue
        elif 'close google' in query:
            kt.close()
            continue
        elif 'open youtube' in query:
             kt.open_youtube()
             continue
        elif 'close youtube' in query:
            kt.close()
            continue
        elif 'open 10 fast fingers' in query:
            kt.open_10fastfingers()
            continue
        elif 'closed tab' in query:
            speak("Tab closed")
            kt.close()
            continue
        elif 'open code' in query:
            kt.open_code()
            continue
        elif 'open wordpad' in query:
            kt.open_wordpad()
            continue
        elif 'music' in query:
            kt.music()
        elif 'day' in query:
            kt.day()
        elif 'date' in query:
            kt.date()
        elif 'time' in query:
            kt.time()
        elif 'search for' in query:
            query=query.replace('search for','')
            if 'karen' in query:
                query=query.replace('karen','')
            kt.google_it(query)
            speak("Here are the results for your search sir")
        elif 'wikipedia' in query:
            query=query.replace('wikipedia','')
            kt.Wikipedia(query)


