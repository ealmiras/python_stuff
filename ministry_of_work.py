from textblob import TextBlob
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello Employee Number 42546346. We hope you had a great day of work. It's time to submit your employee wellness statement")
engine.runAndWait()

print("Enter your employee wellness statements: ")
phrase = input("> ")
blob = TextBlob(phrase)
while blob.sentiment.polarity < 0.5:
    engine.say("Employee Number 42546346, that was not a very positive statement. Please try again.")
    engine.runAndWait()
    print("More positive please: ")
    phrase = input("> ")
    blob = TextBlob(phrase)
print("We appreciate you too!")
engine.say("Employee Number 42546346, thank you for such a kind and positive statement! We here at the ministry of work appreciate you too. Have a great day!")
engine.runAndWait()
