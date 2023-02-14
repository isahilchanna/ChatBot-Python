import random
import wikipedia as wp
import time

GREETINGS_INPUTS = ("hello", "hi", "hey", "greetings", "sup", "what's up",)
GREETINGS_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

INQUIRY_INPUTS = ["how are you", "how are you?", "how are you doing", "how are you doing?","how you doing","how you doing?"]
INQUIRY_RESPONSES = ["I'm good, thanks for asking!", "I'm great", "I'm doing well, thanks!", "I'm okay, thanks for asking."]

OTHER_INPUTS=["nice","good","great"]
OTHER_RESPONSES=["yes","yeah"]

OTHER2_INPUTS=["how about your friends?","have you any friends?","do you have any friends?"]
OTHER2_RESPONSES=["i don\'t have any friends expect you❤️"]

QUES_INPUTS=["can i ask you a question?","can i ask you something?"]
QUES_RESPONSES = [
    "Of course! What would you like to know?",
    "Sure, go ahead and ask your question.",
    "Absolutely, I'm here to help. What's on your mind?",
    "Yes, please feel free to ask me any question.",
    "Sure thing! What's your question?",
    "Absolutely, I'd be happy to help. What's your question?",
    "Of course, what's on your mind?"
]

def greetings(sentence):
    for word in sentence.split():
        if word.lower() in GREETINGS_INPUTS:
            return random.choice(GREETINGS_RESPONSES)

def inquiry(sentence):
    for phrase in INQUIRY_INPUTS:
        if phrase in sentence:
            return random.choice(INQUIRY_RESPONSES)

def Others(sentence):
    for phrase in OTHER_INPUTS:
        if phrase in sentence:
            return random.choice(OTHER_RESPONSES)

def Others2(sentence):
    for phrase in OTHER2_INPUTS:
        if phrase in sentence:
            return random.choice(OTHER2_RESPONSES)

def Ques(sentence):
    for phrase in QUES_INPUTS:
        if phrase in sentence:
            return random.choice(QUES_RESPONSES)


def generate_response(user_input):
    user_input = user_input.lower()
    response = " "
    if greetings(user_input) != None:
        response = greetings(user_input)
        return response
    elif inquiry(user_input)!= None:
        response = inquiry(user_input)
        return response
    elif Others(user_input)!=None:
        response=Others(user_input)
        return response
    elif Others2(user_input)!=None:
        response=Others2(user_input)
        return response
    elif Ques(user_input)!= None:
        response=Ques(user_input)
        print(response)
        user_ques=input("your question please:")
        result=wp.search(user_ques)
        print("Ans:",wp.summary(result[0],sentences=3))
        time.sleep(4)
    else:
        return response
        

        
##    else:
##        response = "I am sorry, I don't understand you."
print("Hello i\'m BRAVO the chat bot!")


while True:
    user_input = input("You: ")
    if user_input == "exit":
        print("~Thank you for using us")
        break
    print("Bot: ", generate_response(user_input))
