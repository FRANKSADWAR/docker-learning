# Understanding Docker
Docker is a platform for building, deploying and managing applications
using lightweight, portable pakcges called containers.

## Processes
A process is one running instance of a program, and the Linux kernel tracks that process with a Process ID (PID), its
parent PID (PPID), an owning user (UID), a current directory, environment variables, memory and a table of open files.

A container is an ordinary process in your machine isolated by Linux to so it sees its own file system, network and 
process list, while sharing the host's kernel.

``` ps -ef | head -n 15 ```




