while True:
    name = input('Please type your name: ')

    if name == 'your name':
        print('Congratulations you figured it out! Now, let\'s try a riddle or two.')
        break

# Define a list of riddles and their corresponding answers.
riddles = [
    {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "answer": "echo"},
    {"question": "What has keys but can't open locks?", "answer": "piano"},
    {"question": "I'm tall when I'm young and short when I'm old. What am I?", "answer": "candle"},
    # Add more riddles here
]

def play_riddle_game():
    score = 0
    for riddle in riddles:
        print("Riddle:")
        print(riddle["question"])
        guess = input("Your answer: ").lower()

        if guess == riddle["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. Try the next riddle.\n")

    print(f"You answered {score}/{len(riddles)} riddles correctly!")

if __name__ == "__main__":
    print("Welcome to the Riddle Game!\n")
    play_riddle_game()
# add a delay to keep the window open
input("Press Enter to exit...")
