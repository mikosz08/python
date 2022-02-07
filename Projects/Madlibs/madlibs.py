
from modules import common

def print_player_madlib():
    words = list()
    words.append(input("ADJECTIVE:"))
    words.append(input("NOUN:"))
    words.append(input("ADJECTIVE:"))
    words.append(input("NOUN:"))
    words.append(input("PART OF THE BODY:"))
    words.append(input("NAME OF FAVORITE DEAD ALLIANCE PALADIN:"))
    words.append(input("PAST TENSE OF BODILY FUNCTION:"))

    madlib = f"""
    Once upon a time, the {words[0]} king of Stormwind,
    Varian Wrynn, was sailing on his ship, the Pride of {words[1]},
    when suddenly an orcish warship came out of the fog! 'Battle stations!' the king ordered.
    'We will not let them take the {words[2]} {words[3]}!'
    Two troll hunters fired arrows at Varian, narrowly missing his {words[4]}.
    'By {words[5]}'s ghost! That was close Varian {words[6]}."""

    print(madlib)

def main():
    import os
    cmd = 'mode 140,20'
    os.system(cmd)
    
    print("=~" * 69)

    print_player_madlib()

    print("=~"* 69)


if __name__ == "__main__":
    main()
    input("\nnom")
