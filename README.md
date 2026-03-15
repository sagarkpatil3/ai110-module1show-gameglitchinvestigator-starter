# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- **Purpose**: A refined number guessing game built to demonstrate state management and logical debugging in Streamlit.
- **Bugs Found**: Incorrect difficulty ranges (Hard was easier than Normal), inconsistent score penalties, attempt penalties for invalid inputs, and secret number desync on difficulty change.
- **Fixes Applied**: Core logic refactored into `logic_utils.py`, consistent scoring logic implemented, input validation added before attempt increment, and difficulty-based state reset implemented.

## 📸 Demo

![Winning Game Screenshot](file:///Users/sagarpatil/.gemini/antigravity/brain/93682b39-af95-4cdd-b2a4-ade881d0e46c/winning_screen_1773547199477.png)

## 🚀 Stretch Features

- [x] **Automated Tests**: Expanded `pytest` suite covering all core logic functions.
- [x] **State Stability**: Verified secret number persistence across interactions.
