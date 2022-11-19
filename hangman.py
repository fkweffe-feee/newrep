def hangman(word):
    ver = 1.0
    questionData = list(word)
    board = ['_']*len(questionData)
    wrong = 0;
    stage =["",
            "        G        ",
            "        A        ",
            "        M        ",
            "        E        ",
            "        O        ",
            "        V        ",
            "        E        ",
            "        R        ",
            ]
    hitData = False
    print('ハングマン改　ver'+ str(ver))
    print(len(stage))
    while(True):
        displayHint(board)
        inputc = input('単語を予想して、入る文字を一文字入力してください。')
        while inputc in questionData:
            charNum = questionData.index(inputc)
            board[charNum] = inputc
            questionData[charNum] = '$'
            hitData = True
        if hitData == False :
            wrong += 1
            print('はずれ')
            if(wrong == (len(stage)-1)):
                print("\n".join(stage))
                break
        else:
            if('_' not in board):
                break
            hitData = False
            
        print("\n".join(stage[0:(wrong+1)]))
    return hitData
def displayHint(board):
    display = ' '.join(board)
    print('ヒント')
    print(display)
    print('\n')
