import os

class Read:
    def __init__(self):
        # 필요한 인자 수를 의미함, Read <filename> 이므로 2개
        self.argsRequired = 2;
    
    def run(self, args):
        if(len(args) != self.argsRequired):
            print("인자를 알맞게 입력해주세요.\nread <filename>와 같은 형식을 가집니다.\n")
            return
        
        if os.path.isfile("./" + args[1]) == False:
            print("존재하지 않는 파일입니다.\n")
            return
        
        f = open("./" + args[1], "r")
        content = f.read()
        print(content)
        f.close()

        print("\n성공적으로 " + args[1] + " 파일을 읽었습니다.\n")