import random
from Person import person

human = person(name = 'Тарас', money = 0, mood = 100, health = 100)
human.change_state(
        money = random.randint(50, 100),
        mood = random.randint(-20, -10),
        health = random.randint(-10, -5)
    )


print(human)
human.change_state(
        money = 100,
        mood = -20,
        health = -5
    )

print(human)


human = person(name = 'Тарас', money = 0, mood = 100, health = 100)
print(human)


go_to_park = Action(name = 'Сходить в парк', money = 0, mood = 15, health = 3)
human.do(go_to_park)

print(human)
