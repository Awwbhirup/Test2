import random
shapes=["Hearts","Diamonds","Clubs","Spades"]
cards=["Joker","Ace","King","Queen","Jack","Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14,'Joker':15}


class card:
    def __init__(self,card,shape="Joker Does Not Have A Shape"):
        self.shape=shape
        self.card=card
        self.value=values[card]
    def __str__(self):
        if(self.card!="Joker"):
            return f"{self.card} of {self.shape}"
        else:
            return "Joker"


class deck:
    
    def __init__(self):
        self.deck_cards=[]
        for i in cards[1:]:
            for j in shapes:
                objct=card(i,j)
                self.deck_cards.append(objct)
        self.deck_cards.append(card(cards[0]))
        self.deck_cards.append(card(cards[0]))
        
    def shuffle(self):
        random.shuffle(self.deck_cards)
        random.shuffle(self.deck_cards)
        
    def one_card(self):
        return self.deck_cards.pop(0)
    
class player:
    
    def __init__(self,name):
        self.name_player=name
        self.players_cards=[]
    
    def give_card(self):
        return self.players_cards.pop(0)
    
    def add_cards(self,crd):
        if type(crd)==type([]):
            self.players_cards.extend(crd)
        else:
            self.players_cards.append(crd)
    
    def shuffle_cards(self):
        random.shuffle(self.players_cards)
        
    def __str__(self):
        return f"{self.name_player} has {len(self.players_cards)} cards left"
    
def main_game():
    deck_of_cards=deck()
    deck_of_cards.shuffle()
    
    name1,name2="",""
    
    while True:
        try:
            name1=input("Enter Player 1's Name :  ").strip().title()
        except:
            print("Invalid Input, Try Again")
            continue
        else:
            if(len(name1)<=0):
                print("Invalid Input, Try Again")
            else:
                break
            
    while True:
        try:
            name2=input("Enter Player 2's Name :  ").strip().title()
        except:
            print("Invalid Input, Try Again")
            continue
        else:
            if(len(name2)<=0):
                print("Invalid Input, Try Again")
            else:
                break
    
    p1=player(name1)
    p2=player(name2)
    
    for i in range(1,(len(deck_of_cards.deck_cards)+1)):
        if(i%2==1):
            p1.add_cards(deck_of_cards.deck_cards[i-1])
        else:
            p2.add_cards(deck_of_cards.deck_cards[i-1])
        
    game_continues,roundcalc=True,1
    
    while game_continues:
        war_continues=False
        
        print(f"Round {roundcalc} : ")
        print('\n')
        
        p1.shuffle_cards()
        p2.shuffle_cards()
        cards_in_hand=[]
        a=p1.give_card()
        b=p2.give_card()
        
        print(f"{p1.name_player} has drawn {str(a)}")
        print(f"{p2.name_player} has drawn {str(b)}")
        
        if(a.value>b.value):
            cards_in_hand=[a,b]
            p1.add_cards(cards_in_hand)
            print(f"{p1.name_player} receives {len(cards_in_hand)} cards")
            print('\n')
            
        elif(a.value<b.value):
            cards_in_hand=[a,b]
            p2.add_cards(cards_in_hand)
            print(f"{p2.name_player} receives {len(cards_in_hand)} cards")
            print('\n')
            
        else:
            war_continues=True
            print('\n')
            
            while war_continues:
                print("War Has Begun")
                print('\n')
                
                if len(p1.players_cards)<11:
                    print(f"{p1.name_player} does not have enough cards for War")
                    print('\n')
                    print(f"{p2.name_player} wins!!")
                    game_continues = False
                    break
                elif len(p2.players_cards)<11:
                    print(f"{p2.name_player} does not have enough cards for War")
                    print('\n')
                    print(f"{p1.name_player} wins!!")
                    game_continues = False
                    break
                else:
                    cards_in_hand=[a,b]
                    c,d=[],[]
                    for j in range(0,10):
                        c.append(p1.give_card())
                        d.append(p2.give_card())
                        
                    cards_in_hand.extend(c)
                    cards_in_hand.extend(d)
                    
                    e=p1.give_card()
                    f=p2.give_card()
                    
                    print(f"{p1.name_player} has drawn {str(e)}")
                    print(f"{p2.name_player} has drawn {str(f)}")
                    
                    cards_in_hand.extend([e,f])
                    
                    if(e.value>f.value): 
                        p1.add_cards(cards_in_hand)
                        war_continues=False
                        print(f"{p1.name_player} receives {len(cards_in_hand)} cards")
                        print('\n')
                        continue
                        
                    elif(e.value<f.value):
                        p2.add_cards(cards_in_hand)
                        war_continues=False
                        print(f"{p2.name_player} receives {len(cards_in_hand)} cards")
                        print('\n')
                        continue
                    
                    else:
                        print('\n')
                        continue
                    
        if len(p1.players_cards)==0:
            print(f"{p1.name_player} does not have any cards left")
            print('\n')
            print(f"{p2.name_player} wins!!")
            game_continues = False
            
        elif len(p2.players_cards)==0:
            print(f"{p2.name_player} does not have any cards left")
            print('\n')
            print(f"{p1.name_player} wins!!")
            game_continues = False
            
        else:
            roundcalc +=1
            continue
        
def war():
    print("  WAR - A CARD GAME  ")
    print("=====================")
    
    check=True
    
    while check:
        main_game()
        print('\n')
        print("Do you want to play again? Yes= y / No=n")
        choices=["y","n"]
        choice=""
        
        while True:
            try:
                choice=input("").strip().lower()
            except:
                print("Invalid Input, Try Again")
                continue
            else:
                if(choice not in choices):
                    print("Invalid Input, Try Again")
                else:
                    break
        if choice=="y":
            check=True
        else:
            check=False
            
    print('\n')
    print("Thanks For playing!!")
    print('\n')
    print("  Developed by- Abhirup Banik  ")
    print("-------------------------------")
        
war()      
          
       
            
                    
                    
                    
                
            
            

            
            
            
        
            
        
        
    
    
                
        
        
        
        
    
            
    
