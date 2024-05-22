import os
from commands.create import Create 
from commands.delete import Delete 
from commands.read import Read
from commands.write import Write
from commands.mkdir import Makedir
from commands.rmdir import Removedir
from commands.cd import Changedir
from commands.list import List
from commands.search import Search
from commands.quit import Quit

commands = {
    'create' : Create,
    'delete' : Delete,
    'read' : Read,
    'write' : Write,
    'mkdir' : Makedir,
    'rmdir' : Removedir,
    'cd' : Changedir,
    'list' : List,
    'search' : Search,
    'quit' : Quit
}


def Simulator():
    print('OS Homework2 파일 시스템 시뮬레이터\n')

    while 1:
        userInput = input("Command: ").strip().lower();

        args = userInput.split(" ")
        if args[0] not in commands:
            print("존재하지 않는 명령어입니다.")
            continue

        cmd = commands[args[0]]()
        cmd.run(args)

if __name__ == "__main__":
    Simulator()