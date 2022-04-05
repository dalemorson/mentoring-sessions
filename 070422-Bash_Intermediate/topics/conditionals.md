# Conditionals

We can now use conditional expressions with standard conditional statements like `if`, `if-else` and `switch case` statements.

## If statement

The format of an `if` statement in Bash is as follows:

```bash
if [[ some_test ]]
then
    <commands>
fi
```

Here is a quick example which would ask you to enter your name in case that you've left it empty:

```bash
#!/bin/bash
# Example 1
# Bash if statement example

read -p "What is your name? " name

if [[ -z ${name} ]]
then
    echo "Please enter your name!"
fi
```

### Task 6

Write a bash script with the following requirements:
1. Use `read` to store two variables, we want to check if these two variables are the same.
2. Use an `if` statement.
3. Use a `conditional expression` in the `if` statement to check if the two variables are the same.
4. Use an `echo` to return a message when the `conditional expression` is true.

### Task 6 - Questions
1. What did you notice when the strings didn't match? ie the `conditional expression` was false?
2. What do you do to terminate an `if` statement?

## If Else statement

With an `if-else` statement, you can specify an action in case that the condition in the `if` statement does not match. We can combine this with the conditional expressions from the previous section as follows:

```bash
#!/bin/bash
# Example 2
# Bash if statement example

read -p "What is your name? " name

if [[ -z ${name} ]]
then
    echo "Please enter your name!"
else
    echo "Hi there ${name}"
fi
```

### Task 7

Update the previous script with the following requirements:
1. Add an `else` statement
2. Use an `echo` to return a message when the `conditional expression` is false

## Switch case statements

As in other programming languages, you can use a `case` statement to simplify complex conditionals when there are multiple different choices. 

So rather than using a few `if`, and `if-else` statements, you could use a single `case` statement.

The Bash `case` statement syntax looks like this:

```bash
case $some_variable in

  pattern_1)
    commands
    ;;

  pattern_2| pattern_3)
    commands
    ;;

  *)
    default commands
    ;;
esac
```

A quick rundown of the structure:

* All `case` statements start with the `case` keyword.
* On the same line as the `case` keyword, you need to specify a variable or an expression followed by the `in` keyword.
* After that, you have your `case` patterns, where you need to use `)`  to identify the end of the pattern.
* You can specify multiple patterns divided by a pipe: `|`.
* After the pattern, you specify the commands that you would like to be executed in case that the pattern matches the variable or the expression that you've specified.
* All clauses have to be terminated by adding `;;` at the end.
* You can have a default statement by adding a `*` as the pattern.
* To close the `case` statement, use the `esac` (case typed backwards) keyword.

Here is an example of a Bash `case` statement:

```bash
#!/bin/bash
# Example 3
read -p "Enter the name of your car brand: " car

case $car in

  Tesla)
    echo -n "${car}'s car factory is in the USA."
    ;;

  BMW | Mercedes | Audi | Porsche)
    echo -n "${car}'s car factory is in Germany."
    ;;

  Toyota | Mazda | Mitsubishi | Subaru)
    echo -n "${car}'s car factory is in Japan."
    ;;

  *)
    echo -n "${car} is an unknown car brand"
    ;;

esac
```

With this script, we are asking the user to input a name of a car brand like Tesla, BMW, Mercedes and etc.

Then with a `case` statement, we check the brand name and if it matches any of our patterns, and if so, we print out the factory's location.

If the brand name does not match any of our `case` statements, we print out a default message: `an unknown car brand`.

We'll now look at [loops](loops.md)