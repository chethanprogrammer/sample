name = input("enter the username")
age = int(input("enter the user age")
dic = {"name":"chethan","age:24}
lst = ["chethan",24]
print("hey there!! my name is,name,"and i am",age,"years old")
print("hey there!! my name %s and i am %d years old"%(name,age)
print("hey there!! my name %(name)s and i am %(age)d years old"%{"name":"chethan","age":24})
print("hey there!! my name is {} and i am {} years old".format(name,age))
print("hey there!! my name is {0[name]} and i am {0[age]} yeras old".format(dic))
print("hey there!! my name is {0} and i am {0} yeras old".format(dic["name"],dic["age"]))
print("hey there!! my name is {0[0]} and i am {0[1]} yeras old".format(dic))
