from random import randint
import pyttsx3
from playsound import playsound

def happy():
    facts = [
        "Grapes light on fire in the microwave.",
        "There are almost 8 million possible seven-digit phone numbers per area code.",
        "Spaghetto, confetto, and graffito are the singular forms of spaghetti, confetti, and graffiti.",
        "McDonald\'s once created bubblegum-flavored broccoli.",
        "The average mammal takes 21 seconds to empty its bladder.",
        "Chewing gum is banned in Singapore.",
        "The average U.S. household has 300,000 things in it.",
        "The 1939 novel Gadsby is the longest book ever published that doesn\'t contain the letter \'e.\'",
        "Lobsters have clear blood.",
        "The first item sold on eBay was a broken laser pointer."
    ]
    engine = pyttsx3.init()
    str = facts[randint(0, 10)]
    engine.say(str)
    print(str)
    engine.runAndWait()

def sad():
    playsound('I-Was-Always-Right-Here.mp3')

def neutral():
    quotes = [
        "The purpose of our lives is to be happy. — Dalai Lama.",
        "Life is what happens when you\'re busy making other plans. — John Lennon.",
        "Get busy living or get busy dying. — Stephen King.",
        "You only live once, but if you do it right, once is enough. — Mae West.",
        "Many of life\'s failures are people who did not realize how close they were to success when they gave up.– Thomas A. Edison",
        "If you want to live a happy life, tie it to a goal, not to people or things.– Albert Einstein",
        "Never let the fear of striking out keep you from playing the game.– Babe Ruth",
        "Money and success don\'t change people; they merely amplify what is already there. — Will Smith",
        "Your time is limited, so don\'t waste it living someone else\'s life. Don\'t be trapped by dogma – which is living with the results of other people\'s thinking. – Steve Jobs",
        "Not how long, but how well you have lived is the main thing. — Seneca"
    ]
    engine = pyttsx3.init()
    str = quotes[randint(0, 10)]
    engine.say(str)
    print(str)
    engine.runAndWait()

def angry():
    jokes = [
        'Why was 6 afraid of 7? Because 7 ate 9',
        'I\'m reading an antigravity book. It\'s impossible to put down!',
        'What kind of cheese doesn\'t belong to you? Nacho cheese!',
        'You can\'t trust atoms. They make up everything!',
        'Why do mushrooms get invited to all the best parties? Because they are such fungis!',
        'Two men walk into a bar. The third one ducks!',
        'Why did the dog cross the road? To get to the barking lot!',
        'Why do potatoes argue? Because they can\'t see eye to eye!',
        'Can February March? No, but April May!',
        'What kind of dog does Dracula have? A bloodhound!'
    ]
    engine = pyttsx3.init()
    str = jokes[randint(0, 10)]
    engine.say(str)
    print(str)
    engine.runAndWait()

def surprise():
    engine = pyttsx3.init()
    str = "Please have a seat, you look surprised!"
    engine.say(str)
    print(str)
    engine.runAndWait()