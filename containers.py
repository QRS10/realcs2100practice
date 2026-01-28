# nums_list: list[int] = [1, 2, 3, 4, 5]
# nums_tuple: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
# nums_set: set[int] = {1, 2, 3, 4, 5, 4, 5, 3, 2, 1}
# mydict: dict[str, int] = {'a':1, 'b':2, 'c':3, 'd':4}
# print(len(nums_list))
# for i in range(1, 11):
#     print(i)
# For terminal:
#     [str(i) for i in range(1, 11)]   Strings of nums into a list
#     [i ** 2 for i in range(1, 11) if i ** 2 > 10]   Squares into a list
#     [i // 2 for i in range(1, 11)]   Integer division into a list
#     {i // 2 for i in range(1, 11)}   Integer division into a set
# converted set = set([0, 1, 1, 2, 2, 3, 3, 4, 4, 5])
#     {n:str(n) for n in range(1, 11)}   Dict with int paired with a string
#     {str(n):(n * str(n)) for n in range(1, 11)}   
# list('howdy') == ['h', 'o', 'w', 'd', 'y']
# ''.join(['h', 'o', 'w', 'd', 'y']) == 'howdy'
# ','.join(['alice', 'bob', 'chris']) == 'alice,bob,chris'
# 'alice,bob,chris'.split(',') == ['alice', 'bob', 'chris']
# names: list[str] = ['alice', 'bob', 'chris']
# names[2] == 'chris'
# names[-1] == 'chris'   (last thing in list)
# perfect_squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# perfect_squares[4:9] == [25, 36, 49, 64, 81]
# names[0] = 'Alice' -> names = ['Alice', 'bob', 'chris']
# names.insert(0, 'zed') -> names = ['zed', 'Alice', 'bob', 'chris']
# also_names = ('alice', 'ben', 'charlie')
# type(also_names) == tuple     (returns type)
# 'Alice' in names == True
# 'alice' in names == False
# for idx,name in enumerate(names):
#     print(idx, names)                  (prints index and value)
# set_nums: set[int] = {1, 2, 3, 4, 5}
# set_nums[0] == error      (sets have no order)
# {1, 2, 3} & {2, 3, 4} == {2, 3}
# {1, 2, 3} - {2, 3, 4} == {1}
# {1, 2, 3} <= {2, 3, 4} == False
# {1, 2, 3} < {2, 3, 4} == False
# mydict['a'] == 1
# mydict['a'] = 100    (changes value with key 'a' to int 100)
# mydict['a'] = [1, 2, 3]    (chnages value with key 'a' to list [1, 2, 3])
# mydict[[1, 2, 3]] = 'weird' (error becuase input type must be immutable)
# mydict[(1, 2, 3)] = 'weird'    (adds key (1, 2, 3) paired with value 'weird')
# for k,v in mydict.items():
#     print(k, v)              (prints dictionary keys with values)