import os

class Create:
    def __init__(self):
        # 필요한 인자 수를 의미함, create <filename> <content> 이므로 3개 이상
        self.argsRequired = 3;
    
    def run(self, args):
        if(len(args) < self.argsRequired):
            print("인자를 알맞게 입력해주세요.\ncreate <filename> <content>와 같은 형식을 가집니다.\n")
            return
        
        if os.path.isfile("./" + args[1]) == True:
            print("이미 같은 명의 파일이 존재합니다.\n")
            return
        
        f = open("./" + args[1], "w")

        for i in range(2,len(args)):
            args[i] = args[i].replace(r'\n', '\n')
            #개행문자 처리
            if args[i].endswith('\n'):
                f.write(args[i])

            else:
                f.write(args[i] + " ")
        f.close()

        print("성공적으로 " + args[1] + " 파일을 생성했습니다.\n")