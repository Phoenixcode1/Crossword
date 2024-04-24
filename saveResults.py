
def prepare_results(player,time,ileGracz):
    ret = f"Player: {player} is the winner with total time of solving: {time}. "
    if ileGracz == 1 :
        ret += "He/she plays Solo."
    if ileGracz > 1 :
        ret += f"He/she plays with {ileGracz} players."
    append_to_file("Wyniki.txt", ret)


def append_to_file(file_path, content):
    with open(file_path, "a") as file:
        file.write(content)
        file.write("\n")  # Dodanie nowej linii po dopisaniu zawartości


