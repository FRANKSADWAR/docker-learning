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


if __name__ == "__main__":
    get_process_info()