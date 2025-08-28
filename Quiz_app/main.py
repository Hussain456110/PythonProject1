import json

def load_questions(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except:
        print("Error: Could not load questions.")
        return []

def quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        print("Options:", ", ".join(q["options"]))
        ans = input("Your answer: ")
        if ans.lower() == q["answer"].lower():
            print("Correct ✅")
            score += 1
        else:
            print("Wrong ❌. Correct:", q["answer"])
    print(f"\nYour Score: {score}/{len(questions)}")

quiz(load_questions("questions.json"))
