<a href="https://github.com/Pfern/BPBR16-Bioinformatics-using-Python-for-Biomedical-Researchers#this-repository-is-for-the-course-materials-and-it-is-organized-as-follows"> Back to Timetable</a>



# What is Unix/Linux?




### What operating system(s) do you know?





## What is the computer shell?
The shell is an interpreter (a program) that lets you interact with the operating system

![shell](../../img/f1_shell.png)

## The Linux shell
-  The shell is a command-line interpreter that lets you interact with Linux
-   The shell takes what you type and "decides" what to do with it
-   The shell is actually a scripting language somewhat like Python
-   It is always possible to change shell (either temporarily or permanently)

![shell](../../img/shelll.png)


## What is the graphical interface?

![graphinter](../../img/f2_graphinter.png)

## What is the command line interface (or Terminal)?
![shell](../../img/f3_shell.png)


## What happens when you double click on the icon of an application?
![word](../../img/word.png)


## Open a command-line terminal on your computer
You can type a program name at the terminal prompt and then type
[Return]

![term](../../img/f4_command.png)

## The Terminal can be customised

-   Change default bg color
-  Change text size, colour and font
-   Increase/decrease transparency
-   Resize it
-   Have multiple windows open side by side
-   Have multiple "tabs" open at the same time
-   Change the command prompt (most commonly a $  or % sign)
-   Make the cursor blinking

## The command-line interface (terminal)
allows you:

-  to send typed instructions to the computer (i.e., run programs, move/view files, etc.)
-  to see the output that results from  those instructions.

> Every time you type any Unix command and press **enter**,
the computer will attempt to follow your instructions and
then, when finished, return you to the **command prompt**.





## What is the filesystem tree?
Type the Unix command `ls` at the command prompt: what happens?


### The directory structure
The file-system is arranged in a hierarchical structure, like an inverted tree
![t17](../../img/t17.png)

> The top of the hierarchy is traditionally called **root**<br>

> When you first login, the current working directory is your home directory (containing files and directories that only you can modify)




## How can you navigate the filesystem?
> **Challenge #1**
---
>
>What do you need to navigate the filesystem?<br>
>Make a list of the actions needed to navigate <br>
(example: change directory)
>
---


See the <a href="https://github.com/Pfern/BPBR16-Bioinformatics-using-Python-for-Biomedical-Researchers/blob/master/day1/1-Unix/Unix-Theory-BPBR16.solutions.md#solution-to-challenge-1">Solution to challenge #1</a>


## What is the **path** of a file or a directory?

Slashes separate parts of the directory path:
`/home/allegra/Documents/Training/materials/Unix/Academis_Linux.pdf`



> **Challenge #2**
---
>
>What do you need to be able to do/manage stuff in the filesystem?
> (example: Make a new directory)
> Write  a list of actions
>*Tip Think of what you need in, e.g., Windows or Mac OSX*
>
---



See the <a href="https://github.com/Pfern/BPBR16-Bioinformatics-using-Python-for-Biomedical-Researchers/blob/master/day1/1-Unix/Unix-Theory-BPBR16.solutions.md#solution-to-challenge-2">Solution to challenge #2</a>

##  Linux commands
Before talking about Linux commands, we need to answer a question:

---

>What is a computer program?
>
>Which ones do you know?
>
>
>- A text file
>- Word
>- OS
>- The shell
>- An Excel data file
>- A database
>- Power point
>- The Linux Terminal
>- A Linux command
>- About Unix commands
>- Commands are themselves programs
>
---

 An example of command:
`%rm myfile.txt [Return]`

- The shell searches the file containing the program `rm`
- executes the program `rm` on `myfile.txt`
- After the process `rm myfile.txt` has finished running, the shell returns the prompt `%` to you, indicating that it is waiting for further commands.

![example](../../img/examplecommand_cccp.png)


```
command_name -options <file> [Return]

%ls [Return]
%ls –l [Return]
%ls -l <dirname> [Return]
%ls -ltr <dirname> [Return]

man <command name> [Return]
whatis <command name> [Return]
```

---
>OPTIONS and ARGUMENTS
>Replace the XXX
>
>
>- There are commands that can take XXX
>- Commands may also take XXX
>- XXX change the behaviour of the command
>- XXX are the objects on which commands act
>- You will specify XXX using a XXX
>- The command name, XXX and XXX must be separated by
XXX
>
>- If you've made a typo: Ctrl-XXX to cancel the whole line
>- Unix is XXX-sensitive
>- Ctrl-XXX sets the cursor at the beginning of the line
>- Ctrl-XXX sets the cursor at the end of the line
>- You can use up and down XXX to recall commands
>- You can use the XXX to complete a command or file name
>- The command XXX tells you where is a given program
>- You can use a XXX to write programs
>
---


## Did you know that... everything in Unix is either a file or a process?

- A **process** is an executing program identified by a unique PID
(PID = Process IDentifier)

- A **file** is a collection of data


## Writing and running programs in Linux

###  Where can we write programs?
### What is a text editor?
### Which ones do you know?
-   Access your home directory using the command-line interface
-   Start the nano text editor

![nano](../../img/nano.png)


- Create a text file `my_first_shell_script.sh`

![firstshell](../../img/first.png)

- Write the commands in a file, save and exit

-  Go to the command-line interface and type `ls` at the prompt


## How can we run programs on Linux?

### Prerequisites to run a program

####  1. The program must be somewhere on your computer
####  2. The program must be **executable**

*Is my script executable?*
Each file (and directory) has associated access rights, which may
be found by typing `ls -l`
![permission](../../img/t34.png)

> Access rights on directories
>- r allows users to list files in the directory
>- w allows users to delete files from the directory or move files into it
>- x allow users to access files in the directory


*How can I make my script executable?*

Changing access rights: chmod

```
%chmod go-rwx myfile.txt
%chmod a+x my_script
```
| **Symbol**  |**Meaning** |
|----|-----|
| u|user     |
| g|group |
| o|other     |
| a|all|
| r|read     |
| w|write (and delete) |
| x| execute (and access direcotry)|
| +| add permission|
| -| take away permission |

### 3. You have to tell the shell which "interpreter" will read and execute the program AND where it will find it You have to tell the shell which "interpreter" will read and execute the program AND where it will find it

![first](../../img/first.png)

#### **&#!/bin/bash** <br/>
> "Aha, you want to use the program located at /bin/bash to interpret all the instructions that follow"
(Bradnam&Korf - Unix and Perl to the Rescue)


####  4.  You must be in the same directory as the program you
want to run OR….
#### 5.  ….you can prefix its name with a path OR…
####  6.  …the path to your program must in the `PATH` **environment variable**
In other words, if you want to execute the script you have to tell Linux where it can find it


**Where Linux searches for programs?**<br>
Either you explicitly tell Linux where it can find your script…
-    by prefixing its name with a path:
`~allegra/Documents/shell_commands.sh`
-  If you are in the same directory as the one of the program, you can type:
`./shell_commands.sh`


Or you can specify the script's path in the `PATH` environment variable
-  If you simply type (at the prompt):
`shell_commands.sh`

Linux will look up a list of predefined directories to see if that program exists in any of those locations


If it finds a match, it will try to run the program and stop searching in any other directory


If it cannot find a match, it will print "command not found"


*You may think of the PATH variable as a sort of address book UNIX environment variables*


Linux keeps track of several special variables that are
associated with your account
-   Written in upper-case letters
-  Use echo and prefix the variable with a $ if you want
to get the content


Try the following commands:
-   printenv
-   echo $SHELL
-   printenv SHELL
-   echo $PATH
-   echo PATH
-   echo $USER


If the system returns a message saying
`"command: Command not found"`
this indicates that **either the command doesn't exist at all on the system or it is simply not in your path.**


-   Any program in `~/allegra/my_scripts` can be run from anywhere in the filesystem (as long as the program file is executable)
-   You can use tab-completion
-   Your scripts will be treated like any Linux command




For shells in the bash family:
`export PATH=$PATH:~/allegra/my_scripts`

For shells in the csh family:
`setenv PATH $PATH\:~/allegra/my_scripts`


### A few more questions…

- What is command-line completion?
- What is a default argument?

---
> **Challenge #3**
>Use a text editor to write commands into a file, save, exit, make it executable and run it
---


See the <a href="https://github.com/Pfern/BPBR16-Bioinformatics-using-Python-for-Biomedical-Researchers/blob/master/day1/1-Unix/Unix-Theory-BPBR16.solutions.md#solution-to-challenge-3">Solution to challenge #1</a>


##  Connecting to a remote computer
```
ssh remote_host
```


The remote_host is the IP address or domain name that
you are trying to connect to.


If your username is different on the remote system:

```
ssh remote_username@remote_host
```


Once you have connected to the server, you will probably be asked to verify your identity by providing a password.

```
ssh -x remote_username@remote_host
```


## Transferring files to/from a remote computer

```
sftp username@host
```

Enter your password when prompted<br>
Several Unix commands do work<br>
`get`:  Copy a file from the remote computer to the local computer.
`put`: Copy a file from the local computer to the remote computer.


`scp`:  copies files over a secure, encrypted network connection.

```
scp /home/image*.jpg allegra@myhost.com:/home/images
scp allegra@myhost.com:/home/image*.jpg /home/allegra/downloads

scp [-12346BCpqrv] [-c cipher] [-F ssh_config] [-i identity_file]
[-l limit] [-o ssh_option] [-P port] [-S program]
[[user@]host1:]file1 ... [[user@]host2:]file2
```

Enter your password when prompted

## Non-interactive download of files from the Web

```
wget [option]... [URL]...
```

- Non-interactive means that it can work in the background, while the user is not logged on.
-   This allows you to start a retrieval and disconnect from the system, letting Wget finish the work.
-   By contrast, most of the Web browsers require constant user's presence, which can be a great hindrance when transferring a lot of data.


## Listing files and directories

![tab47](../../img/t47.png )

### The directories ‘.’, ‘..’, and ‘~’

```
$ ls -a [Enter]
$ cd . [Enter]
$ cd .. [Enter]
$ ls ~/oeiras

```

## Handling files and directories
![tab48](../../img/t48.png)

```more``` ,  ```less```,  ```clear```

## Redirection
![tab49](../../img/t49.png)
