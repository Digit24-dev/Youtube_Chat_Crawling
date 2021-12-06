from builtins import print, KeyboardInterrupt, type, set, len, list, str

import pytchat #import LiveChat
import pafy
import pandas as pd
import random
import time

# 유튜브 API V_3 의 api 키 받아서 입력
pafy.set_api_key('')

# 유튜브 라이브 주소를 입력해 주세요.
# 예를 들어, 다음과 같은 주소가 있을 때에
# https://www.youtube.com/watch?v=GoXPbGQl-uQ
# "GoXPbGQl-uQ" 이 부분이 video_id 입니다.

video_id = 'GoXPbGQl-uQ'

id_list = set("")
start_flag = False
cast_lot = False

v = pafy.new(video_id)
title = v.title
author = v.author
published = v.published

#empty_frame = pd.DataFrame(columns=['제목', '채널 명', '스트리밍 시작 시간', '댓글 작성자', '댓글 내용', '댓글 작성 시간'])
#empty_frame.to_csv('./youtube.csv', encoding="UTF-8")

chat = pytchat.create(video_id)           # topchat_only='FALSE'

while chat.is_alive():

    if cast_lot:
        break

    try:
        data = chat.get()
        items = data.items
        for c in items:
            if c.author.name == "JH Choi":
                if c.message == "끝!" :
                    start_flag = False
                elif c.message == "시작!" :
                    start_flag = True

                if c.message == "추첨!" :
                    cast_lot = True

            if start_flag:
                if c.message.find("도전") == -1:
                    continue
                id_list.add(c.author.name)

            print(f"{c.datetime} [{c.author.name}] - {c.message}")

            # time.sleep(3)
            data.sync_items()
            # data2 = {'제목' : [title], '채널 명' : [author], '스트리밍 시작 시간' : [published], '댓글 작성자' : [c.author.name], '댓글 내용' : [c.datetime], '댓글 작성 시간' : [c.message]}
            # result = pd.DataFrame(data2)
            # result.to_csv('youtube.csv', mode='a', header=False, encoding='UTF-8')

    except KeyboardInterrupt:
        chat.terminate()
        print(id_list)
        break

print("모집 끝! 현재까지 " + str(len(id_list)) + "명의 인원이 모였습니다!")
time.sleep(2)
print("추첨을 시작합니다!")

time.sleep(1)
print("3!!!")

time.sleep(1)
print("2!!!")

time.sleep(1)
print("1!!!")
print()

time.sleep(1)
print("당첨자는~!?")
print()

time.sleep(3)
print(">>>>>>>   " + random.choice(list(id_list)) + " 님!  <<<<<<<<")
print("축하합니다!!!!!")

time.sleep(5)
print("프로그램을 종료합니다.")


