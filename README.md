# <center>UNIX utilities in Python</center>

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

5) <font size="4">__grep.py__</font>. It finds all matches in a text or in stdin it is similar to <font size="4">grep</font>. It can work in pipes, but
to now (13.12.21) __can't work with regular expressions__ (I'll fix it). Simple example ```./grep.py aa test.txt```