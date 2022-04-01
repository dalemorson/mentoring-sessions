# Bash Introduction
Introduction/refresher for mentoring session 31st March 2022.

**Note: Use VS Code live sharing!**

## Introduction:
- Bash is a Unix shell and command language.
  - Can get Bash for Windows.
- Default command interpreter on most Linux and MacOS systems.
- Just need a UNIX terminal and a text editor like Sublime Text, VS Code, or a terminal-based editor like vim or nano.
- Many other languages available across platforms (PowerShell, Python for example). Principles apply to most, just different syntax.

## Benefits:
- Easier and quicker than navigating menus, options and windows within a GUI.
  - No need to use a mouse.
- Less resource-intensive (i.e. no graphical rendering of GUI)
- Automate repetitive tasks.
  - Do the same thing every time, no human error!
  - Reuse someone elses code.
  - Any command you can run in your terminal can be run in a Bash script.
- Inputs that can be used, processed, manipulated. Outputs can be generated.
- Use version control like GitHub.

## What is a Bash script?
- Reusuable sets of bash terminal commands can be created using bash scripts.
- Bash scripts can run any command that can be run in a terminal.
  
## Quick Demo
How long does it take to create 50 folders using the GUI compared to Bash!?
  - create 50 folders using the GUI
  - create 50 folders using Bash

```
mkdir folder{1..50}
```

## Introduction
  - [structure](topics/structure.md)
  - [hello world](topics/hello-world.md)
  - [variables](topics/variables.md)
  - [user input](topics/user-input.md)
  - [comments](topics/comments.md)
  - [arguments](topics/arguments.md)
  - [arrays](topics/arrays.md)