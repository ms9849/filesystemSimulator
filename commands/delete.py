import os

class Delete:
    def __init__(self):
        # 필요한 인자 수를 의미함, delete <filename> 이므로 2개의 인자가 요구 됨.
        self.argsRequired = 2;
    
    def run(self, args):
        if(len(args) != self.argsRequired):
            print("인자를 알맞게 입력해주세요.\ndelete <filename>와 같은 형식을 가집니다.\n")
            return
        
        if os.path.isfile("./" + args[1]) == False:
            print("존재하지 않는 파일입니다.\n")
            return
        
        os.remove("./" + args[1])

        print("성공적으로 " + args[1] + " 파일을 삭제했습니다.\n")