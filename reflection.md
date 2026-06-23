# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| -56 |  Go higher         | told to go lower| None                   |
| -56 | should not be allowed| told to go lower|   None
                              
|  New game|  New game started| Still the game over screen| None|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
With the bug of the new game never starting, claude ai directed me on what I would need to add to fix said bug It broke down why it believed it wasnt workign then gave me a one line fix. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

For the new game not starting, I amnually tested wherether it was was working or not by refreshing mutiple times and clicking the button over and over. 

Then for the how high or how low I asked calude to create a pytest to try and then vefired how it should work with given corrrect number.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---
Streamlit reruns the whole script everytime someone intreacts with the app. Session state is used to save information bvetween these reruns so these values are not reset each time the page refreshes.

To explain to a friend I would say streamlit is constaly rebuilding the page whenever something chnages and session states acts like a memory stroage box that remebers info and rebuilds the page based off of it. Without session state everything like scores would be lost whenever the app refreshes. 

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I want to use checking and really pushing the Ai to challenge me.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
Make sure to ask it everytime I use it if it can full explain what it is doing so I can understand what is happening
- In one or two sentences, describe how this project changed the way you think about AI generated code.
That Ai generated code can be helpful and isnt just hosilatingnating all the time. That it can make meaningful change to a project.
