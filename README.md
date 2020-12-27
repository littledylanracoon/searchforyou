# SearchGOT7 bot：find whatever you want for GOT7 here!


## 發想
因為自己經營一個和追星有關的ig帳號，平常有許多追蹤者會詢問有關偶像的大小事，一一回覆較耗時間，即時性消息一個個發給所有人也十分麻煩；所以設計了一個多功能的linebot讓大家能透過平台隨時獲得資訊。

## 設計
透過圖文選單與輸入關鍵字，可多功能獲得不同方面的資訊，也透過line manager定時推播每日團體行程的訊息，並包含了功能總覽的使用說明讓使用者更能了解如何使用。

## 基本資訊
名稱:SearchGOT7bot <br /> <br />
![image](https://github.com/littledylanracoon/searchforyou/blob/master/img/linebot.jpg)
![image](https://github.com/littledylanracoon/searchforyou/blob/master/img/bot.png)  <br />
## 功能:
![image](https://github.com/littledylanracoon/searchforyou/blob/master/img/function.jpg)
![image](https://github.com/littledylanracoon/searchforyou/blob/master/img/pic.png)
除了選單上的功能 還有其他：
a.輸入「雲端連結」:回覆含有各樣相簿的雲端連結
b.輸入「video」:回覆療癒嗓音的唱歌影片
c.輸入「我要找歌」:可輸入要找的歌曲 會回覆對應的專輯與發行時間🎵 可查詢所有韓專日專歌曲 包含改版專迷你專正規專等等
![image](https://github.com/littledylanracoon/searchforyou/blob/master/img/song.jpg) <br />
智慧辨別：即使只輸入關鍵字也能找到!去掉空格不分大小寫皆能成功搜尋~ <br />
d.輸入「我要找專輯」:可輸入要找的專輯 會回覆該專輯收錄的所有歌曲🎵
![image](https://github.com/littledylanracoon/searchforyou/blob/master/img/album.jpg) <br />

可以連續查詢 想換別的功能直接按選單就可以了! 

## FSM圖
![image](https://github.com/littledylanracoon/searchforyou/blob/master/fsm.png)

### state說明

user:開始使用<br />
state1:輸入人生語錄<br />
state2:輸入官方帳號<br />
state3:輸入當月行程<br />
state4:輸入投票總匯<br />
state5:輸入video<br />
state6:輸入功能總覽<br />
state7:輸入隨機圖片<br />
state8:輸入我要找歌<br />
state9:依照輸入的歌曲 顯示其所在的專輯<br />
state10:找完歌曲後自動進入此state 等待下一個動作(繼續查詢或換一個功能 功用像lamda任意門)<br />
state11:輸入我要找專輯<br />
state12:依照輸入的專輯 顯示其所收錄的所有歌曲<br />
state13:找完專輯後自動進入此state 等待下一個動作(繼續查詢或換一個功能 功用像lamda任意門)<br />
state14:輸入雲端連結<br />

作者：林筠倩 資訊111 


