import os

class Write:
    def __init__(self):
        # 필요한 인자 수를 의미함, Write <filename> <content> 이므로 3개 이상
        self.argsRequired = 3;
    
    def run(self, args):
        if(len(args) < self.argsRequired):
            print("인자를 알맞게 입력해주세요.\nwrite <filename> <content>와 같은 형식을 가집니다.\n")
            return
        
        if os.path.isfile("./" + args[1]) == False:
            print("존재하지 않는 파일입니다.\n")
            return
        
        f = open("./" + args[1], "a")

        for i in range(2,len(args)):
            args[i] = args[i].replace(r'\n', '\n')
            #개행문자 처리
            if args[i].endswith('\n'):
                f.write(args[i])

            else:
                f.write(args[i] + " ")
        f.close()

        print("\n성공적으로 " + args[1] + " 파일에 내용을 추가했습니다.\n")