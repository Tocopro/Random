import random

lotto_list = []
print("creating 100 random lottery tickets")
for i in range(100):
    lotto_list.append(random.randrange(1000000000, 9999999999))
winners = random.sample(lotto_list, 2)
print("Lucky 2 Lottery tickets are ", winners)
