#class - 객체

class unit:
    def __init__(self, name, hp, damage): #class 생성자
        self.name = name #멤버 변수
        self.hp = hp
        self.damage = damage
        self.hello = damage + 1
        print("{0} unit create".format(self.name))
        print("{0} hp and {1} damage".format(self.hp, self.damage))

class attackunit:
    def __init__(self, name, hp, damage): #class 생성자
        self.name = name #멤버 변수
        self.hp = hp
        self.damage = damage

    def attack(self, location): #class method 앞에는 self를 항상 사용한다고 생각하면 됨
        print("{0} : {1} 방향으로 공격, (공격력 {2})".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("die")

#class instance 생성
marine1 = unit("marine", 40, 5)
marine2 = unit("marine", 40, 5)
tank = unit("tank", 150, 35)

print(tank.hello) #인스턴스 값 접근

tank.clocking = True #객체에 없어도, 외부에서 값 추가 가능(확장 가능)
print(tank.clocking)

