class Club:
    FRANCHISE = "OLOLO"

    def __init__(self, name) -> None:
        self.name = name

    def changeFranchiseOfThisClub(self, franchise):
        self.FRANCHISE = franchise

    @classmethod
    def setClubsFranchise(cls, franchise):
        cls.FRANCHISE = franchise


malibu = Club("Malibu")
manhattan = Club("Manhattan")
havana = Club("Havana")
cyberpunk = Club("Cyberpunk")

clubs = [malibu, manhattan, havana, cyberpunk]


def printOutClubs(clubs):
    for club in clubs:
        print(f'\t{club.name}: {club.FRANCHISE}')


# Перед продажой
print("Клубы перед продажей")
printOutClubs(clubs)

# Сделка совершена. Все Клубы переходят под франшизу IT Academy
Club.setClubsFranchise("IT Academy")
print("Клубы куплены франшизей IT Academy")
printOutClubs(clubs)

# Вы выкупаете свой любимый клуб
malibu.changeFranchiseOfThisClub("OLOLO")
print("Выкуп Malibu состоялся.")
printOutClubs(clubs)

# IT Academy Продает свои клубы MAYRAM
Club.setClubsFranchise("MAYRAM")
print("Клубы IT Academy Проданы MAYRAM")
printOutClubs(clubs)

