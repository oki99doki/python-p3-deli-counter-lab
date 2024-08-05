
import ipdb

katz_deli = []


def line(katz_deli):
    if katz_deli == []:
        print("The line is currently empty.")
    else:
        #print(f"The line is currently:")
        #[print(element) for element in katz_deli]

        #line_string = "The line is currently: "
        #for i, customer in enumerate(katz_deli, start=1):
        #    line_string += str(i) + ". " + customer + " "
        #print(line_string.strip())


        ret_str = "The line is currently:"
        for i in range(0, len(katz_deli)):
            ret_str += f' {i + 1}. {katz_deli[i]}'
        print(ret_str)

        
line(katz_deli)

# two arguments: 1. list of current line of people, 2. name of person joining
# 
def take_a_number(katz_deli, name):
    katz_deli.append(name)
    cur_pos = len(katz_deli)
    print(f"Welcome, {name}. You are number {cur_pos} in line.")

take_a_number(katz_deli,'Sebastian')
take_a_number(katz_deli,'Linda')
take_a_number(katz_deli,'Stefan')
take_a_number(katz_deli,'Oscar')
take_a_number(katz_deli,'Audrey')

line(katz_deli)


def now_serving(katz_deli):
    if len(katz_deli) == 0:
        pass
    else:
        next_customer = katz_deli.pop(0)
    if len(katz_deli):
        print(f"Currently serving {next_customer}.")
    else:
        print(f"There is nobody waiting to be served!")

now_serving(katz_deli)

line(katz_deli)


#ipdb.set_trace()

