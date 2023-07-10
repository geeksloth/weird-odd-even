noob_code = '''
number = input("input: ")
try:
    number = int(number)
except:
    print("invalid")

if number == 0:
    print("Zero")
'''
max_run = 2899
temp_toggle = 1
for number in range(1, max_run):
    if temp_toggle == 0:
        temp_code = '''
elif number == {}:
    print("Even")'''.format(number)
        temp_toggle = 1
    else:
        temp_code = '''
elif number == {}:
    print("Odd")'''.format(number)
        temp_toggle = 0

    noob_code += temp_code

#print(noob_code)

my_file = open("noob_oddeven.py", "w")
my_file.writelines(noob_code)
my_file.close()