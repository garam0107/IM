testcase=int(input())
for tc in range(1,testcase+1):
    ans=0
    test=input().split()
    N=int(test[0])   # 버튼의 개수
    BLUE=[]
    ORANGE=[]
    # 각 로봇이 눌러야 할 버튼 번호를 각각 저장
    for i in range(1,len(test),2):
        if test[i]=='B':
            BLUE.append(int(test[i+1]))
        else:
            ORANGE.append(int(test[i+1]))
    nowB=1 # 처음 로봇의 위치
    nowO=1
    time=0
    for i in range(1,len(test),2):
        if test[i]=='B':
            bt_location=BLUE.pop(0)         # 눌러야 할 버튼 위치
            Bmove=abs(bt_location-nowB)+1   # 이동시간 + 누르는시간 1
            time+=Bmove                     # 총 시간에 더하기
            nowB=bt_location                # 블루의 위치를 누른 버튼의 위치로 갱신

            # 블루가 버튼을 누르는데 걸리는 시간동안
            # 오렌지가 이동하는것을 확인
            if len(ORANGE)!=0:
                bt_location=ORANGE[0]       # 오랜지가 눌러야할 버튼의 위치
                if Bmove > abs(bt_location-nowO): #B가 버튼 누르는동안에 O가 다음 버튼까지 이동이가능하다면
                    nowO=bt_location              # O를 다음 버튼위치까지 이동
                else:
                    if nowO<bt_location:          # 우측으로 이동해야 한다면
                        nowO+=Bmove               # B가 걸리는 시간만큼 더하고
                    else:
                        nowO-=Bmove               # B가 걸리는 시간만큼 뺴준다.
        else:
            bt_location=ORANGE.pop(0)
            Omove=abs(bt_location-nowO)+1
            time+=Omove
            nowO=bt_location

            if len(BLUE)!=0:
                bt_location=BLUE[0]
                if Omove>abs(bt_location-nowB):
                    nowB=bt_location
                else:
                    if nowB<bt_location:
                        nowB+=Omove
                    else:
                        nowB-=Omove

    print(f'#{tc} {time}')