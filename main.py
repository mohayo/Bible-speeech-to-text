import speech_recognition as sr

def search_verse(verse, text_file_path):
    # Convert "psalms" to "psalm" (singular form)
    if "psalms" in verse.lower():
        verse = verse.replace("psalms", "psalm")
    # Capitalize the first letter of the verse
    verse = verse.capitalize()
    print(f'Searching for verse: {verse}')
    
    # Search for the verse in the text file
    with open(text_file_path, 'r') as bible:
        verse_found = False
        for line in bible:
            if verse in line:
                print(line)
                verse_found = True
                break

        if not verse_found:
            print("Verse not found.")

def callback(recognizer, audio):
    try:
        print("Listening...")
        voice_data = recognizer.recognize_google(audio)
        print("Recognized:", voice_data)
        search_verse(voice_data, "/Users/ayobami/Text_to_speech/Bible Versions/kjv.txt")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    print("Say the verse you want to search for (e.g., Psalm 18:2)")
    
stop_listening = r.listen_in_background(mic, callback)

# Keep the main thread running to allow background listening
while True:
    pass
