import os

class Removedir:
    def __init__(self):
        # 필요한 인자 수를 의미함, rmdir <dirname> 이므로 2개의 인자가 요구 됨.
        self.argsRequired = 2;
    
    def run(self, args):
        if(len(args) != self.argsRequired):
            print("인자를 알맞게 입력해주세요.\nrmdir <dirname>와 같은 형식을 가집니다.\n")
            return
        
        if os.path.isdir("./" + args[1]) == False:
            print("존재하지 않는 디렉토리입니다.\n")
            return
        
        if len(os.listdir("./" + args[1])) != 0:
            print("디렉토리가 비어있지 않습니다.")
            return

        os.rmdir("./" + args[1])

        print("성공적으로 " + args[1] + " 디렉토리를 삭제했습니다.\n")