---
title: "4: Animal quiz"
reveal: true
weight: 10
---
![Animal Quiz](title.jpg)

Are you a fan of quizzes? Would you like to make one yourself? In this project, you’ll build an animal quiz. Even though the questions are about animals, this project can be easily modified to be about any other topic.

In this example, you'll see bits of code with annotations. The code in black is new code to be added. The code in grey is existing code; use this to work out where to add the new lines of code. The instructions will ask you to run the code at various points. Make sure you do this and that the code successfully runs. **Do not proceed to the next step until the previous one works. You'll just make things harder for yourself!**

## What happens 
The program asks the player some questions about animals. They get three chances to answer each question—you don’t want to make the quiz too difficult! Each correct answer will score points. At the end of the quiz, the program reveals the player’s final score.

## How it works 
This project makes use of a function—a block of code with a name that performs a specific task. A function lets you use the same code repeatedly, without having to type it all in every time. Python has lots of built-in functions, but it also lets you create functions of your own.

<!-- {{< revealx makingAQuiz >}} -->

## 1. Design the main algorithm
We know that we are going to build a quiz with lots of questions, but let's start small, and worry about just one question, as it seems likely
that the other questions we ask will have a lot of code in common. Let's start with a basic algorithm.

<video controls>
    <source src="basicAlgorithm480.mp4" type="video/mp4">
    Your browser does not support the video tag. Watch video <a href="basicAlgorithm480.mp4">here</a>.
</video>

We want to ask the user a question, get their guess, and check it against the right answer. If they are correct, we praise them (and we'll give them a point later). If they get it wrong, we'll let them try again.

We can test out our algorithm by starting at the Start and running our finger along the arrows to check that the behaviour is correct.

## 2. Some code
Now let's turn that into some code.

<video controls>
    <source src="basicCode.mp4" type="video/mp4">
    Your browser does not support the video tag. Watch video <a href="basicCode.mp4">here</a>.
</video>

We use `print()` to talk to the user, and `input()` to get responses back. So far our code doesn't loop when the user guesses incorrectly.
Let's add that now.

## 3. Code with retries
We can work out where to loop by working out the first and last bits of code that correspond with the parts of
the algorithm in the loop, and indent them. We can then write `while True:` at the start of the loop. We then need to work out which decision
should end the loop, and put a `break` there.

<video controls>
    <source src="codeWithLoop.mp4" type="video/mp4">
    Your browser does not support the video tag. Watch video <a href="codeWithLoop.mp4">here</a>.
</video>

We can slightly simplify our code here. Because we break out of the loop if the guess is correct,
we don't need to put the case when the user is wrong inside an `else` block.

<video controls>
    <source src="codeSimplifiedGuessElse.mp4" type="video/mp4">
    Your browser does not support the video tag. Watch video <a href="codeSimplifiedGuessElse.mp4">here</a>.
</video>

This works because if you get as far as the new line 7 we know that you guessed wrong (otherwise we'd have
broken out of the loop already). So we don't need to check or clarify that.

## 5. Multiple questions
Let's add a couple more questions. We can copy/paste the code we need to make more questions. So what do we need to copy?

If you worked out it's all of it, you're right! We are going to extract this repeated part and make it into a function,
so we can write the code once and reuse it multiple times.

<video controls>
    <source src="codeWithFunction.mp4" type="video/mp4">
    Your browser does not support the video tag. Watch video <a href="codeWithFunction.mp4">here</a>.
</video>

By defining a function to do this work, we can add features or make changes to the function and see those reflected in every question—making those changes for every question by hand would be much more effort, and errors would be much more likely to creep in.

## 6. Keeping score

To keep track of the score, we will need a variable. For the moment we'll give one point for a correct answer.

Since the score will exist across all questions, we need to declare the variable in the main body of the code, and tell the `ask()` function to use that variable, rather than make up its own when refer to it.

<video controls>
    <source src="codeAddScore.mp4" type="video/mp4">
    Your browser does not support the video tag. Watch video <a href="codeAddScore.mp4">here</a>.
</video>

Here we add a point to the score when we get a question right and print out the current score. Notice the use of [f-strings](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python) here to print out a variable within other text.

## Challenges

1. Give more points for a correct answer
2. Take away a point for each wrong answer
3. Limit the number of guesses for each question
    <br/>*Help: you will need a variable to store the number of guesses remaining. You will need to add another* `if` *statement to check the guesses remaining, as it is another way to leave the questions loop (i.e. you might get the answer right, or you might run out of guesses).*