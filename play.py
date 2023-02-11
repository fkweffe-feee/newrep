import hangman
import csv

tempdata = list()
with open('save.dat','r',encoding='utf-8')as file:
    reader = csv.reader(file,delimiter=',')
    for row in reader :
        tempdata.append(row)
print('ハングマン')
print('今までの戦績')
print('{}戦{}勝{}負'.format(tempdata[2][1],tempdata[0][1],tempdata[1][1]))

word = input('問題を入力してください。')
gamedata = hangman.hangman(word)

if gamedata == True:
    tempdata[0][1] = int(tempdata[0][1])+1
else:
    tempdata[1][1] = int(tempdata[1][1])+1
tempdata[2][1] = int(tempdata[2][1])+1
with open('save.dat','w',encoding='utf-8',newline="") as file:
    writer = csv.writer(file,delimiter=',')
    for data in tempdata:
        writer.writerow(data)
     
if gamedata==True :
    print('プレイヤーの勝ち')
else:
    print('出題者の勝ち')
    print('答えは{}'.format(word))
print('{}戦{}勝{}負'.format(tempdata[2][1],tempdata[0][1],tempdata[1][1]))
print('fake');

