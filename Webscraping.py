# I want to do a fench word of the day bot
# I hope this will lead me to build a phrase of the day bot to learn french and maybe even a tiktok a day app
# I also want to make my own version of goodrerads!
# I want to use BeautifulSoup to do this im just not sure what it is.



# Sure! I can guide you through building a simple "Word of the Day" bot in Python using web scraping. We'll use a common library like BeautifulSoup to scrape a website. Here's a step-by-step guide:

# Tools Needed:
# Requests: To fetch the HTML content from a webpage.
# BeautifulSoup: To parse the HTML and extract the information we need.
# First, you'll need to install the required libraries:

# bash
# Copy code
# pip install requests beautifulsoup4
# Step 1: Find a Website with a List of Words
# You need a website that lists the 100 most used French words. Let's assume you found a page that has such a list. For this example, let's say we have a website like https://example.com/french-words.

# Step 2: Fetch the Page Content
# We will use requests to fetch the HTML content of the webpage.

from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')
    
import requests

url = 'https://www.linguasorb.com/french/verbs/most-common-verbs/1'  
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("C'est Fait!")
else:
    print("J'ai echoue, reessaye!")
    
# Step 3: Parse the HTML Using BeautifulSoup
# Once the page is fetched, we can parse it to find the list of French words.

from bs4 import BeautifulSoup

# Parse the content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Assuming the words are in a list with <li> tags
word_list = soup.find_all('li')  # You may need to inspect the website to get the exact tag

# Extract text from each <li> element
french_words = [word.get_text() for word in word_list]

# Print the first few words
print(french_words[:10])

# Step 4: Select a "Word of the Day"
# Now that we have a list of words, let's pick one randomly each day.    
    
import random
from datetime import date

def get_word_of_the_day(words):
    # Get the current day as an integer (e.g., day 1, 2, etc.)
    today = date.today().day
    return words[today % len(words)]  # Modulus to cycle through words based on the day

# Get the word of the day
word_of_the_day = get_word_of_the_day(french_words)
print(f"Word of the day: {word_of_the_day}")
    
    
    
    
 #in the og code i got from chatgpt they wanted to Step 5: Automate the Bot
# You can automate the bot to run daily, perhaps sending the "Word of the Day" to you via email, a chat app, or a notification.
# Here's a basic example of how you can send it via email. 
#This is cool and all but I want to do this as a push notification/ txtmsg through TWILIO nxt time

import smtplib
from email.mime.text import MIMEText

def send_email(word_of_the_day):
    # Email details
    sender = 'your_email@example.com'
    recipient = 'recipient_email@example.com'
    subject = 'Word of the Day: ' + word_of_the_day
    body = f"Today's French word is: {word_of_the_day}"

    # Create the email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Send the email
    with smtplib.SMTP('smtp.example.com', 587) as server:  # Use your email provider's SMTP settings
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.sendmail(sender, recipient, msg.as_string())

# Send the word of the day
send_email(word_of_the_day)


# Notes:
# Inspect the Website Structure: You may need to inspect the website structure using browser developer tools (right-click -> "Inspect") to find the correct HTML tags where the words are located.
# Error Handling: Add appropriate error handling in case the website structure changes or the page fails to load.
# Automation: You can use a task scheduler like cron (Linux) or Task Scheduler (Windows) to run the bot daily.
