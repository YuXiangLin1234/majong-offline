def canPeng(a,card):
    n = 0
    for i in range(0,len(a)):
        c = a[i]
        if (c.imageID == card.imageID)
            n += 1
        if n >= 2:
            return True
        print("can not peng", card.imageID)
        return False

def canChi(a,card):
    n = 0
    if card.m_nType == 4:
        return False
    for i in range(0,len(a) - 1):
        c1 = a[i]
        c2 = a[i+1]
        if (c1.m_nNum == card.m_nNum+1 and c1.n_nType == card.m_nType)


def fun2():
    MyTurn = True #
    Get_btn["state"] = NORMAL
    if (len(playersOutCard[1]) > 0):
        card = playersOutCard[1][len(playersOutCard[1]) - 1]
        if(canPeng(playersCard[0],card)):
            Peng_btn["state"] = NORMAL
        #
        if (canChi(playerCard[0],card)):
            Chi_btn["state"] = NORMAL
        if (not canChi(playersCard[0],card) and not canPeng(playersCard[0],card)) :
            Peng_btn["state"] = DISABLED
            Chi_btn["state"] = DISABLED
            #OnBtnGet_Click()
        else:
            Get_bin["state"] = NORMAL

def ComputerOut():
    global k, MyTurn
    m_aCards[k].MoveTo(90+55*13,80)
    m_aCards[k].setFront(True)
    playersCard[1].append(m_aCards[k])
    result1=ComputerCardNum(playersCard[1])
    if(result1):
        showinfo(title="遺憾",message="電腦win")
        return
    i = ComputerCard(playersCard[1])
    #i=0
    card = playersCard[1][i]
    del(playersCard[1][i])
    PlayersOutCard[1].append(card)
    #outCardOrder(playersOutCard[1])
    card.setFront(True)
    #playSound(card)
    sortPoker2(playersCard[1])
    card.x = len(playersOutCard[1]) * 25 - 25
    card.y = 10
    card.MoveTo(card.x,card.y)
    k = k +1
    MyTurn = True

def ComputeCardNum(cards):
    paiArray = [[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]]
    print("玩家手中的牌",len(cards))
    for i in range(0,14):
        card = card[i]
        if (card.imageID > 10 and card.imageID < 20):
            paiArray[0][0] += 1
            paiArray[0][card.imageID - 10] += 1
        if (card.imageID > 20 and card.imageID < 30):
            paiArray[1][0] += 1
            paiArray[1][card.imageID - 20] += 1
        if (card.imageID > 30 and card.imageID < 40):
            paiArray[2][0] += 1
            paiArray[2][card.imageID - 30] += 1
        if (card.imageID > 40 and card.imageID < 50):
            paiArray[3][0] += 1
            paiArray[3][card.imageID - 40] += 1
    print(paiArray)
    hu=huMain()
    result=hu.win(paiArray)
    return result