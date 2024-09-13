class Coffee:
    def __init__(self, name, ing1, ing2, ing3):
        self.name = name
        self.ing1 = ing1
        self.ing2 = ing2
        self.ing3 = ing3

    def ingredients(self):
        return f'В кофе {self.name} есть следующие ингредиенты: {self.ing1}, {self.ing2}, {self.ing3}\n'

    def __str__(self):
        return f'В кофе {self.name} есть следующие ингредиенты: {self.ing1}, {self.ing2}, {self.ing3}\n'


late = Coffee('Late', 'milk', 'coffee', 'milk foam')
cappuccino = Coffee('Cappuccino', 'coffe', 'water', 'coffe')
glace = Coffee('Glace', 'coffe', 'milk', 'ice-cream')
# late.ingredients()
# cappuccino.ingredients()
# glace.ingredients()
print(late, cappuccino, glace)
