# User Input

Previously, variables can be defined in a script however we can ask the user for input instead.

Use `read` to request an input.

```
#!/bin/bash
echo "What is your name?"
read name
echo "Hi there $name"
```

The above will prompt the user for input and then store that input as a string/text in a variable.

We can then use the variable and print a message back to them.

## Task 3
Create a Bash script to `read` an input and use `echo` to output it.

You can also reduce the code by using the `-p` flag.

```
#!/bin/bash
read -p "What is your name?" name
echo "Hi there $name"
```

Before we move onto another way of passing in values, let's look at commenting code.