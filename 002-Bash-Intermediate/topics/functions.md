# Functions

Functions are a great way to reuse code. 

The structure of a function in bash is quite similar to most languages:

```bash
function function_name() {
    your_commands
}
```

You can also omit the `function` keyword at the beginning, which would also work:

```bash
function_name() {
    your_commands
}
```

Example of a "Hello World!" function:

```bash
#!/bin/bash
# Example 10
function hello(){
    echo "Hello World Function!"
}

hello
```

> One thing to keep in mind is that you should not add the parenthesis when you call the function.

Passing arguments to a function work in the same way as passing arguments to a script:

```bash
#!/bin/bash
# Example 11
function hello(){
    echo "Hello $1!"
}

hello Dale
```

Functions should have comments mentioning description, global variables, arguments, outputs, and returned values, if applicable

```bash
#######################################
# Description: Hello function
# Globals:
#   None
# Arguments:
#   Single input argument
# Outputs:
#   Value of input argument
# Returns:
#   0 if successful, non-zero on error.
#######################################
function hello(){
    echo "Hello $1!"
}
```

### Task 9

Can you create a script with the following requirements:
1. A `function` that takes two `arguments` 
2. Use a `conditional expression` to check if the two arguments are the same.  
3. Use `echo` to output whether the two arguments match or not.
