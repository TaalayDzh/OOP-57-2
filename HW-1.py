class Farm:
    def __init__(self, location, square, soil):
        self.location1 = location
        self.square1 = square
        self.soil1 = soil

    def soil_fertility(self):
        print(f'{self.square1} suitable')

Issyk_Kol = Farm ('Bokonbay', 1000, 'glina')
Chui = Farm ('Arashan', 500, 'black')
print(f'{Issyk_Kol.soil1}\n{Issyk_Kol.location1}\n{Issyk_Kol.square1}')
print(f'{Chui.soil1}\n{Chui.location1}\n{Chui.square1}')
