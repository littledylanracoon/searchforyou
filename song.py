import random

def album(text) :
    count = 0
    year = -1
    #word = "SUPERMAN"
    song = ['Stop stop it', 'Gimme', 'Take my hand', 'Magnetic', 'Just Tonight', 'Turn Up The Music', 'Stay', 'Moonlight', "She's A Monster", 'Girls Girls Girls', 'A',
    'skyway', 'Hard Carry', 'Boom Boom Boom', 'Prove It', 'No Jam', 'HEY', 'Mayday', 'My Home', "Who's That", 'If', 'Sick', "Dreamin'", 'Let Me',
    'Lullaby', 'Enough', 'Save You', 'No One Else', 'I Am Me', 'Sunrise', 'OMW', 'Made It', 'My Youth', 'Nobody Knows', 'Party', 'Fine', 
    'Breath', 'LAST PIECE', 'Born Ready', 'SPECIAL', 'WAVE', 'Waiting For You', 'Thank You, Sorry', '1+1', 'I Mean It', 'We Are Young',
    'If You Do', 'Put Your Hands Up', 'Feels Good', 'GOOD', 'Eyes On You', 'Tic Tic Tok', 'Confession Song', 'Every Day', 'To Star',
    'Moon U', 'Teenager', 'You Are', 'Firework', 'Remember You', 'To Me', 'Face', 
    'Lullaby', 'Enough', 'Save You', 'No One Else', 'I Am Me', 'Sunrise', 'OMW','Made It', 'My Youth', 'Nobody Knows', 'Party', 'Fine', 'MiRACLE',
    'Take Me To You', 'Come On', "1:31AM", 'Higher', 'I Love It', 'WOLO', 'King', 'Think About It', '이젠', 'Hunger', 'Phoenix',
    'Hello', 'Girls Girls Girls', 'I Like You', 'Follow Me', 'Like Oh', 'Playground', 'U Got Me', 'A', 'Bad Behavior', 'Good Tonight', 'Forever Young',
    'Just right', 'Before The Full Moon Rises', 'My Reaction', 'Nice', 'Mine', 'Back To Me', 'If You Do', 'Put Your Hands Up', 'Feels Good', 'GOOD', 'Eyes On You', 'Tic Tic Tok',
    'Fly', "Can't", 'See The Light', 'FISH', 'REWIND', 'Beggin On My Knees', 'Something Good', 'HOME RUN', 
    'Never Ever', 'Shopping Mall', 'Paradise', 'Sign', 'Go Higher', 'Q', "Don't Care", 'OUT', ' One And Only You', 'LOOK', 'The Reason', 'Hesitate', 'Us', 'Thank You',
    'Degree', 'ECLIPSE', 'The End', 'Time Out', 'Believe', 'Page', 'You Calling My Name', 'pray', 'Now Or Never', 'Thursday', 'Run Away', 'Crash & Burn', 
    'Aura', 'Crazy', 'NOT BY THE MOON', 'Love You Better', 'Trust My Love', 'Poison', 'Ride', 'Gravity', 'God Has Return', 
    'SHAKING THE WORLD', 'Yo 翻天覆地 Yo', 'GOT ur LUV', 'LAUGH LAUGH LAUGH', 'BE MY GIRL', 'AROUND THE WORLD', 'LOVE TRAIN', 'JIBBERISH', 'O.M.G', 'ANGEL', 'STAY', 'SO LUCKY', 
    'Hey Yah', 'Never Stop', 'Let me know', 'Attention', 'Over & Over', '如果沒有離別', 'TURN UP','DESSERT', 'LION BOY', 'FLASH UP', 'WHY', 'この胸に', '97 YOUNG & RICH',
    "I WON'T LET YOU GO", 'NEVER ENDING STORY', 'ZERO', 'SEESAW', 'REBORN', 'COLD', '25', 'LOVE LOOP', 'YOUR SPACE', '備忘錄', 'KARMA', 'DRUNK', 'SUMMERVIBES', 'REMEMBER ME', 'SUPERMAN',
    'LOVE LOOP', 'YOUR SPACE', '備忘錄', 'KARMA', 'DRUNK' ,'SUMMERVIBES' , 'REMEMBER ME', 'SUPERMAN', 'Sing For U', 'MY SWAGGER', 'MEET ME', 'THE New Era', 'SHINING ON YOU', 'HMMMM', '2']
    for i in song:
        text = text.replace(" ", "")
        i = i.replace(" ", "")
        if text.lower()  == i.lower() :
            year = count
            break
        count+=1  

    if text.lower() == "a":
        year = 93

    """
    test = random.randint(0,9 
    return len(song  
    return song[123],'\n' 
    return song[124],'\n' 
    return song[191],'\n' 
    """
    if year <= 10 and year >= 0:
        return "Identify 2014年11月18日 韓語正規專輯" 
    elif year <= 23 and year >= 11:
        return "Flight Log: Turbulence 2016年9月27日 韓語正規專輯" 
    elif year <= 35 and year >= 24:
        return "Present : YOU 2018年9月17日 韓語正規專輯"   
    elif year <= 45 and year >= 36:
        return "Breath of LOVE : Last Piece 2020年11月30日 韓語正規專輯" 
    elif year <= 54 and year >= 46:
        return "MAD Winter Edition 2015年11月23日 韓語改版專輯" 
    elif year <= 61 and year >= 55:
        return "7 for 7 2017年10月10日 韓語迷你專輯 2017年12月7日 韓語改版專輯" 
    elif year <= 85 and year >= 62:
        return "<Present : YOU> &ME Edition 2018年12月3日 韓語改版專輯" 
    elif year <= 91 and year >= 86:
        return "Got it? 2014年1月20日 韓語迷你專輯"   
    elif year <= 96 and year >= 92:
        return "GOT Love 2014年6月23日 韓語迷你專輯"   
    elif year <= 102 and year >= 97:
        return "Just right 2015年7月13日 韓語迷你專輯"   
    elif year <= 108 and year >= 103:
        return "MAD 2015年9月29日 韓語迷你專輯"   
    elif year <= 116 and year >= 109:
        return "FLIGHT LOG : DEPARTURE 2016年3月21日 韓語迷你專輯"   
    elif year <= 124 and year >= 117:
        return "FLIGHT LOG : ARRIVAL 2017年3月13日 韓語迷你專輯"   
    elif year <= 130 and year >= 125:
        return "Eyes On You 2018年3月12日 韓語迷你專輯"   
    elif year <= 136 and year >= 131:
        return "SPINNING TOP : BETWEEN SECURITY & INSECURITY 2019年5月20日 韓語迷你專輯"   
    elif year <= 142 and year >= 137:
        return "Call My Name 2019年11月4日 韓語迷你專輯"   
    elif year <= 151 and year >= 143:
        return "DYE 2020年4月20日 韓語迷你專輯"   
    elif year <= 163 and year >= 152:
        return "翻天↑覆地 2016年2月3日 日語正規專輯"   
    elif year <= 169 and year >= 164:
        return "Hey Yah 2016年11月16日 日語迷你專輯"   
    elif year <= 176 and year >= 170:
        return "TURN UP 2017年11月15日日語迷你專輯"   
    elif year <= 183 and year >= 177:
        return "I WON'T LET YOU GO 2019年1月30日 日語迷你專輯"  
    elif year <= 191 and year >= 184:
        return "LOVE LOOP 2019年7月31日 日語迷你專輯"  
    elif year <= 200 and year >= 192:
        return "LOVE LOOP ~Sing for U Special Edition~ 2019年12月18日 日語改版專輯"  
    elif year <= 202 and year >= 201:
        return "MY SWAGGER 2017年5月24日 日語單曲"  
    elif year <= 206 and year >= 203:
        return "THE New Era 2018年6月20日 日語單曲"  
    else:
        wrong = "沒有找到唷😢" + '\n' + "可能無法查詢的原因:" + '\n' + "把Gimme打成Give me" + "把Moon U打成Moon You" + '\n' + "把Run Away打成Runaway" + '\n' + "把GOT ur LUV打成GOT Your love" + '\n' + "把Hey Yah打成Hey Yeah" + '\n' + "把Sing For U打成Sing for you" + '\n' + "把Feels Good打成Feel Good" + '\n' + "把Every Day打成Everyday" + '\n' + "把She's A Monster打成She is A Monster" + '\n' + "把O.M.G打成OMG" + '\n' + "把U Got Me打成You got me" + '\n' + "把Degree打成1 degree" + '\n' + "把97 YOUNG & RICH打成97 YOUNG and RICH" + '\n' + "把Over & Over打成Over and Over" + '\n' + "把Crash & Burn打成Crash and Burn"
        return wrong 




