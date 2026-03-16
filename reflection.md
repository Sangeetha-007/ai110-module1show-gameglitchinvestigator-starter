# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

In the game, I never guessed the number correctly. For a range of 1 to 100. I would guess 99, and it would say I need to go higher, only for the right number to be a lower number. That is one error I noticed. Another error I found is how the "hard" level is from 1 to 50, meanwhile the "normal" level is 1 to 100. It should be easier to guess a number correctly when there is a smaller range. 3rd error I found is how the "New Game" button doesn't work.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude for this project. It also agreed with me how the get_difficulty_range function is incorrect by giving the "hard" level a smaller range than "normal". I fixed the code manually myself and asked Claude to inspect it to see if it agrees with what I wrote. A misleading suggestion Claude gave me was how it said: 
"  1. Wrong hint direction (lines 37–40): The messages are flipped. If guess > secret, the player guessed too high, so the hint should say "Go Lower" — but it says "Go
  HIGHER". Same bug in reverse for the else branch.
  2. TypeError fallback uses string comparison (lines 42–46): When a TypeError occurs, it converts guess to a string and compares using >. String comparison is
  lexicographic (e.g., "9" > "10" is True), so this will give wrong results for numbers.
  3. Same flipped hint bug in the except block (line 45): The same wrong-direction hint persists in the fallback path. "
I disagree with this suggestion, but I will keep it in mind and come back to it. I think Claude is wrong but I will check it later. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided if a bug was really fixed by checking the logic myself first. Then making Claude AI confirm. One pytest I ran was to check the function test_winning_guess in test_game_logic.py. The error the pytest showed was a string/tuple error, therefore all 5 tests failed. AI did help me understand the test, and it helped make the change. I verified it before accepting its suggestions. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---
If I had to explain Streamlist "reruns" to a friend who has never used Streamlit, this is what I would say. Streamlit is a platform to host a web application. Web applications can have bugs/mistakes which we as the developer would need to fix with the help of AI. We would need to fix the code, then rerun it to test to see if we like and agree with what we see. Session state allows web applications to remember user data, for example inputs I used to play this game. 

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse in all of my future projects, is how I wrote the code myself before asking Claude AI to check; instead of blankly asking it to generate the code. One thing I would do differently next time I would with AI on a coding task is prompt with more detail. After this project, I am glad, humans have to be involved with testing code, and making sure it works the way we want, rather than completely relying on the AI to do it all. I hope humans continue to test and validate, so we can make safe softwares, and not vibe code everything. 
