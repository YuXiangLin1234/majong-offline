# Method of Reproduction
## 執行
下載後，使用jupyternotebook執行麻將.ipynb檔即可

## youtube
https://www.youtube.com/watch?v=SGDZYBPe0HQ

## 介紹
### 規則

建立一個檔案 rules.py ，其中包含三個主要的函數 canPeng , canChi , huMain，
藉由這三個來判定主程式中操作是否可進行(未做特殊牌型的胡牌方式 — 碰碰胡等)。

### 麻將牌

建立兩個類別 Card , Card_little， 
前者用於建立麻將牌，其中包含數個函數 setFront , MoveTo ....，
setFront 用來設定牌的正反面，而呈現給玩家，
MoveTo   用於移動麻將牌位置；
而後者繼承前者並且用於場中被丟棄之牌。

### 按鈕狀態設定

建立一個函數 fun2 ，
每當任一方出牌後，進入此函數判斷是否將按鈕狀態改成 Normal，
因麻將規則的優先順序應是 胡、碰、吃 (本次專題無花牌和槓之操作)，
故進入函數後，優先判定是否胡牌並結束遊戲，若無則判定是否可碰牌
並調整碰牌按鈕狀態，若無再判定是否可吃牌並調整吃牌按鈕狀態。

### 電腦端

建立三個函數 ComputerCard , ComputerSelectCard , ComputerOut，
函數 ComputerCard 會依照條件選取該丟的牌，其中會使用函數 ComputerSelectCard 幫忙做搜尋。
函數 ComputerOut 控制電腦丟出的牌位置，並從電腦手牌中刪除此牌。

### 胡牌判定

建立一個函數 ComputeCardNum ，
傳入手牌之陣列，並呼叫 rules.py 中的類別 huMain，
藉以判定是否胡牌。

### 麻將舞台

建立一函數 BeginGame ，
設定開始位置，並將麻將牌載入(以函數 LoadCards)，再用random函式中的shuffle將載入的麻將牌打亂，並將麻將牌發給四位玩家(以函數 ResetGame)。

建立一函數 LoadCards ，
將所有麻將牌存入清單 m_aCards 。 

建立一函數 ResetGame ，
將四家的手牌淨空，並發牌給四位玩家(以函數 ShiftCards)。

建立一函數 ShiftCards ，
設定發牌數量，並設定初始發牌位置(以函數 Shift)，再整理四家牌面(以函數 sortPoker2)。

建立一函數 Shift ，
設定麻將牌位置。

建立一函數 sortPoker2 ，
按花色理牌，任一玩家進牌及出牌應通過一次此函數進行理牌的動作。

### 滑鼠點擊

建立一函數 btn_MouseDown ，
當玩家點擊麻將牌時，觸動此函數，
若是可操作麻將牌(我方手牌)，則將牌上移，並記錄此卡牌。

### 按鈕功能

建立數個函數 OnBtnGet_Click , OnBtnOut_Click ， OnBtnChi_Click , OnBtnPeng_Click，

函數 OnBtnGet_Click 用於取牌，將牌新增至手牌中，並會直接計算玩家是否胡牌。
函數 OnBtnOut_Click 判斷玩家是否選取牌，若已選取牌則將丟牌按鈕狀態調成 DISABLED，並將其牌新增和移動至場中牌堆。由於沒有完成連線，因此我們直接在此直接加三個電腦的丟牌動作。
函數 OnBtnChi_Click , OnBtnPeng_Click 分別用於吃牌與碰牌。

### 主程式

建立視窗，設定視窗大小及標題，以及建立各種按鈕。
創建各種所需的清單，並設定一些初始參數。
呼叫函數 BeginGame 並進入 mainloop 中。
