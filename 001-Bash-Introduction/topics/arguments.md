# Arguments

So far our scripts have had pre-defined variables or expects user input.

We can also pass in `arguments` before a script is run. 

This is very useful for automation, as we can pass outputs from one script as an input to another!

Passing in arguments looks like this:

```
./script.sh your_argument1 your_argument2 your_argument3
```

We can then use `$1` in order to reference the first argument, if there was a second argument use `$2` and so on.

An example script would look like this:

```
#!/bin/bash
echo "My name is $1"
```

When running the example you can pass in an argument:

```
./script.sh Dale
```

The output would be:

```
My name is Dale
```

To reference all arguments, you can use $@:

```
#!/bin/bash
echo "All arguments: $@"
```

If you run the script again:

```
./arguments.sh dog cat bird
```

You will get the following output:

```
All arguments: dog cat bird
```

## Task 4:
Create a script that takes 2 or more arguments and use `echo` commands to output values.

Finally, we'll look at arrays.