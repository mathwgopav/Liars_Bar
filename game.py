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
        self.cards = self.create_deck()#lista de objetos
        self.chosen_card = random.choice(self.cards)
    
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
    
    def chosen_another_card(self):
        self.chosen_card = random.choice(self.cards)
    
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
        self.last_played_cards = []
        
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
    
    def play_cards(self, is_firt_turn):
        #opcoes pra escolher
        choices = ["LIARRRR!!!!"]+[str(card) for card in self.hand.show_hand()]

        #validaçao
        def limit_cards_to_play(answers, current):
            if "LIARRRR!!!!" in current and len(current) > 1:
                raise ValidationError('', reason="Você só pode escolher 'LIARRRR!!!!' isoladamente!")
            elif len(current) > 3:
                raise ValidationError('', reason="Você pode escolher no máximo 3 cartas!")
            return True

        quest = [
            inquirer.Checkbox(
                'cards',
                message=f"Sua vez de jogar {self.name}!",
                choices=choices,
                validate=limit_cards_to_play
            )
        ]
        
        res = inquirer.prompt(quest)
        
        if res['cards'] == ['LIARRRR!!!!']:
            if is_firt_turn:
                print("Você não pode acusar de mentiroso na primeira rodada!")
            else:
                return "LIAR"
                
        self.last_played_cards = res['cards']
        print(f"{self.name} jogou  {len(res['cards'])} cartas")
        
        return "PLAYED"
        
    
    #Acusar de mentiroso
    def LIAR(self, accused_player, chosen_card:Deck):
        #TODOS os jogadores devem ver essa mesnsagem
        print(f"{self.name}: M E N T I R O S O . . . !")
        #tempo pra revelar as cartas do jogador anterior
        time.sleep(3)
        #as cartas sao ..............
        #faço a verificaçao se o acusador (self.char) acertou, ou seja o jogador anterior está mentindo e nao colocou a(s) carta correta(s).
        print(f"As cartas jogadas por {accused_player.name} foram: {accused_player.last_played_cards}")
        
        if all(card == chosen_card.name for card in accused_player.last_played_cards):
            print(f"{self.name} está ERRADO. Agora é hora da roleta russa!")
            return self.gun.shoot()
        else:
            print(f"{self.name} estava correto! {accused_player.name} estava mentindo!")
            return "ACUSATION_SUCCESS"
    
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
            print("Arma mirada na sua cabeça...")
            time.sleep(3)
            print("Tiro na cabeça 💀")
            self.current_bullet = self.barrel
            return -1
        else:
            print(f"{self.current_bullet} Arma mirada na cabeça...")
            time.sleep(3)
            print("Ufa... escapou dessa vez!")
            self.current_bullet += 1
            print(f"Voce tem {self.barrel - self.current_bullet} tiros restantes! ☢️")



