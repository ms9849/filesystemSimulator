import os

class Makedir:
    def __init__(self):
        # 필요한 인자 수를 의미함, mkdir <dirname> 이므로 2개의 인자가 요구 됨.
        self.argsRequired = 2;
    
    def run(self, args):
        if(len(args) != self.argsRequired):
            print("인자를 알맞게 입력해주세요.\nmkdir <dirname>와 같은 형식을 가집니다.\n")
            return
        
        if os.path.isdir("./" + args[1]) == True:
            print("이미 같은 명의 디렉토리가 존재합니다.\n")
            return
        
        os.mkdir("./" + args[1])

        print("성공적으로 " + args[1] + " 디렉토리를 생성했습니다.\n")