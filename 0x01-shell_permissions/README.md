Create a script that switches the current user to the user betty.: su betty / Write a script that prints the effective username of the current user.: id -un / Write a script that prints all the groups the current user is part of. : id -nu / Write a script that changes the owner of the file hello to the user betty. : chown betty hello/ Write a script that creates an empty file called hello.: touch hello / Write a script that adds execute permission to the owner of the file hello.: chmod u+x hello / Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.: chmod u+x,g+x,o+r hello
Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello : chmod a+x hello
Write a script that sets the permission to the file hello as follows:

Owner: no permission at all
Group: no permission at all
Other users: all the permissions : chmod 007 hello / Write a script that sets the mode of the file hello : chmod 753 hello / Write a script that sets the mode of the file hello the same as olleh’s mode.: chmod --reference=olleh hello / Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. :chmod -R ugo+X . / Create a script that creates a directory called my_dir with permissions 751 in the working directory.: mkdir -m 751 my_dir
/Write a script that changes the group owner to school for the file hello: chgrp school hello / Write a script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory. :chown -R vincent:staff ./ Write a script that changes the owner and the group owner of _hello to vincent and staff respectively.: chown -h vincent:staff _hello / Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.:chown --from=guillaume betty hello
 
  