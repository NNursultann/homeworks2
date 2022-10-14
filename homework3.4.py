class Human:
    def __new__(cls,name,age,growth):
        cls.name = name
        cls.age = age
        cls.growth = growth
        return super().__new__(cls)

    def __str__(cls):
        return f'name: {cls.name}\n' \
               f'age: {cls.age}\n' \
               f'growth: {cls.growth} m\n'
dan =Human('Daniel',23,1.78)
print(dan)