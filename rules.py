def canPeng(a,card):
    n = 0
    for i in range(0,len(a)):
        c = a[i]
        if (c.imageID == card.imageID):
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
        if (c1.m_nNum == card.m_nNum+1 and c1.m_nType == card.m_nType and c2.m_nNum == card.m_nNum + 2 and c2.m_nType == card.m_nType):
            return True
    for i in range(0, len(a) - 1):
        c1 = a[i]
        c2 = a[i + 1]
        if (c1.m_nNum == card.m_nNum - 1 and c1.m_nType == card.m_nType and c2.m_nNum == card.m_nNum + 1 and c2.m_nType == card.m_nType):
            return True
    for i in range(0, len(a) - 1):
        c1 = a[i]
        c2 = a[i + 1]
        if (c1.m_nNum == card.m_nNum - 2 and c1.m_nType == card.m_nType and c2.m_nNum == card.m_nNum - 1 and c2.m_nType == card.m_nType):
            return True
    print('不能吃牌！！！', card.imageID)
    return False

class huMain():
    def __init__(self):
        # 定義手中的牌 int allPai[4][10]
        self.allPai = [
            [6, 1, 4, 1, 0, 0, 0, 0, 0, 0], # "餅"
            [3, 1, 1, 1, 0, 0, 0, 0, 0, 0], # "條"
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # "萬"
            [5, 2, 3, 0, 0, 0, 0, 0, 0, 0]  # "字"
        ]
        if self.Win(self.allPai):
            print('Hu！\n')
        else:
            print('Not Hu！\n')
    #  判斷是否胡牌的函數
    def Win(self, allPai):
        jiangPos = 0
        jiangExisted = False
        # 是否滿足3, 3, 3, 3, 2的模型
        for i in range(0, 4):
            yuShu = allPai[i][0] % 3 #餘數
            if yuShu == 1:
                return False #不滿足3, 3, 3, 3, 2的模型
            if yuShu == 2:
                if jiangExisted == True:
                    return False #不滿足3, 3, 3, 3, 2的模型
                jiangPos = i #"將"在哪行
                jiangExisted = True
        
        # 不含"將"處理
        for i in range(0, 4):
            if i != jiangPos:
                if not self.Analyze(allPai[i], i == 3):
                    return False
        # 該類別牌中要包含"將"，因為要對"將"進行輪詢，效率較低，放在最後
        success = False # 指出除掉"將"後是否可透過
        for j in range(1, 10): # 對列操作，用j表示
            if allPai[jiangPos][j] >= 2:
                # 除去這兩張牌
                allPai[jiangPos][j] += -2
                allPai[jiangPos][0] += -2
                if self.Analyze(allPai[jiangPos], jiangPos == 3):
                    success = True
                # 還原這兩張牌
                allPai[jiangPos][j] += 2
                allPai[jiangPos][0] += 2
                if success == True:
                    break
        return success

    # 分成"刻""順"組合
    def Analyze(self, aKindPai, ziPai): 
        if aKindPai[0] == 0:
            return True
        #尋找第一張牌
        for j in range(1, 10):
            if aKindPai[j] != 0:
                break
        if aKindPai[j] >= 3: #作為刻牌
            # 除去這三張牌
            aKindPai[j] += -3
            aKindPai[0] += -3
            result = self.Analyze(aKindPai, ziPai)
            # 還原這三張刻牌
            aKindPai[j] += 3
            aKindPai[0] += 3
            return result
        # 作為順牌
        if (not ziPai) and j < 8 and aKindPai[j+1] > 0 and aKindPai[j+2] > 0:
            # 除去這三張順牌
            aKindPai[j] += -1
            aKindPai[j+1] += -1
            aKindPai[j+2] += -1
            aKindPai[0] += -3
            result = self.Analyze(aKindPai, ziPai)
            # 還原這三張順牌
            aKindPai[j] += 1
            aKindPai[j+1] += 1
            aKindPai[j+2] += 1
            aKindPai[0] += 3
            return result
        return False