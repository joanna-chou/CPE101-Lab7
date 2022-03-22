# Lab 7 - Nested List Functions
# 
# Name: Joanna Chou
# Instructor: S. Einakian 
# Section: 07
# Date: 2/16/2022

# 1) This function takes a list of values and groups the elements into groups of three as sublists.
def groups_of_3(lst: list) -> list:
    main_list = []
    idx = 0
    if len(lst)%3 == 0:
        lst_div = len(lst)//3
    else:
        lst_div = (len(lst)//3) + 1
    for times in range(lst_div):
        sub_list = []
        for idx in range(idx, idx+3):
            if idx < len(lst):
                sub_list.append(lst[idx])
        idx += 1
        main_list.append(sub_list)
    return main_list

#2) This function takes a nested list and returns the final value of each sublist in a list.
def final_value(lst: list) -> list:
    main_list = []
    for obj in lst:
        for idx in range(len(obj)):
            if idx == (len(obj)-1):
                main_list.append(obj[idx])
    return main_list

#3) This function takes list and creates a nested list that repeats the corresponding integer in the original list that integer number of times.
def repeat_value(lst: list) -> list:
    main_list = []
    for obj in lst:
        sub_list = []
        count = 0
        while count < int(obj):
            sub_list.append(obj)
            count += 1
        main_list.append(sub_list)
    return(main_list)