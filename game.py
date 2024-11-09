import random
import time
import inquirer
from inquirer.errors import ValidationError


#cartas
class Cards:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __repr__(self):
        return f"{self.name}"

class King(Cards):
    def __init__(self):
        super().__init__(name="King 👑", value="1")
class Queen(Cards):
    def __init__(self):
        super().__init__(name="Queen 👸", value="2")
class Ace(Cards):
    def __init__(self):
        super().__init__(name="Ace ❤️", value="3")

#baralho
class Deck:
    def __init__(self):
        self.cards = self.create_deck()
    
    def create_deck(self):
        king = [King() for _ in range(6)]
        queen = [Queen() for _ in range(6)]
        ace = [Ace() for _ in range(6)]
        
        deck = king + queen + ace
        random.shuffle(deck)
        return deck
    
        
    def draw_cards(self, n):
        draw_cards = self.cards[:n] 
        self.cards = self.cards[n:]
        return draw_cards
    
#Mao
class Hand:
    def __init__(self, deck: Deck):
        self.hand = deck.draw_cards(5)
        
    def show_hand(self):
        return self.hand

#personagens
class Char:
    def __init__(self, deck: Deck):
        self.name = self.__choice_char()
        self.gun = Gun()
        self.hand = Hand(deck)
        # seu baralho
        
    def __choice_char(self):
        quest = [
            inquirer.List(
                'chars',
                message="Qual personagem você quer escolher",
                choices=["Coelhinha🐰", "Touro🐂", "Porco🐷", "Rinoceronte🦏"]
            ),
        ]
        res = inquirer.prompt(quest)
        print(f"Você escolheu: {res['chars']}")
        return res['chars']
    
    def play_cards(self):
        choices = [str(card) for card in self.hand.show_hand()]

        def limit_cards_to_play(answers, current):
            if len(current) > 3:
                raise ValidationError('', reason="Você pode escolher no máximo 3 cartas!")
            return True

        quest = [
            inquirer.Checkbox(
                'cards',
                message="Sua vez de jogar! Escolha até 3 cartas:",
                choices=choices,
                validate=limit_cards_to_play
            )
        ]
        
        res = inquirer.prompt(quest)
        print(f"Você jogou as cartas: {res['cards']}")
        
    
    #Acusar de mentiroso
    def LIAR(self):
        pass

#pistola
class Gun:
    def __init__(self):
        self.barrel = 6
        self.bullet = int(random.random() * self.barrel)
        self.current_bullet = 0

    def shoot(self):
        if self.current_bullet == self.barrel:
            print("Arma só tinha uma bala e já foi desparada!")
            return
        
        if self.current_bullet == self.bullet:
            print(f"{self.current_bullet} Arma mirada na cabeça...")
            time.sleep(3)
            print("Tiro na cabeça 💀☠️")
            self.current_bullet = self.barrel
        else:
            print(f"{self.current_bullet} Arma mirada na cabeça...")
            time.sleep(3)
            print("Ufa... escapou dessa vez!")
            self.current_bullet += 1



