#if练习
#python中相同缩进被认为是同一代码块。缩进请严格按照Python的习惯写法：4个空格，不要使用Tab，更不要混合Tab和空格，否则很容易造成因为缩进引起的语法错误。
# age = 18
# if age == 20:
#     print('age=20')
#     age+=1
# elif age==18 :
#     print('age=18')
# else:
#     print(age)
# print(age)


#for循环练习
# L = [12,13,14]
# age = 12
# for age in L :
#     age=age+1
#     print(age)
# print(age)


# L = [75, 92, 59, 68]
# sum = 0.0
# for score in L:
#     sum = sum + score
# print (sum / 4)

#while循环练习
# age=18
# while  age>17:
#     age=age+1
#     if age==20:
#         break
#
# print(age)

#多重循环

# L = [1,2,3,4]
#
# for x in L :
#     for Y in L:
#        print(x+Y)
#
# C = list(range(1,101))


#冒泡排序练习
# array = [1, 2, 5, 3, 6, 8, 4]
#
# for i in range(0, len(array), 1):
#     for j in range(i + 1, len(array), 1):
#         if array[j] < array[i]:
#             array[j], array[i] =array[i], array[j] # list元素互换
#
# print(array)

#dict练习
d = {

    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
d.setdefault('ss',232) #增加元素 如存在相同key 则不更新
d.pop('ss') #根据key 删除
l=d.popitem() #去除最后一位 并返回 tuple
print(d)
print(l)

#update(c)将d升级到d里，d里有的保存，d没有但是c有的则添加到d里，如果有key d和dc1都有的则将c相应的kv覆盖到d
e = d.copy()
c = {
    'Adam': 11,
    'Lisa': 12,
    'Bart': 13,
    'cc': 233
}
d.update(c)
print(e)
print(d)

# print(d.keys())
# print(d.values())
# print(d.items())
#
# #遍历value
# for v in d.values():
#     print(v)