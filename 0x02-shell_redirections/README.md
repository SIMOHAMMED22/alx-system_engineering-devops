Write a script that prints “Hello, World”, followed by a new line to the standard output.: echo "Hello, World" / Write a script that displays a confused smiley "(Ôo)'.: echo \"\(Ôo\)\' / Display the content of the /etc/passwd file. : cat /etc/passwd
Display the content of /etc/passwd and /etc/hosts : cat /etc/passwd /etc/hosts/ Display the last 10 lines of /etc/passwd : tail -n 10 /etc/passwd 
Display the first 10 lines of /etc/passwd :head -n 10 /etc/passwd
Write a script that displays the third line of the file iacta.: cat iacta | head -3 | tail -1 / Write a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line. :echo "Best School" > \\\*\\\\\'\"Best\ School\"\\\'\\\\\*\$\\\?\\\*\\\*\\\*\\\*\\\*\:\)/ Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.: ls -la > ls_cwd_content/ Write a script that duplicates the last line of the file iacta: tail -n 1 iacta >> iacta/ Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders. :find . -type f -name "*.js" -delete / Write a script that counts the number of directories and sub-directories in the current directory.: find . -type d -not -path '.' | wc -l/ Create a script that displays the 10 newest files in the current directory.
: ls -lt | head -n 10/ Create a script that takes a list of words as input and prints only words that appear exactly ONCE : sort |uniq -u
Display lines containing the pattern “root” from the file /etc/passwd : grep "root" /etc/passwd / Display the number of lines that contain the pattern “bin” in the file /etc/passwd : grep -c "bin" /etc/passwd / Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.: grep -A 3 "root" /etc/passwd / Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.: grep -v 'bin' /etc/passwd
Display all lines of the file /etc/ssh/sshd_config starting with a letter.: grep '^[a-zA-Z]' /etc/ssh/sshd_config
Replace all characters A and c from input to Z and e respectively . : tr Ac Ze / Create a script that removes all letters c and C from input. :echo "$1" | tr -d 'cC'
Create a script that removes all letters c and C from input.

Write a script that reverse its input.rev
Write a script that displays all users and their home directories, sorted by users . : cut -d : -f 1,6 /etc/passwd /Write a command that finds all empty files and directories in the current directory and all sub-directories.: find . -empty -printf "%P\n" / Write a command that finds all empty files and directories in the current directory and all sub-directories. : find . -empty \( -type d -o -type f \) -printf '%f\n' 
Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.: find -type f -name '*.gif' -printf '%f\n' | rev | cut -c 5- | rev | LC_ALL=C sort -f
Create a script that decodes acrostics that use the first letter of each line. : cut -c1 | paste -sd ''
 : cut -c1 | paste -sd ''



 
