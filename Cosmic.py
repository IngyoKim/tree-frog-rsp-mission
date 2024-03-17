import random
import time

class RSP:
    def FrogRSP():
        AnswerStr = str(input("가위, 바위, 보를 입력해주세요 : "))
        ComputerValue = random.randint(0, 2)

        if ComputerValue == 0:
            ComputerValueStr = '가위'
        elif ComputerValue == 1:
            ComputerValueStr = '바위'
        else:
            ComputerValueStr = '보'

        StartTime = time.time()
        GameValueStr = str(input("상대는 [{}]를 냈습니다 : ".format(ComputerValueStr)))
        EndTime = time.time()
        TimeValue = EndTime - StartTime

        if AnswerStr == '가위':
            Answer = 0
        elif AnswerStr == '바위':
            Answer = 1
        else:
            Answer = 2

        if TimeValue < 3:
            if GameValueStr == '개굴':
                if Answer == ComputerValue:
                    print("당신은 승리하셨습니다!")
                else:
                    print("당신은 패배하셨습니다!")
            elif GameValueStr == '졌다':
                if ComputerValue - Answer == 1 or (ComputerValue == 0 and Answer == 2):
                    print("당신은 승리하셨습니다!")
                else:
                    print("당신은 패배하셨습니다!")
            elif GameValueStr == '이겼다':
                if Answer - ComputerValue == 1 or (Answer == 0 and ComputerValue == 2):
                    print("당신은 승리하셨습니다.")
                else:
                    print("당신은 패배하셨습니다!")
        else:
            print("당신은 시간초과로 패배하셨습니다!")

print("청개구리 가위바위보를 시작합니다.")
RSP.FrogRSP()
ReplayGameValue = int(input("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.\n"))
while True:
    if ReplayGameValue == 1:
        RSP.FrogRSP()
        ReplayGameValue = int(input("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.\n"))
    else:
        exit()