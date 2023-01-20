class SuperHero:
    people = "people"
    def hero(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def aji(self):
        return f"name: {self.name}"
    def heal(self):
        return f"health_points: {self.health_points * 2}"
    def aky(self):
        return f"nickname: {self.nickname}, super: {self.superpower}, heal: {self.health_points}"
    def git(self):
        return f"catchphrase: {len(self.catchphrase)}"        
hero = SuperHero()
print(hero.hero("hub","ji","fly","500","taza"))
print(hero.aji())
print(hero.heal())
print(hero.aky())
print(hero.git())