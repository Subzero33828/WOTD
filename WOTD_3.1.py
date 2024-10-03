import requests
from bs4 import BeautifulSoup
import random
from datetime import date
print(date.today())
from twilio.rest  import Client 
from email.mime.text import MIMEText
import smtplib
import schedule
import time


# Constantes pour Twilio et email
TWILIO_ACCOUNT_SID = 'ACe0513e604e5c2e3e7af87582486a1253'
TWILIO_AUTH_TOKEN = 'ecc19521ddac85ffc83a139b576f5df0'
FROM_NUMBER = '+1 844 459 0221' 
TO_NUMBER = '+1 267 282 1075' 
EMAIL_SENDER = 'subzero33828@gmail.com'
EMAIL_RECIPIENT = 'shamarbrowne@gmail.com'
SMTP_SERVER = 'smtp.gmail.com' 
SMTP_PORT = 587  #??? Define
EMAIL_PASSWORD = 'your_email_password' 

#url = input("Please enter the url to fetch French words: ")  # Ask the user to input the url
url = 'https://www.vistawide.com/french/top_100_french_words.htm'

def fetch_french_words(url: str) -> list[str]:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, features='html.parser')
        word_list = soup.find_all('li')  # Ajustez en fonction du site web réel
        return [word.get_text() for word in word_list]
    else:
        print("Échec de la récupération des mots.")
        return []


def get_word_of_the_day(words: list[str] ) ->  str:
    if not words:
        print("Aucun mot disponible.")
        return "Aucun mot disponible."
    return random.choice(seq=words)  # Sélectionnez un mot aléatoire dans la liste


def send_sms(word_of_the_day: str):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            from_=FROM_NUMBER,
            body=f"Le mot du jour d'aujourd'hui est : {word_of_the_day}",
            to=TO_NUMBER
        )
        print(f"Message envoyé : {message:str}")
    except Exception as e:
        print(f"Échec de l'envoi du SMS : {e}")


def send_email(word_of_the_day: str):
    msg = MIMEText(f"Le mot français d'aujourd'hui est : {word_of_the_day}")
    msg['Subject'] = 'Mot du Jour'
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECIPIENT

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(user=EMAIL_SENDER, password=EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECIPIENT, msg.as_string())
        print("Email envoyé avec succès.")
    except Exception as e:
        print(f"Échec de l'envoi de l'email : {e}")

 
def main(url: str) -> None:
    french_words = fetch_french_words(url)
    if french_words:
        word_of_the_day = get_word_of_the_day(words=french_words)
        print(f"Mot du jour : {word_of_the_day}")
       # Represent SMS and email actions as strings
        sms_message = f"Le mot du jour d'aujourd'hui est : {word_of_the_day}"
        email_message = f"Le mot français d'aujourd'hui est : {word_of_the_day}"

        # Log or print the messages instead of sending them
        print(f"SMS to be sent: {sms_message}")
        print(f"Email to be sent: {email_message}")


# Planifiez la fonction principale pour qu'elle s'exécute quotidiennement
schedule.every().day.at("09:00").do(main, url) # type: ignore   # Définissez l'heure à laquelle vous souhaitez que le travail s'exécute
#schedule.every().day.at("18:00").do(main, url)  # Essai d'ajouter un deuxième message

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)  # Attendez une minute avant de vérifier à nouveau









