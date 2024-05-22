import os

class Search:
    def __init__(self):
        # 필요한 인자 수를 의미함, search <filename> 이므로 2개의 인자가 요구 됨.
        self.argsRequired = 2;
    
    def run(self, args):
        if(len(args) != self.argsRequired):
            print("인자를 알맞게 입력해주세요.\nsearch <filename>와 같은 형식을 가집니다.\n")
            return
        
        currentDir = os.getcwd()
        for root, dirs, files in os.walk(currentDir):
            for file in files:
                if file == args[1]:
                    filePath = os.path.join(root, file)
                    print("성공적으로 파일을 발견했습니다, 경로는 " +  filePath + " 입니다.")
                    return
        
        print("파일을 찾을 수 없습니다.")