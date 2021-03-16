lst=[1,2,3,4,4,5,6]

lst_c=[i for i in lst if i%2==0]

print(lst_c)

set_1=set(lst)

set_c={i**2 for i in lst}
print(set_c)

#dict comprehension
city=['cor','pune','gurgaon']
state=['RJ','MH','HR']

z=zip(city,state)
print(z)

dict_c={city:state for city,state in zip(city,state)}
print(dict_c)
