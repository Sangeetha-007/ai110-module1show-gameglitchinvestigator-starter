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

- [ ] Describe the game's purpose. The game's purpose is to guess a number. There are 3 different levels and each level gives you different attempts at guessing the number. 
- [ ] Detail which bugs you found. One bug I found was how it would say "go higher" or "go lower" incorrectly. Another bug was how there were more attempts for the "Normal" level compared to "Hard" level. 
- [ ] Explain what fixes you applied. The fixes I applied are to fix the "go higher" and "go lower" statements correctly. Another bug I fixed is, to make the attempts decrease when the levels go up. Also, when I applied the pytest, there was an issue of strings being used, where it had to be tuples instead. 

## 📸 Demo

- [ ] <img src="/Users/sangeetha/Desktop/game.png"

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
