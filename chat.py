import re
import random
from answers import pronounces, responses


# This function takes a string fragment, splits it into tokens,
# and replaces any token found in the pronounces dictionary with its corresponding value.
# It then joins the tokens back into a string and returns it.
def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in pronounces:
            tokens[i] = pronounces[token]
    return ' '.join(tokens)


# This function takes a message as input, iterates over the responses list,
# and tries to match the message with each pattern in the list.
# If a match is found, it selects a random response from the corresponding list of answers,
# reflects any groups in the match, and formats the response with these reflected groups.
# It then returns the formatted response.
def get_response(msg):
    for pattern, answers in responses:
        # Remove punctuation and match the pattern
        match = re.match(pattern, msg.rstrip(".!"))
        if match:
            response = random.choice(answers)
            return response.format(*[reflect(g) for g in match.groups()])
