import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import openai
import os
from dotenv import load_dotenv
load_dotenv()

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "5c2508270add455386bd318b0ea4f189"

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

def speak(text, voice="Samantha"):  # You can change voice here!
    os.system('say -v {} "{}"'.format(voice, text))



openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure to load this from a .env file
if not openai.api_key:
    raise Exception("OpenAI API key not found. Please check your .env file.")

def aiProcess(command):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Lyra. You are helpful, quick, and smart. Answer briefly."},
            {"role": "user", "content": command}
        ]
    )

    return response['choices'][0]['message']['content']


def processCommand(c):
    #command for opening link
    if "Open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "Open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "Open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "Open Github" in c.lower():
        webbrowser.open("https://Github.com")
    # Music library
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        print("fething news")
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey={}".format(newsapi))
        if r.status_code == 200:
            # parse the json response
            data = r.json()

            #extract the articles
            articles = data.get('articles',[])

            #print the headlines
            for article in articles[:5]:
                speak(article['title'])

    else:
        #let open AI handle the request
        output = aiProcess(c)
        speak(output)
        

if __name__ == "__main__":
    speak("Initializing lyra")
    while True:
        #listen for the wake word "Lyra"
        #obtain audio from the microphone
        r = sr.Recognizer()
            
        print("recognizing...")

            #recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening")
                #voice clarity 
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=3, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower() == "lyra"):
                speak("Yaa, I'm active")
                #listen for command
                with sr.Microphone() as source:
                    print("lyra active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("User's Command:", command)


                    processCommand(command)
                    print("👉 Command received inside processCommand:", command)
        except Exception as e:
            print(" Couldn't understand your voice. Please try again.")
            
                    


