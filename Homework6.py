my_dict = {"Наташа": 1982, "Анжела": 1996, "Юля": 2017, "Кристина": 2005}
print(my_dict)
print(my_dict["Юля"])
print(my_dict.get("Настя"))
my_dict.update({"Света": 2008, "Коля": 1997})
my_dict.pop("Кристина")
print(my_dict)
my_set = {1, 6, 8, 1, 1, 8, 'top', 2.0}
print(my_set)
my_set.update({5, 50})
my_set.discard(50)
print(my_set)
