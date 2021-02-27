import random
city_list=['Newyork','chicago']
print("Select random element",random.choice(city_list))
print(random.randint(0,5))
print(random.randrange(10,50,5))
list=[44,66,77,88]
print("select a element",random.choice(list))
list1=[2,5,8,9,12]
print("random",random.sample(list,3))
list2=[2,5,6,7]
random.shuffle(list2)
print("shuffled list",list2)
