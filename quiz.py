import random

# Questions database
questions = {
    "technical": {
        "l1": [
            ("What does HTML stand for?", "HyperText Markup Language"),
            ("What is the basic unit of data storage in a computer?", "Bit"),
            ("What does CPU stand for?", "Central Processing Unit"),
            (
                "What programming language is known for its use in web development?",
                "JavaScript",
            ),
        ],
        "l2": [
            ("Difference between HTTP and HTTPS?", "encryption"),
            ("Purpose of a CDN (Content Delivery Network)?", "performance"),
            ("Difference between RAM and ROM?", "volatile"),
            ("What is the use of a VPN?", "security"),
        ],
        "l3": [
            ("What is the CAP theorem in distributed systems?", "consistency"),
            ("Explain the concept of blockchain in one word.", "decentralization"),
            ("What is a quantum computer's main advantage?", "speed"),
            ('What does the term "machine learning bias" refer to?', "data"),
        ],
    },
    "sports": {
        "l1": [
            ("Which sport uses a shuttlecock?", "badminton"),
            ("How many players are there in a basketball team?", "five"),
            ("Who is known as the fastest man alive?", "bolt"),
            ("Which sport is played at Wimbledon?", "tennis"),
        ],
        "l2": [
            ('Which sport is the "national game" of India?', "hockey"),
            (
                "Who was the captain of the Indian cricket team when they won the 1983 Cricket World Cup?",
                "kapil dev",
            ),
            ("Which city hosted the Commonwealth Games in India in 2010?", "delhi"),
            (
                "Who was the first Indian female athlete to win an Olympic medal?",
                "karnam malleswari",
            ),
        ],
        "l3": [
            (
                "Who was the first Indian cricketer to score a triple century in Test cricket?",
                "virender sehwag",
            ),
            (
                "Which Indian athlete won the gold medal in the javelin throw at the 2020 Tokyo Olympics?",
                "neeraj chopra",
            ),
            ("Which country has won the most FIFA World Cup titles?", "brazil"),
            (
                "Who holds the record for the most Grand Slam singles titles in tennis (men's singles)?",
                "roger federer",
            ),
        ],
    },
    "maths": {
        "l1": [
            ("10 - 7 =", "3"),
            ("4 * 4 =", "16"),
            ("6 + 8 =", "14"),
            ("9 / 3 =", "3"),
        ],
        "l2": [
            ("Square root of 225?", "15"),
            ("5 * (1 + 9) =", "50"),
            ("Value of x: 2x + 5 = 15", "5"),
            ("Circumference of a circle with radius 5?", "31.42"),
        ],
        "l3": [
            ("Value of x: log₂(x) = 3", "8"),
            (
                "What is the area of a circle with radius 6 units (in square units)?",
                "113.04",
            ),
            ("What is the sum of the interior angles of a hexagon?", "720 degrees"),
            ("Evaluate the limit: lim(x -> 0) (sin(x) / x)", "1"),
        ],
    },
}


def ask_question(question, answer):
    user_answer = input(f"{question} ").strip().lower()
    return user_answer == answer.lower()


def quiz(topic, difficulty):
    selected_questions = questions[topic][difficulty]
    random.shuffle(selected_questions)
    score = 0

    for question, answer in selected_questions:
        if ask_question(question, answer):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{answer}'.")

    print(f"Total Score: {score}/{len(selected_questions)}")


def main():
    print("Welcome to the Quiz!")
    topic = input("Choose a topic (technical/sports/maths): ").strip().lower()
    while topic not in questions:
        topic = (
            input("Topic not available. Choose again (technical/sports/maths): ")
            .strip()
            .lower()
        )

    difficulty = input("Choose difficulty level (l1/l2/l3): ").strip().lower()
    while difficulty not in questions[topic]:
        difficulty = (
            input("Invalid difficulty level. Choose again (l1/l2/l3): ").strip().lower()
        )

    quiz(topic, difficulty)


if __name__ == "__main__":
    main()
