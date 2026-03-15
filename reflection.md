# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- The game had several logical and UI-related issues that made it confusing or unfair.
- **Incorrect Difficulty Range**: The "Hard" difficulty range (1-50) was actually smaller and thus easier than the "Normal" difficulty range (1-100).
- **Inconsistent Score Logic**: The score would sometimes increase when a "Too High" guess was made depending on the attempt number, which is counter-intuitive for a penalty.
- **Attempt Penalty for Invalid Guesses**: Entering a non-numeric guess still counted as an attempt, punishing the user for typos.
- **Secret Number Desync**: Changing the difficulty after a game started didn't reset the secret number, potentially leaving it outside the newly displayed range.

---

## 2. How did you use AI as a teammate?

- I used the Antigravity Agent and Copilot to refactor code and identify logical inconsistencies.
- **Correct Suggestion**: The Agent correctly identified that `st.session_state.attempts` was being incremented before input validation, leading to unfair attempt penalties. I verified this by entering "abc" as a guess and seeing the attempt count stay the same after the fix.
- **Incorrect Suggestion**: Initially, the Agent suggested moving the functions to `logic_utils.py` without implementing them (leaving `NotImplementedError`). I had to explicitly prompt it to replace the errors with actual logic. I verified this by running `pytest` and seeing the initial failures.

---

## 3. Debugging and testing your fixes

- I decided a bug was fixed by combining automated `pytest` cases with manual verification of the Streamlit UI.
- One key test I ran was the `test_difficulty_ranges` case, which confirmed that "Hard" difficulty now provides a significantly larger range (1-500) than "Normal" (1-100), ensuring the difficulty levels make sense.
- AI helped me by suggesting edge cases for `parse_guess`, such as handling `None` or decimal inputs like "10.5", which I then incorporated into my tests.

---

## 4. What did you learn about Streamlit and state?

- The secret number kept changing in the original app because Streamlit reruns the entire script upon every user interaction (like clicking a button). Without using `st.session_state`, the `random.randint` call would be executed again, generating a new secret.
- I would explain Streamlit "reruns" to a friend as a game that clears the board and restarts every time you make a move, unless you use a "notebook" (session state) to write down what happened in the previous turns.
- The change that finally gave the game a stable secret number was wrapping the secret number assignment in an `if "secret" not in st.session_state:` block, and also ensuring it resets explicitly only when a new game starts or difficulty changes.

---

## 5. Looking ahead: your developer habits

- A strategy I want to reuse is refactoring core logic into separate files early. This made it much easier to write automated tests for individual components without worrying about the Streamlit UI overhead.
- Next time, I would be more proactive in defining the structure of the refactor before letting the AI generate code. This helps avoid "skeleton" code that needs a second pass to actually work.
- This project showed me that AI-generated code is a great draft, but it often lacks defensive programming (like input validation) and logical consistency across state changes. A human "investigator" is essential to ensure the code is actually robust.
