import json
import random

QUIZ_FILE = "data.json"


def load_quiz_file():
    """Load quiz content from a JSON file."""
    try:
        with open(QUIZ_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"{QUIZ_FILE} not found. Make sure it exists.")
        return {}


def list_topics(quiz_content):
    """Display available quiz topics."""
    print("\nAvailable Topics:")
    for index, topic in enumerate(quiz_content.keys(), 1):
        print(f"{index}. {topic}")
    return list(quiz_content.keys())


def start_quiz(topic, player_name, quiz_content):
    """Run the quiz for a selected topic."""
    print(f"\n{player_name}, welcome to the {topic} quiz!")
    if topic not in quiz_content:
        print(f"No questions available for the topic: {topic}.")
        return

    score = 0
    questions = random.sample(quiz_content[topic], min(len(quiz_content[topic]), 5))

    for i, question in enumerate(questions, 1):
        print(f"\nQ{i}: {question['q']}")
        for option_index, option in enumerate(question["o"], 1):
            print(f"{option_index}. {option}")
        try:
            answer = int(input("Choose your answer (1/2/3/4): "))
            if question["o"][answer - 1] == question["a"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {question['a']}")
        except (ValueError, IndexError):
            print("Invalid choice. Skipping this question.")

    print(f"\nYour total score: {score}/{len(questions)}. Well done, {player_name}!")


def main():
    """Main function to drive the application."""
    print("Welcome to the Quiz Game!")
    quiz_content = load_quiz_file()

    if not quiz_content:
        print("No quiz data found. Exiting.")
        return

    users = {}
    logged_in_user = None

    # User Registration and Login
    while not logged_in_user:
        print("\n1. Register\n2. Login\n3. Exit")
        action = input("Select an option: ")
        if action == "1":
            username = input("Choose a username: ")
            if username in users:
                print("Username already exists. Try logging in.")
            else:
                password = input("Set a password: ")
                users[username] = password
                print("Registration successful!")
        elif action == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if users.get(username) == password:
                print("Login successful!")
                logged_in_user = username
            else:
                print("Invalid username or password.")
        elif action == "3":
            print("Exiting the application. Thank you!")
            return
        else:
            print("Invalid choice. Please try again.")

    # Quiz Menu
    while True:
        topics = list_topics(quiz_content)
        topic_choice = input(f"Select a topic (1-{len(topics)}): ")
        if topic_choice.isdigit() and 1 <= int(topic_choice) <= len(topics):
            selected_topic = topics[int(topic_choice) - 1]
            start_quiz(selected_topic, logged_in_user, quiz_content)
        else:
            print("Invalid topic selection. Please try again.")

        play_again = input("Do you want to take another quiz? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thankyou")
            break


if __name__ == "__main__":
    main()