from game import Char, Deck
import pyfiglet

def main():
    
    print(pyfiglet.figlet_format("LIAR's BARs", font="doom"))
    
    deck = Deck()
    
    print("Antes de começarmos o jogador deve escolher seu personagem!")
    char1 = Char(deck)
    char2 = Char(deck)
    
    print(f"Atenção🛑! A carta dessa rodada é: {deck.chosen_card}")
    
    is_first_turn = True
    while True:
        result1 = char1.play_cards(is_first_turn)
        if result1 == 'LIAR':
            out = char1.LIAR(char2, deck.chosen_card)
            if out == "ACUSATION_SUCCESS":
                russian_roulette = char2.gun.shoot()
                if russian_roulette == -1:
                    print(f"Jogador(a) {char1.name} MORREU 💀")
                    break #ainda so tem 2 jogadores 
        is_first_turn = False
        
        result2 = char2.play_cards(is_first_turn)
        if result2 == 'LIAR':
            out = char2.LIAR(char1, deck.chosen_card)
            if out == "ACUSATION_SUCCESS":
                russian_roulette = char1.gun.shoot()
                if russian_roulette == -1:
                    print(f"Jogador(a) {char2.name} MORREU 💀")
                    break #ainda so tem 2 jogadores

#o jogo precissa encerrar caso so tenha um jogador.
#a carta da rodada deve ser alterada sempre que alguem atirar.
#a forma como é escolhida a carta deve ser alterada.
#concertar bugs envolvendo o botao liar no primeiro turno.
#colocar espaços entre cada print.
        
if __name__ == "__main__":
    main()
