
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
first_result = [len(f_s) for f_s in first_strings if len(f_s) > 5]


second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
second_result = [(f_s, s_s) for f_s in first_strings for s_s in second_strings if len(f_s) == len(s_s)]

third_result = {strings: len(strings) for strings in first_strings + second_strings if len(strings) % 2 == 0}


print(first_result)
print(second_result)
print(third_result)

