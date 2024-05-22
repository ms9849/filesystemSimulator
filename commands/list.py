import os

class List:
    def __init__(self):
        # 필요한 인자 수를 의미함, 인자가 존재하지 않으므로 1이 요구 됨.
        self.argsRequired = 1;
    
    def run(self, args):
        if(len(args) != self.argsRequired):
            print("인자를 알맞게 입력해주세요.\nlist 명령어는 인자를 가지지 않습니다.\n")
            return
        
        if len(os.listdir(os.getcwd())) == 0:
            print("디렉토리가 비어있습니다.")
            return
        
        files = os.listdir(os.getcwd())
        for i in files:
            print(i, end=" ")

        print("\n성공적으로 디렉토리 내의 파일들을 출력했습니다.\n")