# Arrays

Unlike variables, arrays can hold several values under one name.

For example if you wanted a list using variables you would have to declare the following:

```
variable1="dog"
variable2="cat"
variable3="bird"
.... and so on
```

The downside is the list of variables could grow, and you would need to know the right variable name to reference.

An array is just one variable name, but stores multiple values. 

You can initialise an array by assigning values divided by space and enclosed in `()`. Example:

```bash
my_array=("dog" "cat" "bird")
```

To access the elements in the array, you need to reference them by their numeric index.

>{notice} keep in mind that you need to use curly brackets.

* Access a single element, this would output: `dog`

```bash
echo ${my_array[1]}
```

* The following would both return the last element: `bird`

```bash
echo ${my_array[3]}
echo ${my_array[-1]}
```

* As with command line arguments using `@` will return all arguments in the array, as follows: `dog cat bird`

```bash
echo ${my_array[@]}
```

* Prepending the array with a hash sign (`#`) would output the total number of elements in the array, in our case it is `3`:

```bash
echo ${#my_array[@]}
```

## Task 5
Create a script that takes multiple `arguments` and stores them in an `array`. Then use echo to output each array value.

### Notes

I noticed when running the code in iTerm the index starts at 1, but when running the Bash script the index is 0.

Found this article:
https://stackoverflow.com/questions/50427449/behavior-of-arrays-in-bash-scripting-and-zsh-shell-start-index-0-or-1

bash array indexing starts at 0 (always)
zsh array indexing starts at 1 (unless option KSH_ARRAYS is set)
To always get consistent behaviour, use:
```
${array[@]:offset:length}
```