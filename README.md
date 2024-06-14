[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ugsDDcR1)
# CP1404 Assignment 2: Travel Tracker 2.0 by Kantapong Wongsanguan

_Edit this README, replacing this line and above with your own name/details._  
_At the end of the project, complete the project reflection below by answering the questions (replace the ... parts)._
_Note that to get high marks for this, your reflection should match the "exemplary" description from the rubric:_

> The project reflection is complete and describes development and learning well, shows careful thought, highlights insights made during code development.


## 1. How long did the entire project (assignment 2) take you?
I completed this assignment on multiple days since June 1st. Though I did not record the exact time it took and time for reviewing the app, the estimation would be around 15-20 hours. ( 3d, 4h each, (3rd ~6h))
Note: You may like to use the WakaTime plugin, which tracks exactly how long you spend in code. See http://wakatime.com (but note that the free version only has a 7-day history)

## 2. What are you most satisfied with?
The most satisfaction being when the codes and the app finally worked accordingly despite the lengthy hours it took.

## 3. What are you least satisfied with?
There were some codes where it should be pretty forward and I should have been able to code it without looking back to the lecture notes and the example, however it is what it is, there were little parts of the code where I could not get it right without addition lecture notes. 

## 4. What worked well in your development process?
I would say the early foundation of what was taught in earlier weeks were really fundamentally needed. The hours it took to increase the understanding of those structure taught really paid off in developing the app brick by brick.

## 5. What about your process could be improved the next time you do a project like this?
Consistent Time management. During the process, I took sometime off to study other subject modules as well. During the time off, I kept having ideas about how to solve the problems and how to improve the codes which it would definitely be better for me to just sit down and finish the programme in a more consistent period within one or two weeks.
In addition to creating organised schedules instead of do it whenever I felt like, utilizing learning resources more instead of going at the code alone for hours would and seeking clarification from lecturer would be one of the first thing I do in a project like this, since in the end, the purpose is not to just test myself but to complete the task optimally without wasting time more than intended too.

## 6. Describe what learning resources you used and how you used them.
I mostly refer back to the lecture pptx, notes , and further provided subject materials. The structure of the app was similarly taught in the weekly practical sessions while the extended exercises given was really helpful as well.

## 7. Describe the main challenges or obstacles you faced and how you overcame them.
Time management and understanding more complex concepts. The main challenges were as previous mentioned, time management with the addition of more complex concepts. Understanding the structures of the program as intended, I made a mistake where I did not make clear pseudocode. I kinda made the pseudocode in the notes as I went along completing the codes task by tasks and in the end the function methods in the Class did not follow the SRP rules at all. Making clear pseudocode would be beneficial in my case since to overcome these challenges, I implemented strategies along the ways as I progress which I can see now is not at all optimal.
In terms of coding, I overcame those obstacles by simplified and improving my codes structure in organised way. this allowed me to encapsulate data and functions, create reusable code, and achieve code extensibility through inheritance ,which I think enhancing the code readability and facilitated future modifications. 

## 8. Briefly describe your experience using classes and if/how they improved your code.
Reflecting on the classes, there are several areas in my process that I could improve for the future. 
Simplifying and use pseudocode for better code structures would really improve my codes for the next time. In summary, planning, time management, communication (to lecturer), testing, documentation, and reflection each coding session will definitely lead to improved project outcomes for the next one.
Overall, experiences with using classes taught me, mostly in resilience and problem-solving more complex tasks efficiency in a more organised way.

# Work Journal


Work Entries: Each time you work on the assignment, record an entry in your journal that includes: 
• Date and time you worked, including duration 
•What you worked on with simple details, enough that someone reading it would understand 
• Any difficulties you faced and how you overcame them
Entry 1
Date: 22/1/2023 - morning
Duration: 30 minutes
Detail: 
•	Started going through the assignment 2 pdf provided on LearnJCU 
•	Started drafting the pseudocode 
o	Left out the loading of the saved text file as I was really unsure on how the code would look like at the moment
Difficulties: 
•	The written pseudocode done for this part could be done in a lot shorter time if I could think of the appropriate naming off the top of my head. Checking the Pseudocode Guide was really helpful. 
Date: 22/1/2023 - afternoon
Duration: 45 minutes
Detail: 
•	Started the main function. Leaving out the loading option at the beginning of the main function for later.
•	Picking the right loop to use was not as tricky as the first time before the practical class, since I have done menu with function previously. The same also goes for picking the right statement to use for if, elif, else.
•	Stop when the main and greeting function was done after a few times fixing the code
Difficulties: 
•	Was really unsure if the main function would work correctly as intended or not since I didn’t finish all the functions used in the main. However, already tested for greeting function when the program is run.
•	Took a few tries to get the spacing right so the output from the code would look like the one in the given example. Use of print() and \n




Entry 2
Date: 25/1/2023 
Duration: 90 minutes
Detail:
•	Finished coding the rest of the function.
•	Took a few times to correct all the error during the process. Previous practical works were really helpful as the guideline on how the code should look like step by step.
•	Went back and started on reading the plants text file
•	Unsuccessful on getting the file to read the texts and store them as list variable
Difficulties:
•	Using the right command to store texts in file as list variable
Entry 3
Date: 30/1/2023
Duration: 60 minutes
Detail: 
•	Double check everything. Comparing the output with the given example, adjusting the constant for rainfall were quite helpful as I was really unlucky to get the wanted amount of rainfall to test carious scenario.
•	Still unsuccessful on storing the texts in file as list variable
Difficulties:
•	Using the right command to store texts in file as list variable
Entry 4
Date: 31/1/2023
Duration: 120 minutes
Detail
•	Managed to read the plants.txt file and stored text data as a list 
•	Realising unwanted output when the plants has all died.
o	Input for choice is still requested by the code but output as error when input choice “(W)ait”.
•	Fixing Pseudocode after getting all the codes to work correctly.
•	Create a function for each choice input as its own section
o	Create pseudocode for function for simulating a day on its own section.
	Previously the entire section under if choice == ‘w’: was the code for simulating the next day. Now after input choice as ‘w’, the next code run is the function.
Difficulty:
•	Not realising ‘pass’ to do nothing in ‘if’ statement is needed when choice == ‘w’ and no plants are present in the garden.
•	The main difficulty for me which took the longest time to complete this part was the lack of understanding how function returns the variable.
o	Took a while fixing and trying many variations of code to get “food = simulate_day(plants)”.

Summary
 It has been quite a fun and challenging process to this assignment. The problem that always occur to me was due to the lack of understanding how to correctly pass on arguments. Sometimes, I understood what I needed to use but however, calling the right variable or the needs to create new ones where quite confusing. To solve the issues I found in my code, I needed to spent quite a lot of time trying many solutions, combinations, and/or variations of coding to truly understands how it works. I felt like this assignment has the same process of trying and getting it right after failing as the same as the practical sessions I have been having on campus but this took a little bit longer. 
 Now, I have learned that there are always a way for coding and there is always a shorter better code for it . For example, multiple lines of code I have written can be shorten with a few built-in functions available on PyCharm. Good thing is I will be learning those in the future, improving my coding later on. 
 To improve my skill and develop solution faster than what I have done for this assignment, for some parts, for example, reading and editing a different variable type from a text file to python variable, I need to go back studying the notes on how the function work step by step. In addition, practising in my on time would be a lot of help as I will get to know and learn from failing what I could not do.

