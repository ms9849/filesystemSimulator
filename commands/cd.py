import os

class Changedir:
    def __init__(self):
        # 필요한 인자 수를 의미함, cd <dirname> 이므로 2개의 인자가 요구 됨.
        self.argsRequired = 2;
    
    def run(self, args):
        if(len(args) != self.argsRequired):
            print("인자를 알맞게 입력해주세요.\ncd <dirname>와 같은 형식을 가집니다.\n")
            return
        
        if os.path.isdir("./" + args[1]) == False:
            print("존재하지 않는 디렉토리입니다.\n")
            return
        
        os.chdir("./" + args[1])

        print("성공적으로 작업 디렉토리를 " + args[1] + " 로 변경했습니다.\n")