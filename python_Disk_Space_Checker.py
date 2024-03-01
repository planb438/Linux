import shutil

def check_disk_space(path):
    total, used, free = shutil.disk_usage(path)
    print(f"Total space: {total // (2**30)} GB")
    print(f"Used space: {used // (2**30)} GB")
    print(f"Free space: {free // (2**30)} GB")

if __name__ == "__main__":
    path = "/"
    check_disk_space(path)
