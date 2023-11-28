from freeGPT import AsyncClient
from asyncio import run
import mysql.connector
import speech_recognition as sr
import pyttsx3
import winsound


async def main():
    while True:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="sakila"
        )
        d = {}
        mycursor2 = mydb.cursor()
        mycursor2.execute("show tables")
        res = mycursor2.fetchall()
        k = []
        for tab in res:
            k.append(tab[0])
            mycursor1 = mydb.cursor()
            l = []
            mycursor1.execute("SHOW COLUMNS FROM %s" % tab[0])
            results = mycursor1.fetchall()
            for row in results:
                l.append(row[0])
            d[k[-1]] = l

        mycursor = mydb.cursor()
        l = []
        mycursor.execute("SHOW COLUMNS FROM %s" % tab[0])
        results = mycursor.fetchall()
        for row in results:
            l.append(row[0])

        recognizer = sr.Recognizer()
        mic = sr.Microphone()

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)

        while True:
            choice = int(input('''
MENU
1. Voice input
2. Text input
3. Exit
'''))

            if choice == 1:
                try:
                    with mic as source:
                        print("Ask for the information that you would like to retrieve", end=" ")
                        engine.say('Ask for the information that you would like to retrieve')
                        engine.runAndWait()
                        print(":")
                        winsound.PlaySound("Chimes", winsound.SND_ALIAS)
                        recognizer.adjust_for_ambient_noise(source, duration=0.2)
                        recognizer.dynamic_energy_threshold = True
                        audio = recognizer.listen(source, 3, 10)
                        audioText = recognizer.recognize_google(audio)
                        print(audioText)
                        audioText = audioText.lower()
                        if audioText in ["exit", "break", "leave", "end", "quit"]:
                            break
                except:
                    print("Could not recognize speech")
                    continue
            elif choice == 2:
                audioText = input("Enter the information you would like to retrieve: ")
                audioText = audioText.lower()
                if audioText in ["exit", "break", "leave", "end", "quit"]:
                    break
            elif choice == 3:
                return
            else:
                print("Invalid choice. Please select 1, 2, or 3.")

            # Getting response
            a = f"convert the following into an SQL query: {audioText} if the dictionary provided is {d} which consists of the table name on the left and the column names on the right. Use the information accordingly. I want only the SQL query and nothing else. Do not type anything except the query."
            try:
                resp = await AsyncClient.create_completion("gpt3", a)
                print(resp)
                mycursor.execute(resp)
                results = mycursor.fetchall()
                for row in results:
                    print(row)
            except Exception as e:
                print(f"🤖: {e}")


if __name__ == "__main__":
    run(main())