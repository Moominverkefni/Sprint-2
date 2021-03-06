import sqlite3
import sys

class Question:
    #Tengingar vid gagnagrunn
    conn = sqlite3.connect('muminspurningar.db')
    c = conn.cursor()
    Stig = 0
    def __init__(self):
        pass
        
    #Saekir spurningar ur gagnagrunninum
    def getQuestion(self, level):
        
        self.c.execute('SELECT count(spurning) FROM Spurningar WHERE level = :level',{'level': level})
        count =  (int)(''.join(map(str,(self.c.fetchone()))))
        self.c.execute('SELECT spurning, SpId FROM Spurningar WHERE level = :level',{'level': level})    
        return self.c.fetchmany(count)
    
    
    #Saekir svar vid vidkomandi spurningu ur gagnagrunninum
    def getAnswer(self, SpID):           
        self.c.execute('SELECT svor FROM Svor WHERE SvID = :SvID',{'SvID': SpID})
        return self.c.fetchone()
    
    #Athugar hvort leikmadur hefur unnid
    def checkScore(self):
        if(self.Stig == 5):
            print('Thu vannst leikinn!!')
            self.c.close()
            self.conn.close()
            sys.exit()
            
    #Athugar hvort leikmadur setti inn rett svar        
    def checkAnswer(self,SpID,svar):
        self.c.execute('SELECT rettSvar FROM Svor WHERE SvID = :SvID',{'SvID': SpID})

        if (svar == ''.join(map(str,(self.c.fetchone())))):
            print("Rett svar!")
            self.Stig += 1 
            self.checkScore()
            
        else:
            print("Rangt svar!")
            self.Stig = 0
              
    #Flaedi leiksins
    def playGame(self,level):
        x = self.getQuestion(level)
        
        for i in range(0,len(x)):
            print(''.join(map(str,(x[i][0]))))
            print(''.join(map(str,(self.getAnswer(x[i][1])))))
            svar = input('')
            self.checkAnswer(x[i][1], svar)
            
        while(True):
            self.playMore()
        
    #Vill leikmadur halda afram ad reyna?
    def playMore(self):
        print('Viltu halda afram?')
        svar = input('j / n: \n' )
        if(svar == 'j'):
            print('Veldu erfidleikastig, 1, 2 eda 3')
            level = input()
            self.playGame(level)
        else:
            print('Okei Bless.')
            self.c.close()
            self.conn.close()
            sys.exit()
            
            
    
    
# Main fall leiksins.
def main():
    Spurn = Question()
    print('Velkominn i spurningarleik Bisamrottunnar. \nThu tharft ad svara 5 spurningum rett i rod til ad vinna leikinn.  \nVeldu erfidleikastig fyrir spurningarnar: 1, 2 eda 3. ')
    level = input()
    Spurn.playGame(level)
    
    
if __name__  == '__main__':
    main()
    
    
    
## A dagskra:
## Setja upp Try blokkir
## Birta Skyringu a svari ef leikmadur svarar rett
## Birta mynd med spurningu?



    
