filename = "KakaoTalk_20240410_2227_54_665_group.txt"
kt_file = open(filename, 'r',encoding='utf8')
kt_file_content = kt_file.readlines()
kt_file.close()

speaker_count = dict() #딕셔너리 하나 생성 -> 누가보내고 어떤 내용을 보냈는지 사람별로 구분하여 저장할 수 있게 세팅

kt_file_content = kt_file_content[4:] #3번째줄까지는 쓸데없는 내용

name = "" 
for line in kt_file_content: #줄별로 반복
    if "님을 초대하였습니다." in line: #메세지가 아닌 부분 예외처리
        continue
    elif line.count('-') == 30:
        continue
    elif "님이 나갔습니다." in line:
        continue
    elif line[0] == '[': #사람이름별로 메세지 저장
        line = line.strip('\n').split("] ") #사람이름만 잘라오기 위해
        name = line[0][1:]
        data = "] ".join(line[2:]) 
        if name in speaker_count:   #ditc의 key값이 있을 경우에는 이렇게 하고요
            speaker_count[name].append(data)
        else:                       #없을때는 이렇게 합니다
            speaker_count[name]=[data]
    else:
        speaker_count[name][-1] += line.strip('\n') #줄바꿈을 했을때

while True:
    command = input("입력 : ")
    if command == "\stop":
        break
    elif command == "\laugh":
        laugh = ['ㅋㅋ','웃겨','웃김'] #\laugh 리스트에 웃음과 관련된 단어를 저장
        for i in speaker_count: #speaker_count 안에 있는 모든 경우를 반복
            c_count = 0 #횟수를 초기회
            for j in laugh:
                for chat in speaker_count[i]: #사람별로 한 말들을 가져옴
                    if j in chat:
                        c_count += 1 
            print(i,":",c_count)
    elif command == "\cry":
        cry = ['ㅠㅠ','ㅜㅜ','슬퍼']
        for i in speaker_count:
            c_count = 0
            for j in cry:
                for chat in speaker_count[i]:
                    if j in chat:
                        c_count += 1
            print(i,":",c_count)
    elif command == "\swear":
        swear = ['ㅅㅂ','시발','ㅈㄴ','존나']
        for i in speaker_count:
            c_count = 0
            for j in swear:
                for chat in speaker_count[i]:
                    if j in chat:
                        c_count += 1
            print(i,":",c_count)
    elif command == "\\talk":
        for i in speaker_count:
            c_count = 0
            for chat in speaker_count[i]:
                c_count += 1
            print(i,":",c_count)
    else:
        for i in speaker_count:
            c_count = 0
            for chat in speaker_count[i]:
                if command in chat:
                    c_count += 1
            print(i,":",c_count)


