class Card(object):
	def __init__(self, suit, value):
		self.suit = suit
        self.value = value
    def getCard(self):
        for suit in range(1,5):
            for value in range(1, 14):
                if self.value == 1:
                    trueValue = "Ace"

                elif self.value == 11:
                    trueValue = 'Jack'
                elif self.value == 12:
                    trueValue = Queen
                elif self.value == 13:
                    trueValue = 'King'
                else:
                    trueValue = value
        return trueValue

class Deck(object):
	def __init__(self):
		self.cards = []

        for suit in range(1,5):
            
            for value in range(1, 14):
                if value == 1:
                    trueValue = "Ace"    
                elif value == 11:
                    trueValue = 'Jack'
                elif value == 12:
                    trueValue = Queen
                elif value == 13:
                    trueValue = 'King'
                else:
                    trueValue = value
        return trueValue

	def createDack(self):

		cardsSpades = Card('spades', 'trueValue')
        cardsClubs = Card('spades', 'trueValue')
        cards = Card('spades', 'trueValue')
        cardsSpades = Card('spades', 'trueValue')
		print new_card, new_card.suit, new_card.value
		
deck1 = Deck()
deck1.createDack()

		