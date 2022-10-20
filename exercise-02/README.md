# Exercise 2: Getting Started With Git And Python

Deadline: 27.10.2022 11:59

## Step 1
Clone this repository to your local computer. On the command line, you would use the following command: `git clone https://github.com/IDH-Cologne-Deep-Learning-Uebung/uebung-deep-learning-ws2223/tree/master/exercise-02`.

## Step 2
Create a new branch in the repository, named after your UzK-account: `git checkout -b "UZKACCOUNT"`

## Step 3
Open the file calc.py, and run it. The output you should be getting is something like this:
```
Enter number 1: 
5
Enter number 2: 
7
Sum: 12
Product: 35
```

## Step 4
Extend this simple calculator by adding the following new features:

- In addition to being asked for two numbers, the user is now also asked for a math operation they want to do (either addition or multiplication). The program should then either add or multiply the numbers and then print the result.
- The program also accepts the names of the math operations (add/addition and multi/multiplication).
- Instead of exiting the program after calculation, the program asks the user whether they want to continue. If the user enters some form of confirmation, the program starts over. If not, it exits.

## Step 5
Commit your results to your local repository and push it to the server. On the command line, you'd use:
- `git add calc.py`
- `git commit -m "COMMENT"`
- `git push`
