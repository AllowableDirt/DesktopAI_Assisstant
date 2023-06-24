import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai
import datetime
import random
from config import apikey


chatstr = ""

# function to create chat
def chat(query):
    global chatstr
    print(chatstr)
    openai.api_key = apikey
    chatstr += f"Oni Chan: {query.removesuffix('using AI')}\nKyojuro Rengoku: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # todo: wrapping  in a try catch because sometimes no choice is available.
    # try:

    # Prints the response too and the above function stores them in a file
    say(response["choices"][0]["text"])
    chatstr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('ai')[:20]).removesuffix('using AI')}.txt", "w") as f:
        f.write(text)



    # Function to generate and print the response from ai
def ai(prompt):
    openai.api_key = apikey
    text = f"Openai response for Prompt:{prompt} \n ------------------------------\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt.removesuffix('using AI'),
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    #todo: Wrapping  in a try catch because sometimes no choice is available.
    # try:

    # Prints the response too and the above function stores them in a file
    print(response["choices"][0]["text"])
    text+= response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('ai')[:20]).removesuffix('using AI')}.txt", "w") as f:
        f.write(text)


#say function to give the audio output
def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

        # creating error scenarios while taking audio input
        try:
            query = r.recognize_google(audio, language ="en-in")
            print(f"User said: {query}")
            return query

        except Exception as e:
            return "Some error occured, khee khee khee"


# main function
print( "main function is running" )
#taking textual input and return audio ouput
text = " Kon'nichiwa, I'm Rengoku Kyojuro, What can I do for you"
say(text)
# taking audio command and returning as output

#to take multiple inputs
while True:
    print('Listening.......')
    query = takecommand()
    #say(query)
    print('Recognizing.......')
    #opening various commonly used sites
    sites=[['youtube',"https://youtube.com"],['google','https://google.com'],['Whatsapp','https://web.whatsapp.com/'],['hindu','https://thehindu.com'],'linkedin',"https://linkedin.com"]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            say(f'[Opening {site[0]} Bhai')
            webbrowser.open(site[1])


    #todo: add playlists and add option to play in a loop or random manner
    if "open favourite music" in query:
            musicPath= r"C:\Users\abhis\OneDrive\Pictures\Screenshots\hanuman.m4a"
            os.startfile(musicPath)


    #todo: more ways of reciting time can be added
    elif "the time" in query:
        strfTime = datetime.datetime.now().strftime("%H hours++   %M minutes and %S seconds")
        say(f"Bhai time horha hai:{strfTime}")


    #todo: add the feature to open andy windows apps
    #opening apps not working because of unable to accsess path og program files.
    elif "open spotify".lower() in query.lower():
        os.system(r"C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.213.661.0_x86__zpdnekdrzrea0\Spotify.exe")


    #todo: this feature has been added for genereting the respinses using AI, here the function is being called!!!
    elif "ai".lower() in query.lower():
        ai(prompt = query)

    elif "reset".lower() in query.lower():  # To reset the chat
        chatstr = ""

    elif "quit".lower() in query.lower():  # To exit the desktop assistant
        exit()

    else:
        print('Kyojuro Speaking.......')
        chat(query)







