# Structure
Bash shell script files use the `.sh` extension. 

Create a new file:

```
touch hello-world.sh
```

Edit file in VS Code.

In order to execute/run a bash script file, the first line must indicate the absolute path to the bash executable:

```
#!/bin/bash
```

This is called a shebang.

All that the shebang does is to instruct the operating system to run the script with the /bin/bash executable.

If you try to run the script you'll get:

```
zsh: permission denied: ./hello-world.sh
```

The script needs “execute” permission to run:

```
chmod +x script.sh
```

chmod is the command and system call used to change the access permissions of file system objects, sometimes known as modes.

chmod stands for `Change Mode`

Next we'll add an Hello World! echo output.