import random

# Create a variable to store the user's name
user_name = None
actual_name = None
game_started = False
riddle_pool = []  # Initialize an empty riddle pool

# Define a list of riddles and their corresponding answers.
all_riddles = [
    {"question": "What gets wet while drying?", "answer": "towel"},
    {"question": "What can you catch, but not throw?", "answer": "cold"},
    {"question": "What can travel all around the world without leaving its corner?", "answer": "stamp"},
    {"question": "I'm always hungry, I must always be fed. The finger I touch will soon turn red. What am I?", "answer": "Fire"},
    {"question": "The more you take, the more you leave behind. What am I?", "answer": "footsteps"},
    {"question": "I'm a word of letters three, add two and fewer there will be. What am I?", "answer": "few"},
    {"question": "The more you have of it, the less you see. What is it?", "answer": "Darkness"},
    {"question": "I have keys but open no locks. I have space but no room. You can enter, but you can't go inside. What am I?", "answer": "Keyboard"},
    {"question": "What is full of holes but still holds water?", "answer": "sponge"},
    {"question": "What goes up but never comes down?", "answer": "age"},
    {"question": "David's parents have three sons: Snap, Crackle, and what's the name of the third son?", "answer": "David"},
    {"question": "What has one head, one foot and four legs?", "answer": "bed"},
    {"question": "What has roots as nobody sees, is taller than trees, up, up it goes, and yet never grows?", "answer": "mountain"},
    {"question": "What has words, but never speaks?", "answer": "book"},
    {"question": "It stalks the countryside with ears that can't hear. What is it?", "answer": "corn"},
    {"question": "If there are three apples and you take away two, how many apples do you have?", "answer": "two"},
    {"question": "What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?", "answer": "river"},
    {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "answer": "echo"},
    {"question": "What has keys but can't open locks?", "answer": "piano"},
    {"question": "I'm tall when I'm young and short when I'm old. What am I?", "answer": "candle"},
        # Add more riddles here
]

def select_riddles():
    # Shuffle the riddle pool
    random.shuffle(all_riddles)
    # Select a subset of questions (e.g., 5 questions) from the shuffled pool
    return all_riddles[:5]

while not game_started:
    if user_name is None:
        user_name = input('Please type your name: ')

    # Check if the user entered "your name" to start the game
    if user_name.lower() == 'your name':
        game_started = True
    else:
        # Set actual_name to user_name if it's not empty
        if user_name:
            actual_name = user_name
            user_name = None

if actual_name is None:
    actual_name = "RiddleMaster"

print(f'Congratulations {actual_name}, you figured it out! Now for the real riddles. One word answers only. Good Luck!')

def play_riddle_game():
    selected_riddles = select_riddles()  # Select random riddles for the game
    score = 0
    for riddle in selected_riddles:
        print("Riddle:")
        print(riddle["question"])
        guess = input("Your answer: ").strip().lower()
        answer = riddle["answer"].strip().lower()

        if guess == answer:
            print("Correct!\n")
            score += 1
        else:
            show_answer = input("Incorrect. Would you like to see the correct answer? (y/n): ").lower()
            if show_answer == "y":
                print(f"The correct answer is: {riddle['answer']}\n")

    print(f"You answered {score}/{len(selected_riddles)} riddles correctly!")

if __name__ == "__main__":
    while True:
        play_riddle_game()

        play_again = input(f"{actual_name}, would you like to play again? (y/n): ").lower()
        if play_again != "y":
            break
