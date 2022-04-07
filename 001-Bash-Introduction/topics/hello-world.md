# Hello World

Once we have our hello-world.sh file created and we've specified the bash shebang on the very first line, we are ready to create our first Hello World bash script.

Open the hello-world.sh file and add the following after the `#!/bin/bash` line:

```
echo "Hello World!"
```

Save and execute the script:

```
./hello-world.sh
```

You will see a "Hello World!" message on the screen.

Another way to run the script would be:

```
bash hello-world.sh
```

As bash can be used interactively, you could run the following command directly in your terminal and you would get the same result:

```
echo "Hello World!"
```

Putting a script together is useful once you have to combine multiple commands together.

Next we'll add some variables.