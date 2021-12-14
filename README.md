# <center>UNIX utilities in Python (This repository is incomplete.)</center>

## Description

This repository is an attempt to make up some famous UNIX-commands in Python
without using subprocess module or external packages.

Here you can find the following utilities:

1) File <font size="4">__wc.py__</font> simulates <font size="4">wc</font> command. It works as original one wc command, it takes an argument as a path to file or take it
   from stdin by default, output sets by default as stdout, you can redirect it by adding __<big>'> filename'</big>__  to the end of the command.
   It can work in pipes and save. Simple example: 
   ```ls ~ | ./wc.py -c``` 
   The following options are available (all three work by default):
   - <font size="4">-l or --lines</font> – lines count
   - <font size="4">-w or --words</font> - words count
   - <font size="4">-c or --bytes</font> - bytes count 
   
2) File <font size="4">__ls.py__</font> works as original one <font size="4"> ls </font> command. It needs a path
to a folder/filer to show its content, by default it sets as '.' – current folder. It can work in pipes,
   and result can be redirected to a file by adding __<big>'> filename'</big> to the end of the command. Simple example ```./ls.py -a ~/Documents```
   It supports only one option:
   - <font size="4">-a</font> - to display all files including the hidden.
   
3) File <font size="4">__rm.py__</font> works as original one <font size="4">rm</font> command. It takes only one argument - path to a folder/file and remove it.
It can remove folders recursively. Simple example: ```./rm.py -r /System``` ( Don't try this at home:) ). It takes only one
   option:
   - <font size="4">-r</font> means remove all content recursively. 
   
4) <font size="4">__sort.py__</font>. It simply sorts file. It works as UNIX-command <font size="4">sort</font>.
It can work in pipes or redirect output to a file. Simple example: ```./ls.py | ./sort.py > sorted_ls.txt```. Unfortunately, It has no options.

5) <font size="4">__grep.py__</font>. It finds all matches in a text or in stdin, it is similar to <font size="4">grep</font>. It can work in pipes.
To now, it can work with regular expressions. To now(14.12) I couldn't color a matched text in terminal, I decided to make it UPPER, this is why it has some problems while finding upper case letter/words.  Simple example ```./grep.py aa test.txt```
   
6) <font size="4">__cat.py__</font>. This script simulates __cat__ UNIX-utility. I reads file and print its content to stdout by default.
You can redirect output to a file and also read from stdin. It works in pipes. Simple example: ```./ls.pt | ./cat.py file.txt > new_file.txt```
   
7) <font size="4">__tail.py__</font>. It works as original one __tail__ UNIX-command. It takes input as a file or take it from stdin by default.
Output is in stdout by default, you can redirect it to a file by adding __>__ sign. Simple example: 
   ```./tail.py -n 10 text.txt > text_tail.txt```. It has one optional argument 
   - __-n__. Number of the lines to show. It is __impossible__ to omit __n__ while using
   our command with this option (e.g ./tail -5 - won't work). By default n=10
     
8) <font size="4">__mkdir.py__</font>. This command simply create a directory in the path it took, works as __mkdir__ UNIX-utility. It can create subdirectories.
Simple example: ```./mkdir.py -p ~/Documents/new_folder/subfolder1```. It has an additional option:
   - __-p__ allows creating intermediate directories. 
   
## The installation guide
If you want to install this project to your own machine follow these simple steps:
- clone this repository ```git clone https://github.com/keyreallkeyrealenko/UNIX_utilities.git```
- create virtual environment in a current directory and call it __venv__. 
```python3.9 -m venv venv```
  
- activate virtual environment 
```source venv/bin/activate```
  
- make the scripts executable: ```chmod + x *.py```
  
- and use these scripts as written above