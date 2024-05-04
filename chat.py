import re
import random
import json

with open('intents.json', 'r') as f:
    intents = json.load(f)


def get_response(msg):
    # Iterate over the intents
    for intent in intents['intents']:
        # For each pattern in the intent's patterns
        for pattern in intent['patterns']:
            # Check if the pattern matches the message
            if re.search(f".* {pattern} .*", msg, re.IGNORECASE):
                # If a pattern matches, select a random response
                return random.choice(intent['responses'])
    # Default response if no pattern matches
    return "I'm not sure how to respond to that."
