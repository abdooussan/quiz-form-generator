from Quiz import  Quiz_Generator
import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import flet as ft
import tempfile




def Generator(page):
    # Initialiser le reconnaisseur
    r = sr.Recognizer()
    #  sets the sampling rate to 44100 samples per second,
    fs = 44100  

    # line sets the duration of the recording to 8 seconds.
    seconds = 8  

    # Commencer l'enregistrement
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)

    # Attendez que l'enregistrement soit terminé
    sd.wait()  
  
    # Créez un fichier temporaire avec une extension .wav pour stocker l'audio
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        audio_file = tmpfile.name
        sf.write(tmpfile.name, recording, fs)
    recognizer = sr.Recognizer()
    # Create an AudioFile object to represent the audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        #text = recognizer.recognize_google(audio_data)
        text = r.recognize_google(audio_data)
        print(text)
    def open_url(e):
        page.launch_url(e.data)
    page.add(ft.Text("here is the google form Link:  ",  style=ft.TextThemeStyle.HEADLINE_SMALL))
    page.add(
        ft.Markdown(
            Quiz_Generator(text),
            on_tap_link=open_url,
            extension_set="gitHubWeb",
            expand=True)
    )



def main(page):
    Text = ft.Text("Quiz IA Generator", size=70, weight=ft.FontWeight.W_900, selectable=True)
    def start_recording(e):
            page.clean()
            page.add(Text, ft.ElevatedButton("Stop Record", on_click=stop_recording))
            Generator(page)

            
    def stop_recording(e):
             page.clean()
             # Open the audio file
             page.add(Text, ft.ElevatedButton("Record", on_click=start_recording))

    

    #page.add(ft.ElevatedButton("Record", on_click=start_recording))

    button = ft.ElevatedButton("Record", on_click=start_recording)
    button.align_self = "center"
    # Add the button to the page.
    page.add(Text, button)


ft.app(target=main, view=ft.WEB_BROWSER) 

