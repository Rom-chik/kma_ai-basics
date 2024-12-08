#made by Roman Antoshchuk on 20.09.2024
# NOT A MEDICAL ADVISOR!!! 
import time
import json
import random
import re


def load_intents(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: Firstaid file not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Could not decode JSON.")
        return None


def rand_choice(answers):
    return random.choice(answers)


def find_answer(user_input, data, dont_understand_counter):
    user_input = user_input.lower()  # Ensure case-insensitivity

    if user_input == "/start":
        return "Chat started", 0

    for intent in data['intents']:
        for pattern in intent["patterns"]:
            # check for pattern
            if re.search(r"\b" + re.escape(pattern.lower()) + r"\b", user_input):
                dont_understand_counter = 0

                # check for anti context words
                context = intent.get("context_set", "")
                anti_context = intent.get("anti_context_set", "-")
                if context in user_input and anti_context != "-":
                    if anti_context not in user_input:
                        # replace where necessary * with word
                        return rand_choice(intent["answers"]).replace("*", pattern), dont_understand_counter
                else:
                    return rand_choice(intent["answers"]).replace("*", pattern), dont_understand_counter

    #counter to make bot give up on 3rd time
    dont_understand_counter += 1
    if dont_understand_counter > 2:
        return "Stop playing with me. I'm first aid bot and don't have time for this games", 0
    else:
        return rand_choice(data['intents'][-1]["answers"]), dont_understand_counter


# chat def
def chat(data):
    print("Chatbot is running! Type '/start' to begin or type 'exit' to quit.")
    dont_understand_counter = 0

    while True:
        user_input = input("You: ").lower()
        # stop word / exit
        if user_input == 'bye' or user_input == 'goodbye':
            print("Goodbye!")
            break

        # response
        answer, dont_understand_counter = find_answer(user_input, data, dont_understand_counter)
        time.sleep(0.5)
        print("Bot: " + answer)


intents_data = load_intents('firstaid.json')
if intents_data:
    chat(intents_data)
