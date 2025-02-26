class Pokemon:
    def __init__(self, name):
        self.name = name


    def walks(self):
        print("Walk..")

    # java에서는 target_pokemon은 같은 Pokemon type으로 받는 곳이므로
    # 오류가 난다.
    # python에서는 그냥 적용됨. type checking을 안해서.
    def attack(self, target_pokemon):
        print(f"{self.name}Attack {target_pokemon.name}!")


#상속받을 땐 괄호 안에 부모 클래스
class Pikachu(Pokemon):
    pass


class Agumon:
    def __init__(self, name):
        self.name = name


agumon = Agumon('아구몬')
pikachu = Pikachu('피카츄')
pikachu.attack(agumon)
