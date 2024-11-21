# ❗CSC226 Final Project

## Instructions

Relly Gray

https://docs.google.com/document/d/1DiAe0NfPnl17viu_tUDePR5RxEHGm1ECc_ooHmqzmSM/edit?usp=sharing

---

## References 
Throughout this project, you have likely used outside resources. Reference all ideas which are not your own, 
and describe how you integrated the ideas or code into your program. This includes online sources, people who have 
helped you, AI tools you've used, and any other resources that are not solely your own contribution. Update as you go.

---

## Milestone 1: Setup, Planning, Design

Mood-Based Music Recommender 

Create an app that suggests songs based on the user’s mood or activity.

Fetches playlists or tracks using APIs like Spotify or YouTube.
  
(https://docs.google.com/document/d/1nrINAUR9xkZ100Ogs3r2qlp0K-9iJ2MBfkwViqSO9nM/edit?usp=sharing 
'''Image of CRC card as an example. Upload your CRC card(s) in place of this one.'''

❗️**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments: 

```
    Branch 1 name: grayr2
    Branch 2 name: _____________
```
---

## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
    It’s going okay so far, but I realize I’m behind and need to catch up quickly. 
    I’m worried about completing everything on time, especially with so much still left to do. 
    What surprised me most was realizing how far behind I actually am, but I’m determined to 
    focus and finish strong.
```

---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 
`5%`


Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

```
    I’m not very confident about completing this project because I feel behind and unsure if I 
    can manage my time effectively. To increase my chances of success, I will break the project 
    into smaller, manageable tasks and set daily goals to track progress. Additionally, I’ll 
    focus on finishing the core features first, ask for help when needed, and set aside 
    dedicated time for uninterrupted work each day
```

---

## Milestone 4: Final Code, Presentation, Demo


In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button 
in PyCharm. 
```
After hitting the "Run" button in PyCharm, the program will start by asking you to enter your 
name to personalize the experience. Next, you’ll be prompted to input your current mood 
(e.g., “happy,” “sad,” “energetic,” etc.), and the program will analyze your input to match 
it with a music genre. Based on the genre, the program will recommend a list of songs or 
playlists that fit your mood. You can save these playlists for later or explore another mood 
by simply entering a new one when prompted. Follow the on-screen instructions, and you’ll be 
guided through the process step by step, ensuring an easy and enjoyable user experience.
```

Every program has bugs or features that had to be scrapped for time. These bugs should be tracked in the issue queue. 
You should already have a few items in here from the prior weeks. Create a new issue for any undocumented errors and 
deficiencies that remain in your code. Bugs found that aren't acknowledged in the queue will be penalized.
```
Deficiency: Limited Song Recommendations
Description: Currently, the program only recommends songs from a small local database and does not use external APIs, limiting variety.
Priority: Low
Reason for potential Scrapping: Time constraints on integrating an API like Spotify or YouTube.
Proposed Fix: In the future, add an APIHandler class to fetch songs from online services.
Status: Unresoved (yet?)

Bug: Empty Mood Input Causes Crash
Description: If the user presses Enter without typing a mood, the program throws an error instead of prompting the user again.
Priority: High
Proposed Fix: Add input validation to ensure the user cannot submit an empty response.
Status: Unresolved

Bug: Genre Mapping Missing for Uncommon Moods
Description: When a user inputs a mood that is not mapped (e.g., "confused" or "excited"), the program defaults to "unknown," but this behavior is not user-friendly.
Priority: Medium
Proposed Fix: Add more mood mappings to MoodAnalyzer or include a fallback to suggest a random genre if the mood isn’t recognized.
Status: Unresolved

Deficiency: No GUI
Description: The program runs in the console, which may be less user-friendly for some users. A graphical interface was planned but not implemented.
Priority: Low
Reason for Scrapping: Lack of time and focus on core functionality.
Proposed Fix: Use a library like Tkinter or PyQt to build a simple interface for mood input and song recommendations.
Status: Deferred
```

### ❗Reflection
In three to four well-written paragraphs, address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- (For partners) How well did you work with your partner? What made it go well? What made it challenging?
```
I selected this project because I love music and enjoy curating playlists based on moods. 
Music is such a personal and emotional experience, and being able to create a program that 
ties emotions to music felt like a meaningful and creative way to explore coding. I wanted 
the project to reflect something I’m passionate about, which kept me motivated throughout 
the process, even when it became challenging.

The final project was a bit wonky compared to my initial design. While the core 
functionality of analyzing moods and recommending songs worked, some planned features, 
like integrating an API for more song variety and adding a graphical user interface, likely 
will be scrapped due to time constraints. Additionally, there were a few bugs, like 
handling unrecognized moods or empty inputs, that made the program less polished than I had 
hoped. Despite these setbacks, the project still captured the essence of what I wanted to 
achieve.

Through this process, I learned a lot about planning, time management, and the importance of 
breaking tasks into smaller, achievable steps. I also gained a better understanding of 
debugging and validating user input to make programs more user-friendly. Most importantly, I 
realized the value of focusing on the core functionality first instead of trying to do too 
much at once, which can lead to feeling overwhelmed.

The hardest part of the project was balancing design and implementation. I spent a lot of 
time thinking about how the classes would interact and what features to include, but I 
underestimated how long it would take to write and debug the actual code. Next time, I would 
focus on building a simple, working prototype first and then add additional features 
gradually. This would allow me to spend more time polishing the program and less time 
scrambling to finish the core components. Working alone was challenging because I didn’t have 
anyone to brainstorm with or share the workload, but it also allowed me to fully immerse 
myself in the project and take ownership of every aspect.
```