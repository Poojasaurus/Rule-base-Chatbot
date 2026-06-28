import random

INTENTS = {
    "greeting": {
        "keywords": [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ],
        "responses": [
            "Hello! 👋",
            "Hi there! 😊",
            "Hey! Nice to see you.",
            "Welcome! How can I help you today?"
        ]
    },

    "how_are_you": {
        "keywords": [
            "how are you",
            "how are you doing",
            "how do you feel"
        ],
        "responses": [
            "I'm doing great!",
            "I'm always ready to help.",
            "Fantastic! Thanks for asking."
        ]
    },

    "name": {
        "keywords": [
            "what is your name",
            "who are you"
        ],
        "responses": [
            "I'm DecodeBot Pro.",
            "My name is DecodeBot Pro."
        ]
    },

    "creator": {
        "keywords": [
            "who made you",
            "who created you"
        ],
        "responses": [
            "I was created using Python as a Rule-Based AI Chatbot."
        ]
    },

    "python": {
        "keywords": [
            "python"
        ],
        "responses": [
            "Python is a powerful programming language widely used for AI, automation and web development."
        ]
    },

    "ai": {
        "keywords": [
            "ai",
            "artificial intelligence"
        ],
        "responses": [
            "Artificial Intelligence enables computers to perform tasks that normally require human intelligence."
        ]
    },

    "machine_learning": {
        "keywords": [
            "machine learning",
            "ml"
        ],
        "responses": [
            "Machine Learning is a branch of AI where computers learn patterns from data."
        ]
    },

    "joke": {
        "keywords": [
            "joke",
            "tell me a joke"
        ],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
            "Why did Python break up with Java? It found someone less complicated. 😄",
            "Debugging is like being a detective in a crime movie where you're also the murderer. 😂"
        ]
    },

    "motivation": {
        "keywords": [
            "motivate me",
            "motivation",
            "motivate"
        ],
        "responses": [
            "Success is built one small step at a time.",
            "Consistency beats talent when talent isn't consistent.",
            "Keep learning. Your future self will thank you."
        ]
    },

    "thanks": {
        "keywords": [
            "thanks",
            "thank you"
        ],
        "responses": [
            "You're welcome! 😊",
            "Happy to help!",
            "Anytime!"
        ]
    }
}


def get_response(user_input):
    user_input = user_input.lower().strip()

    for intent in INTENTS.values():

        for keyword in intent["keywords"]:

            if keyword in user_input:

                return random.choice(intent["responses"])

    return "Sorry, I don't understand that. Type 'help' to see available commands."