import pytchat #import LiveChat
import pafy
import pandas as pd
import time

pafy.set_api_key('AIzaSyCYq4WSuf4jjYyV6nxHVpBfASzfQeA6niw')

video_id = 'cqRvVIQrUQc'

v = pafy.new(video_id)
title = v.title
author = v.author
published = v.published

empty_frame = pd.DataFrame(columns=['제목', '채널 명', '스트리밍 시작 시간', '댓글 작성자', '댓글 내용', '댓글 작성 시간'])
empty_frame.to_csv('./youtube.csv', encoding="UTF-8")

chat = pytchat.create(video_id)           # topchat_only='FALSE'

while chat.is_alive():
    try:
        data = chat.get()
        items = data.items
        for c in items:
            print(f"{c.datetime} [{c.author.name}] - {c.message}")
            time.sleep(3)
            data.sync_items()
            data2 = {'제목' : [title], '채널 명' : [author], '스트리밍 시작 시간' : [published], '댓글 작성자' : [c.author.name], '댓글 내용' : [c.datetime], '댓글 작성 시간' : [c.message]}
            result = pd.DataFrame(data2)
            result.to_csv('youtube.csv', mode='a', header=False, encoding='UTF-8')
    except KeyboardInterrupt:
        chat.terminate()
        break


