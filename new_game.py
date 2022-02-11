'''
    Love letter - implementation of the game
'''

class Game:
    def __init__(self, deck, dealt_cards, players):
        self._deck = deck #array of cards in numbers, ie: [1, 1, 8] would mean Guard, Guard, Princess left in the deck
        self._players = players #guessing this is something like an array?
        self.turn = 0
        self.current_player = 0

        total_players = len(players) # probably?
        self._active = total_players> 1 and self._cards_left() > 0

    def play(self, player, move):
        if player == self.current_player:
            self.current_player += 1


        
    def players(self):
    #return the list of players
        return None
        
    def deck(self):
    #return the list of cards
        if len(self.deck) > 1:
            return self.deck[0]
        else:
            return 0
    
    def draw_card(self):
    #return card at the top of the deck (if game is running)
        return None
    
    def turn(self):
    #return the current turn number
        return self.turn
    
    def current_player(self):
    #return the player whose turn it currently is?
        return self.current_player
    
    def winner(self):
    #return the winner of the game (if there is one)
        return None
    
    def cards_left(self):
    #return the number of the cards left in the deck
        return None
    
    
    """left to add:
        event for each specific card
        function that checks if a move is valid?
        function that shuffles/resets the deck
        
       """ 