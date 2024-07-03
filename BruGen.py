import random
from progress.bar import Bar
from random import randint

file = open("Pass.txt", 'r+')


def check(inta):
    with open('Pass.txt', 'r+') as file:
        content = file.read()
        if inta in content:
            pass
        else:
            file.write(inta + "\n")


def gr(length):
    return "".join(chr(random.randint(97, 122)) for _ in range(length))


def generate_word(length):
    return "".join(chr(randint(65, 90)) for _ in range(length))


def generate_num(summary):
    bar = Bar('Processing num ', max=summary)
    cikl = 0
    while (cikl < summary):
        name = random.randint(00000000, 99999999)
        bar.goto(cikl)
        cikl += 1
        check(str(name))
    bar.next()
    bar.finish
    con = 0
    bar2 = Bar('Processing word ', max=summary)
    while con < summary:
        name2 = generate_word(8)
        name3 = gr(8)
        bar2.goto(con)
        con += 1
        check(name2)
        check(name3)
    bar2.next()
    bar2.finish


print("█▄▄ █▀█ █░█ █▀▀ █▀▀ █▄░█")
print("█▄█ █▀▄ █▄█ █▄█ ██▄ █░▀█")
a = input("\nEnter summary: ")
generate_num(int(a))
file.close
