# Understanding Docker
Docker is a platform for building, deploying and managing applications
using lightweight, portable pakcges called containers.

## Processes
A process is one running instance of a program, and the Linux kernel tracks that process with a Process ID (PID), its
parent PID (PPID), an owning user (UID), a current directory, environment variables, memory and a table of open files.

A container is an ordinary process in your machine isolated by Linux to so it sees its own file system, network and 
process list, while sharing the host's kernel.

Every process is created by another one.

The very first process a kernel starts is PID 1 (the init system, usually systemd); its starts the rest of the system, adops orphaned children
and it ever exits the whole machine goes down.

``` ps -ef | head -n 15 ```


Processes are controlled with signals. SIGTERM (15) politely asks a process to stop so it can clean up.

SIGKILL (9) ends a process instantly with no chance to clean up and cannot be caught. A finished process returns an exit code.

0 means success, and a code above 128 means "killed by signal"

## Daemons and services
A daemon is a long-running background process with no terminal attached, usually by the init system at boot, restarted if it 
crashes and it writes logs to files or the journal.

Databases, web servers, SSH, and docker itself are daemons. Yout talk to a daemon through a socket or network port.

``` systemctl list-units --type=service ```

Image: 

Container: a running instance of an image. A container is an ordeinary process started inside its own namespace. It shares the host kernel, which is why it starts in milliseconds.

Registry: a server that stores Docker images i.e DockerHub, Github Container Registry, Amazon Elastic Container Registry (ECR)

Volume: storage that outlives ( persists ) a container

Network: virtual network letting docker containers find each other by name

Compose: A YAML file desribing several containers that run together

The Linux kernel exposes each process under the proc/ folder.
