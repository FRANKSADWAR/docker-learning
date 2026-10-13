import os


def get_process_info():
    pid = os.getpid()

    print("pid:", pid, "parent:", os.getppid(), "user id:", os.getuid())
    print("working dir", os.getcwd())
    print("PATH starts with:", os.environ["PATH"][:40])
    print("Open file descriptions: ", sorted(os.listdir(f"/proc/{pid}/fd")))
    documents =os.listdir("/home/billy/Documents")
    for doc in documents:
        print(doc)

def parent_child_fork():
    child = os.fork()
    if child == 0:
        os.execvp("Sleep", ["sleep","30"]) ## The child becomes the sleep program
    else:
        print("parent", os.getpid(), "started child", child)
        os.waitpid(child,0) ## parent waits for the child to finish
        print("Child finished")

if __name__ == "__main__":
    #get_process_info()
    parent_child_fork