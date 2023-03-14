Create a script that creates an alias. : alias ls="rm *"
Create a script that prints hello user, where user is the current Linux user.: echo hello $USER
Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program. : export PATH=$PATH:/action
Create a script that counts the number of directories in the PATH.: echo $PASH | tr ":" "\n" | wc -l
Create a script that lists environment variables. : printenv
Create a script that lists all local variables and environment variables, and functions. : set
Create a script that creates a new local variable.: BEST="School"
Write a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line. :  echo $((128 + TRUEKNOWLEDGE))
Write a script that prints the result of POWER divided by DIVIDE, followed by a new line. : echo $((POWER / DIVIDE))
