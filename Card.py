class Card(Button):
    def __init__(self,cardtype,num,bm,master):
        Button.__init__(self,master)
        # 牌的類型
        self.m_nType = cardtype
        # 牌的點數
        self.m_nNum = num
        # URL 還沒找到
        # 1 - 桶(餅) 2 - 條  3 - 萬  4 - 字牌
        if self.m_nType == 1:
            FrontURL = ""
        elif self.m_nType == 2:
            FrontURL = ""
        elif self.m_nType == 3:
            FrontURL = ""   
        elif self.m_nType == 4:
            FrontURL = ""
        self.img = bm
        self.imageID = self.m_nType * 10 + self.m_nNum
        FrontURL = FrontURL + str(self.m_nNum)
        FrontURL = FrontURL + ".png"
        self["width"] = 51
        self["height"] = 67
        self["text"] = str(self.imageID) + ".png"
        self.setFront(False)
        #self.MoveTo(100,100)
        self.bind("<ButtonPress>", btn_MouseDown)
        self.cardID = 0
    def __cmp__(self,other):
        return cmp(self.imageID, other.imageID)

#書上的是看得到別人的牌的
    def setFront(self, b):
        self.m_bFront = b
        if (b == True):
            self["image"] = self.img
        else:
            self["image"] = back

    def MoveTo(self,x1,y1):
        self.place(x = x1, y = y1)
        self.x = x1
        self.y = y1
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getImageID(self):
        return imageID

class Card_little(Card):
    def __init__(self,cardtype,num,bm,master,width, length):
        super().__init__(cardtype,num,bm,master)
        self["width"] = width
        self["height"] = length