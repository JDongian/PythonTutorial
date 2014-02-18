example_list0 = []
example_list1 = [j for j in range(50)]
example_list2 = ['abcdefghi', 66.25, 333, 333, 1, '', 1234.5]
example_list3 = [example_list0, example_list1, example_list2]
#Iterating through lists is easy.
#for example in example_list3:
#    print example[:5]
#for example in example_list1[:5]:
#    print example**6

example_tuple0 = ()
example_tuple1 = ('a',)
example_tuple2 = (j for j in range(50))
example_tuple3 = (example_list0, example_list1, example_list2)
#Iterating through tuples is nearly the same thing.
#for example in example_tuple1:
#    print example
#for example in example_tuple2:
#    print example**4

example_set0 = set()
example_set1 = set(('',))
example_set2 = set(j for j in range(50))
example_set3 = set([66.25, 333, 333, 1, 1234.5])
#Iterating through a set is easy too. Note that sets are unordered.
#for example in example_set1:
#    print example
#for example in example_set3:
#    print example**4

example_dict0 = dict()
example_dict1 = {x: x**2 for x in range(5)}
example_dict2 = dict(sape=4139, guido=4127, jack=4098)
example_dict3 = {'cow': "Moooo!",
                 'chicken': "Cluck, cluck.",
                 'horse': "neigh",
                 'snake': "Hissssss...."}
#Iterating through a dictionary is the only one that looks different.
#for v in example_dict1.values():
#    print v
#for k in example_dict2.keys():
#    print k, example_dict2[k]

# Ask what a frozenset is!
