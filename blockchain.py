import hashlib
from os import walk


def write(file, sender, receiver, mes):
    file.write("Sender: " + sender)
    file.write("\nReceiver: " + receiver)
    file.write("\nMessege:\n" + mes)


def get_all_blocks(path):
    file_list = []
    for (dirpath, dirnames, filenames) in walk(path):
        file_list.extend(filenames)
        break
    file_list = sorted(file_list, key=str)
    file_list = [x for x in file_list if x.startswith("block")]
    return file_list


def create_new_block(sender, receiver, mes):
    mypath = "blocks/"
    file_list = get_all_blocks(mypath)

    if "block 1.txt" not in file_list:
        file = open("blocks/" + "block 1.txt", "w+")
        write(file, sender, receiver, mes)
        file.close()

    else:
        file_list = sorted(file_list)
        file = open("blocks/" + file_list[-1], "r")
        content = file.read()
        file.close()
        hashed = hashlib.sha256(bytes(content, "utf-8")).hexdigest()
        number_of_block = file_list[-1].split(".")[0]
        number_of_block = int(number_of_block.split()[1])
        file_name = "blocks/" + "block " + str(number_of_block + 1) + ".txt"
        new_file = open(file_name, "w+")
        new_file.write(hashed + "\n")
        write(new_file, sender, receiver, mes)
        new_file.close()


def mine():
    path = "blocks/"
    file_list = get_all_blocks(path)
    for i in range(0, len(file_list) - 1):
        prev_file = open("blocks/" + file_list[i])
        prev_content = prev_file.read()
        prev_content = hashlib.sha256(bytes(prev_content, "utf-8")).hexdigest()
        prev_file.close()
        next_file = open("blocks/" + file_list[i + 1])
        next_content_hash = next_file.readline()[:-1]
        if prev_content != next_content_hash:
            return [False, len(file_list)]
    return [True, len(file_list)]
