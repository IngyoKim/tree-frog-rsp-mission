import random
import time

class RSP:
    def FrogRSP():
        AnswerStr = str(input("가위, 바위, 보를 입력해주세요 : "))

        if AnswerStr == '가위':
            Answer = 0
        elif AnswerStr == '바위':
            Answer = 1
        elif AnswerStr == '보':
            Answer = 2
        else:
            print("Error!")
            exit()

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

        if TimeValue < 3:
            if GameValueStr == '개굴':
                if Answer == ComputerValue:
                    print("당신은 승리하셨습니다!")
                else:
                    print("당신은 패배하셨습니다!")
            elif GameValueStr == '이겼다':
                if ComputerValue - Answer == 1 or (ComputerValue == 0 and Answer == 2):
                    print("당신은 승리하셨습니다!")
                else:
                    print("당신은 패배하셨습니다!")
            elif GameValueStr == '졌다':
                if Answer - ComputerValue == 1 or (Answer == 0 and ComputerValue == 2):
                    print("당신은 승리하셨습니다!")
                else:
                    print("당신은 패배하셨습니다!")
            else:
                print("Error!")
                exit()
        else:
            print("당신은 시간초과로 패배하셨습니다!")

    def HardFrogRSP():
        ReplyValue = random.randint(1,10)
        print("이번의 숫자는 : {}".format(ReplyValue))
        AnswerStr = str(input("가위, 바위, 보를 입력해주세요 : "))

        if AnswerStr == '가위':
            Answer = 0
        elif AnswerStr == '바위':
            Answer = 1
        elif AnswerStr == '보':
            Answer = 2
        else:
            print("Error!")
            exit()

        StartTime = time.time()
        for i in range(1, 11):
            RandomValue = random.randint(0, 2)

            if RandomValue == 0:
                RandomValueStr = '가위'
            elif RandomValue == 1:
                RandomValueStr = '바위'
            else:
                RandomValueStr = '보'

            if RandomValue == 0 and i == ReplyValue:
                ComputerValueStr = '가위'
                ComputerValue = 0
            elif RandomValue == 1 and i == ReplyValue:
                ComputerValueStr = '바위'
                ComputerValue = 1
            elif RandomValue == 2 and i == ReplyValue:
                ComputerValueStr = '보'
                ComputerValue = 2
            print("상대는 [{}]를 냈습니다.".format(RandomValueStr))
        GameValueStr = str(input("선택은? : "))
        EndTime = time.time()
        TimeValue = EndTime - StartTime

        if TimeValue < 3:
            if GameValueStr == '개굴':
                if Answer == ComputerValue:
                    print("당신은 승리하셨습니다!")
                else:
                    print("당신은 패배하셨습니다!")
            elif GameValueStr == '이겼다':
                if ComputerValue - Answer == 1 or (ComputerValue == 0 and Answer == 2):
                    print("당신은 승리하셨습니다!")
                else:
                    print("당신은 패배하셨습니다!")
            elif GameValueStr == '졌다':
                if Answer - ComputerValue == 1 or (Answer == 0 and ComputerValue == 2):
                    print("당신은 승리하셨습니다!")
                else:
                    print("당신은 패배하셨습니다!")
            else:
                print("Error!")
                exit()
        else:
            print("당신은 시간초과로 패배하셨습니다!")

print("청개구리 가위바위보를 시작합니다.")
RSP.FrogRSP()
ReplayGameValue = int(input("게임을 새로 시작하려면 1, 종료하려면 2, 하드모드를 하려면 3을 입력하세요.\n"))

while True:
    if ReplayGameValue == 1:
        RSP.FrogRSP()
        ReplayGameValue = int(input("게임을 새로 시작하려면 1, 종료하려면 2, 하드모드를 하려면 3을 입력하세요.\n"))
    elif ReplayGameValue == 2:
        exit()
    elif ReplayGameValue == 3:
        RSP.HardFrogRSP()
        ReplayGameValue = int(input("게임을 새로 시작하려면 1, 종료하려면 2, 하드모드를 하려면 3을 입력하세요.\n"))
    else:
        print("Error!")
        exit()