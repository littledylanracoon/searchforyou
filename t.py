
def song(word):
    result = ""
    count = 1
    album = ['Identify', 'Flight Log: Turbulence', 'Present : YOU', 'Breath of LOVE : Last Piece', 'MAD Winter Edition', '7 for 7', '<Present : YOU> &ME Edition',
    'Got it?', 'GOT Love', 'Just right', 'MAD', 'FLIGHT LOG : DEPARTURE', 'FLIGHT LOG : ARRIVAL', 'Eyes On You', 'SPINNING TOP : BETWEEN SECURITY & INSECURITY', 'Call My Name',
    'DYE', '翻天↑覆地','Hey Yah', 'TURN UP', "I WON'T LET YOU GO", 'LOVE LOOP', 'LOVE LOOP ~Sing for U Special Edition~', 'MY SWAGGER', 'THE New Era']

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
    word = word.rstrip()
    word = word.lower()
    print('now word is ' + word)
    if word.find("identify") != -1:
        result = result + album[0] +'\n'
        for i in range(0,11):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("turbulence") != -1:
        result = result + album[1] +'\n'
        for i in range(11,24):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("present") != -1 and word.find("me") == -1:
        result = result + album[2] +'\n'
        for i in range(24,36):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("breath") != -1 or word.find("last piece") != -1:
        result = result + album[3] +'\n'
        for i in range(36,46):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("winter") != -1:
        result = result + album[4] +'\n'
        for i in range(46,55):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("7") != -1:
        result = result + album[5] +'\n'
        for i in range(55,62):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("me") != -1 and word.find("present") != -1:
        result = result + album[6] +'\n'
        for i in range(62,86):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("it") != -1:
        result = result + album[7] +'\n'
        for i in range(86,92):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("got it") != -1:
        result = result + album[8] +'\n'
        for i in range(92,97):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("just") != -1:
        result = result + album[9] +'\n'
        for i in range(97,103):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("mad") != -1:
        result = result + album[10] +'\n'
        for i in range(103,109):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("departure") != -1:
        result = result + album[11] +'\n'
        for i in range(109,117):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("arrival") != -1:
        result = result + album[12] +'\n'
        for i in range(117,125):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("eyes") != -1:
        result = result + album[13] +'\n'
        for i in range(125,131):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("spinning") != -1:
        result = result + album[14] +'\n'
        for i in range(131,137):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("name") != -1:
        result = result + album[15] +'\n'
        for i in range(137,143):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("dye") != -1:
        result = result + album[16] +'\n'
        for i in range(143,152):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("翻天") != -1:
        result = result + album[17] +'\n'
        for i in range(152,164):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("hey") != -1:
        result = result + album[18] +'\n'
        for i in range(164,170):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("turn") != -1:
        result = result + album[19] +'\n'
        for i in range(170,177):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("let") != -1:
        result = result + album[20] +'\n'
        for i in range(177,184):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("loop") != -1:
        result = result + album[21] +'\n'
        for i in range(184,192):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("sing") != -1:
        result = result + album[22] +'\n'
        for i in range(192,201):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("swagger") != -1:
        result = result + album[23] +'\n'
        for i in range(201,203):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    elif word.find("era") != -1:
        result = result + album[24] +'\n'
        for i in range(203,207):
            result = result + str(count) + '.' + song[i]+'\n'
            count += 1
    else:
        result = result + '沒有找到唷😢請再確認一次是否輸入正確！'

    return result
    

    
