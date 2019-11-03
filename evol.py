import math
import random

class Genotype():
    def __init__(self):
        while True:
            self.aLen = random.randint(0, 10)
            self.bLen = random.randint(0, 10)
            if self.aLen + self.bLen <= 10:
                break
        cards = [i for i in range (1, 11)]
        self.a = []
        self.b = []
        for i in range (0, self.aLen):
            card = random.choice(cards)
            cards.remove(card)
            self.a.append(card)
        for i in range (0, self.bLen):
            card = random.choice(cards)
            cards.remove(card)
            self.b.append(card)

    def loss(self, A, B):
        sumA, sumB  = 0, 0
        for card in self.a:
            sumA += card
        for card in self.b:
            sumB += card
        return math.sqrt((A-sumA)**2 + (B-sumB)**2)

    def mutate (self):
        pass

    def crossover(self):
        pass



class Environment():
    def __init__(self, noGenotypes, A, B):
        self.noGenotypes = noGenotypes
        self.A, self.B = A, B
        self.population = [Genotype() for i in range(noGenotypes)]

    def loss(self):
        loss = 0
        for genotype in self.population:
            loss += genotype.loss(self.A, self.B)
        return loss

    def sort(self):
        self.population.sort(key=lambda x: x.loss(self.A, self.B), reverse=False)

    def mutate (self):
        pass

    def crossover(self):
        pass

    def selection(self):
        pass

    def print(self):
        print("TOTAL GENERATION LOSS: " + str(self.loss()))
        for genotype in self.population:
            print("LOSS: " + str(genotype.loss(self.A, self.B)))
            print (genotype.a)
            print (genotype.b)
            print ("   ")

if __name__ == '__main__':
    epochs = 50
    env = Environment(2, 10, 30)
    env.sort()
    env.print()
