from transitions.extensions import GraphMachine
from utils import send_text_message
from utils import send_image_message
from utils import send_video_message
from pics import picshow
from song import album
from test import speak
from t import song
import random

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "人生語錄"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "官方帳號"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "當月行程"
    
    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "投票總匯"
    
    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() == "video"
    
    def is_going_to_state6(self, event):
        text = event.message.text
        return text.lower() == "功能總覽"

    def is_going_to_state7(self, event):
        text = event.message.text
        return text.lower() == "隨機圖片"
    
    def is_going_to_state8(self, event):
        text = event.message.text
        print('this is going to state8')
        print(text)
        return text.lower() == "我要找歌"

    def is_going_to_state9(self, event):
        text = event.message.text
        test = text.replace(" ", "")
        print('this is going to state9')
        print(test)
        answer = (test.encode('UTF-8').isalpha() or text.lower() == "Over & Over".lower() or text.lower() == "Over&Over".lower() or text == "25" or text.lower() == "O.M.G".lower() or text.lower() == "I WON'T LET YOU GO".lower() or text.lower() == "97 YOUNG & RICH".lower() or text.lower() == "97 YOUNG&RICH".lower() or text.lower() == "Don't Care".lower() or text.lower() == "She's A Monster".lower() or text.lower() == "1:31AM".lower() or text.lower() == "Can't".lower() or text == "이젠" or text.lower() == "Crash & Burn".lower() or text.lower() == "Crash&Burn".lower() or text.lower() == "Yo 翻天覆地 Yo".lower() or text.lower() == "Yo翻天覆地Yo".lower() or text ==  "如果沒有離別" or text == "備忘録" or text ==  "この胸に" or text == "2" or text == "1+1")
        print(answer)
        return answer
    
    def is_going_to_state11(self, event):
        text = event.message.text
        print('this is going to state11')
        print(text)
        return text.lower() == "我要找專輯"

    def is_going_to_state12(self, event):
        text = event.message.text
        test = text.replace(" ", "")
        test = test.lower()
        print('this is going to state12')
        print(test)
        answer = (test.encode('UTF-8').isalpha() or test.find("me") != -1 or test.find("present") != -1 or test.find("hey") != -1 or test.find("let") != -1 or test.find("sing") != -1 or test.find("7") != -1 or test.find("got it") != -1 or test.find("last piece") != -1 or test.find("breath") != -1 or test.find("spinning") != -1 or test.find("arrival") != -1 or test.find("departure") != -1 or test.find("turbulence") != -1 or test.find("翻天") != -1)
        print(answer)
        return answer

    def is_going_to_state14(self, event):
        text = event.message.text
        print('this is going to state14')
        print(text)
        return text.lower() == "雲端連結"

    def on_enter_state1(self, event):
        print("I'm entering state2")
        reply_token = event.reply_token
        send_text_message(reply_token, speak())
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")
        url = 'https://twitter.com/GOT7Official?s=20'
        url1 = 'https://www.vlive.tv/channel/ECDF'
        url2 = 'https://www.facebook.com/GOT7Official/'
        url3 = 'https://www.instagram.com/got7.with.igot7/?hl=zh-tw'
        url4 = 'https://weibo.com/JYPEGOT7?topnav=1&wvr=6&topsug=1'
        url5 = 'https://fans.jype.com/Portal'
        url6 = 'https://www.youtube.com/channel/UC8HEl74jL3bLLwfDP1OALxw'
        url7 = 'https://www.instagram.com/jaybnow.hr/'
        url8 = 'https://www.instagram.com/marktuan/'
        url9 = 'https://www.instagram.com/jacksonwang852g7/'
        url10 = 'https://www.instagram.com/jinyoung_0922jy/'
        url11 = 'https://www.instagram.com/333cyj333/'
        url12 = 'https://www.instagram.com/bambam1a/'
        url13 = 'https://www.instagram.com/yu_gyeom/'
        url14 = 'https://twitter.com/marktuan'
        url15 = 'https://twitter.com/JacksonWang852'
        url16 = 'https://twitter.com/GOTYJ_Ars_Vita?s=20'
        url17 = 'https://twitter.com/BamBam1A'
        url18 = 'https://twitter.com/real_Kimyugyeom?s=20'
        url19 = 'https://weibo.com/u/6636606962?topnav=1&wvr=6&topsug=1&is_all=1'
        url20 = 'https://weibo.com/jacksonwangG7?topnav=1&wvr=6&topsug=1'
        
        account = "官方推特" + '\n' + url + '\n' + "官方vlive" + '\n' + url1 + '\n' + "官方FB" + '\n' + url2 + '\n' + "官方ins" + '\n' + url3 + '\n' + "官方微博" + '\n' + url4 + '\n' + "官方fans" + '\n' + url5 + '\n' + "官方youtube" + '\n' + url6 + '\n\n' + "成員ins" + '\n' + "林在范：jaybnow.hr" + '\n' + url7 + '\n' + "段宜恩：marktuan" + '\n' + url8 + '\n' + "王嘉爾：jacksonwang852g7" + '\n' + url9 + '\n' + "朴珍榮：jinyoung_0922jy" + '\n' + url10 + '\n' + "崔榮宰：333cyj333" + '\n' + url11 + '\n' + "BamBam：bambam1a" + '\n' + url12 + '\n' + "金有謙：yu_gyeom" + '\n' + url13 + '\n\n' + "成員推特" + '\n' + "段宜恩：Mark Tuan" + '\n' + url14 + '\n' + "王嘉爾：Jackson Wang 王嘉爾 왕잭슨" + '\n' + url15 + '\n' + "崔榮宰：CYJ" + '\n' + url16 + '\n' + "BamBam：BamBam" + '\n' + url17 + '\n' + "Yugyeom：김유겸" + '\n' + url18 + '\n\n' + "成員微博" + '\n' + "段宜恩：段宜恩" + '\n' + url19 + '\n' + "王嘉爾：王嘉爾" + '\n' + url20
        reply_token = event.reply_token
        send_text_message(reply_token, account)
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")
        schedule = "🗓12/31(四) AIS5GVirtualCountdown慶典" + '\n' + "時間: 19:00" + '\n' + "觀看平台:AISPLAY"
        reply_token = event.reply_token
        send_text_message(reply_token, schedule)
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")

    def on_enter_state4(self, event):
        print("I'm entering state4")
        url = 'https://m.weibo.cn/status/4581016964438995?'
        url1 = 'https://m.weibo.cn/status/4577554092523865?'
        url2 = 'https://m.weibo.cn/status/4582489358599640?'
        url3 = 'https://m.weibo.cn/status/4580612332332933?'
        url4 = 'https://m.weibo.cn/status/4580844591123170?'
        url5 = 'http://curaprox-gda.co.kr/'

        vote = "1、首爾歌謠大賞：⏰1月24日 23:00" + '\n' + "投票教程:" + '\n' + url + '\n' + "投票軟體:The 30th SMA Official Vote APP" + '\n' + "入圍部門:本賞/人氣賞/韓流特別賞/SMA傳奇新人獎" + '\n' + "注意事項:主攻本賞(Main Awards)" + '\n\n' + "2、Gaon： ⏰二輪截止 12月27日 17:00 三輪截止 1月10日 17:00" + '\n' + "投票教程:" + '\n' + url1 + '\n' + "投票軟體: Mubeat" + '\n\n' + "3、金唱片（大陸區）：⏰12月31日 23:59" + '\n' + "投票教程:" + '\n' + url3 + '\n' + "投票軟體: QQ音樂" + '\n\n' + "4、金唱片（海外區）：⏰12月31日 23:00" + '\n' + "投票教程:" + '\n' + url4 + '\n' + "投票軟體: " + '\n' + url5 + '\n' + "注意事項: 建議使用Chrome"

        reply_token = event.reply_token
        send_text_message(reply_token, vote)
        self.go_back()

    def on_exit_state4(self):
        print("Leaving state4")

    def on_enter_state5(self, event):
        print("I'm entering state5")
        reply_token = event.reply_token  
        url = 'https://drive.google.com/uc?export=download&id=1YgrVAY1U3nmsOfDQsXgDvQrx1x44lh31'
        url1 = 'https://i.imgur.com/LPcPN01.jpg'
        send_video_message(reply_token, url, url1)
        self.go_back()

    def on_exit_state5(self):
        print("Leaving state5")
    
    def on_enter_state6(self, event):
        print("I'm entering state6")
        reply_token = event.reply_token  
        tell = "✨功能總覽：" + '\n' + "1.官方帳號(點擊選單第一排第二個)：" + '\n' + "包含官方 & 團員所有社交軟體的帳號" + '\n' + "2.人生語錄(點擊選單第一排第三個)：" + '\n' + "每一位成員有8-9句語錄 隨機回覆充滿驚喜與力量💚" + '\n' + "3.投票總匯(點擊選單第二排第一個)：" + '\n' + "年末回歸不知道要去哪裡投甚麼票嗎?看這裡就對了!" + '\n' + "4.當月行程(點擊選單第二排第二個)：" + '\n' + "即時更新官宣行程 掌握GOT7行程我有💪" + '\n' + "5.隨機圖片(點擊選單第二排第三個)：" + '\n' + "將掉落隨機一張男友照 馬上存起來😍" + '\n' + "6.雲端連結(輸入「雲端連結」：" + '\n' + "含有表情包、男友照、資料庫等相簿 應有盡有!" + '\n' + "7.我要找歌(輸入「我要找歌」)：" + '\n' + "按照指示輸入要找的歌曲 會回覆對應的專輯與發行時間🎵" + '\n' + "8.我要找專輯(輸入「我要找專輯」)：" + '\n' + "按照指示輸入要找的專輯 會回覆該專輯收錄的所有歌曲🎵" + '\n' + "⚠注意事項：" + '\n' + "a.可查詢所有韓專日專歌曲 包含改版專迷你專正規專等" + '\n' + "b.除了歌曲本身即為中文以外 請以歌曲/專輯原本的英文名查詢 no哈德凱瑞no陀螺專no愛的供氧😠" + '\n' + "c.可以連續查詢 不需要每查一次就打一次我要找歌/找專輯 想換別的功能直接按選單就可以了!" + '\n' + "d.如果覺得自己應該沒輸錯但顯示錯誤 可能是現在正在錯誤的狀態 請再打一次「我要找歌」或「我要找專輯」" + '\n' + "e.在查詢過程中如果輸入後沒有立即得到回覆 可以再重新輸入一次(小bug抱歉😭)" + '\n' + "以上注意事項 如果有其他問題請聯絡被窩👇" + '\n' + "IG： ahgaseigot7777 謝謝💕"        
        send_text_message(reply_token, tell)
        self.go_back()

    def on_exit_state6(self):
        print("Leaving state6")

    def on_enter_state7(self, event):
        print("I'm entering state7")
        text = event.message.text
        print(text)
        reply_token = event.reply_token
        send_image_message(reply_token, picshow())
        self.go_back()

    def on_exit_state7(self):
        print("Leaving state7")
    
    def on_enter_state8(self, event):
        print("I'm entering state8")
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入想尋找在哪張專輯的歌曲名(除了 Yo 翻天覆地 Yo、如果沒有離別、備忘錄、この胸に 、1+1 這五首歌以外 其他需為英文歌名查詢)")
        self.advance(event)

    def on_exit_state8(self,event):
        print("Leaving state8")
        
    def on_enter_state9(self,event):
        print("I'm entering state9")
        text = event.message.text
        print(text)
        reply_token = event.reply_token
        print(album(text))
        send_text_message(reply_token, album(text))
        print("i'm here")
        self.go_back()
        
    def on_exit_state9(self):
        print("Leaving state9")
    
    def on_enter_state11(self, event):
        print("I'm entering state11")
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入想查看專輯內所有歌曲的專輯名(除了日專翻天↑覆地外 其他需輸入專輯英文名)")
        self.advance(event)

    def on_exit_state11(self,event):
        print("Leaving state11")
        
    def on_enter_state12(self,event):
        print("I'm entering state12")
        word = event.message.text
        print(word)
        reply_token = event.reply_token
        print(song(word))
        send_text_message(reply_token, song(word))
        print("i'm here")
        self.go_back()
        
    def on_exit_state12(self):
        print("Leaving state12")
    
    def on_enter_state14(self,event):
        print("I'm entering state14")
        reply_token = event.reply_token
        url = 'https://drive.google.com/drive/folders/1KBC054JqN4BWR7s-kx5asup632WZnGo5?usp=sharing'
        send_text_message(reply_token, url)
        self.go_back()
        
    def on_exit_state12(self):
        print("Leaving state12")
   