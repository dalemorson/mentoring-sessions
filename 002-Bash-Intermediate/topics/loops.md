# Loops

Loops are very convenient. With Bash you can use `for`, `while`, and `until` loops.

## For loops

Here is the structure of a `for` loop:

```bash
for var in ${list}
do
    your_commands
done
```

Example:

```bash
#!/bin/bash
# Example 4
users="Dale Karolina"

for user in ${users}
do
    echo "${user}"
done
```

A quick rundown of the example:

* First, we specify a list of users and store the value in a variable called `$users`.
* After that, we start our `for` loop with the `for` keyword
* Then we define a new variable which would represent each item from the list that we give. In our case, we define a variable called `user`, which would represent each user from the `$users` variable.
* Then we specify the `in` keyword followed by our list that we will loop through
* On the next line, we use the `do` keyword, which indicates what we will do for each iteration of the loop
* Then we specify the commands that we want to run
* Finally, we close the loop with the `done` keyword

You can also use `for` to process a series of numbers. For example here is one way to loop through from 1 to 10:

```bash
#!/bin/bash
# Example 5
for num in {1..10}
do
    echo ${num}
done
```

## While loops

The structure of a while loop is quite similar to the `for` loop:

```bash
while [ your_condition ]
do
    your_conditions
done
```

Here is an example of a `while` loop:

```bash
#!/bin/bash
# Example 6
counter=1
while [[ $counter -le 10 ]]
do
    echo $counter
    ((counter++))
done
```

First, we specified a counter variable and set it to `1`, then inside the loop, we added counter by using this statement here: `((counter++))`. 

That way, we make sure that the loop will run 10 times only and would not run forever. 

The loop will complete as soon as the counter becomes 10, as this is what we've set as the condition: `while [[ $counter -le 10 ]]`.

Let's create a script that asks the user for their name and not allow an empty input:

```bash
#!/bin/bash
# Example 7
read -p "What is your name? " name

while [[ -z ${name} ]]
do
    echo "Your name can not be blank. Please enter a valid name!"
    read -p "Enter your name again? " name
done

echo "Hi there ${name}"
```

Now, if you run the above and just press enter without providing input, the loop would run again and ask you for your name again and again until you actually provide some input.

## Until Loops

The difference between `until` and `while` loops is that the `until` loop will run the commands within the loop until the condition becomes true.

Structure:

```bash
until [ your_condition ]
do
    your_commands
done
```

Example:

```bash
#!/bin/bash
# Example 8
count=1
until [ $count -gt 10 ]
do
    echo $count
    ((count++))
done
```

## Summary

This section has a lot of information and is good to be aware of each loop type and why you would use each:

- `for` - will loop for the amount of items there are.
- `while` - do something while it's true.
- `until` - do something until it's true.

### Task 8

Create a loop script with the following requirements:
1. Use `read` to input a list of users and store them into a single variable.
2. Use a `for` loop.
3. Use `echo` to output each of the strings from the variable. 

Finally we'll look at [functions](functions.md)