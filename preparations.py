def prepare_dict_words(path):
    dic = {}
    with open(path, "r") as file:
        content = file.read()
        content = content.split("\n")
        for i in range(len(content)):
            word = ""
            description = ""
            line = content[i].split(":")
            word += line[0]
            description += line[1]
            dic[word] = description
    return dic
