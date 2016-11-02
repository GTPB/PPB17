<a href="https://github.com/ELIXIR-ITA-training/python_course"> Back to Timetable</a>

## The Python structure - Vocabulary, tips and comments

- Python code can be written in two different "containers":
  - Interactive interpreter (not permanent)
  - Modules or programs (permanent)
 
- The content of a module can be used in a script (or in a different module) by importing the module

- Scripts, programs, modules can be  written in text files.
<img src="../../img/pm1.png" alt="slot" style="width: 100px;"/>
<img src="../../img/pm2.png" alt="slot" style="width: 100px;"/>

- Inside modules you can define other containers: classes and functions.

- More in general, modules are containers for data, functions and classes. 

- In other words, we will call **modules** text files containing definitions of data (through variable's assignment), functions and classes.

- We will call **programs** or **scripts** text files containing definitions AND actions. 

- You will **run programs** and **import modules**.

- When you ```import``` a module, Python reads and executes each line contained therein.

- It is good practice to write small re-usable pieces of code in separate modules and connect them through the ```import``` statement and the **dot syntaxt**.

- The objects contained in modules (and, if you want to, in classes and functions) are: data structures; variable definitions; operators; control flow statements.

## The “dot” syntax
<img src="../../img/pm5.png" alt="slot" style="width: 100px;"/>
<img src="../../img/pm6.png" alt="slot" style="width: 100px;"/>
<img src="../../img/pm7.png" alt="slot" style="width: 100px;"/>

# The matryoshka doll-like structure of Python

<img src="../../img/pm8.png" alt="slot" style="width: 100px;"/>


#### module.class.method()
#### module.method()
#### class.method()
#### module.variable
#### module.class.variable



## Challenge
> -   Open a text file using gedit
> -   Write:`print "My name is:", "myname"`

<img src="../../img/pm3.png" alt="slot" style="width: 100px;"/>

> -   Save the file in your home directory with the name: `my_name.py`
> -   Go to your home directory using the command-line interface
> -   Type at the prompt: `python my_name.py`
> -   Open a DIFFERENT text file using gedit
> -   Write: `import my_name`

<img src="../../img/pm4.png" alt="slot" style="width: 100px;"/>

> -   Save the file in your home directory with the name: `my_first_run.py`
> -    Go to your home directory using the command-line interface
> -    Type: `python my_first_run.py`

