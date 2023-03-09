Create a script that switches the current user to the user betty.: su betty / Write a script that prints the effective username of the current user.: id -un / Write a script that prints all the groups the current user is part of. : id -nu / Write a script that changes the owner of the file hello to the user betty. : chown betty hello/ Write a script that creates an empty file called hello.: touch hello / Write a script that adds execute permission to the owner of the file hello.: chmod u+x hello / Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.: chmod u+x,g+x,o+r hello
Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello : chmod a+x hello
Write a script that sets the permission to the file hello as follows:

Owner: no permission at all
Group: no permission at all
Other users: all the permissions : chmod 007 hello / Write a script that sets the mode of the file hello : chmod 753 hello
  
