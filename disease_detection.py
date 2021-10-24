

disease_dict = {"Arterienriss": "I77.2",
                "Harnblaseninfektion": "N30.9",
                "Klaviculafraktur": "S42.00",
                "Ovarialzyste": "N83.2",
                "Schädelprellung": "S00.95",
                "Schenkelhalsfraktur": "S72.00",
                "Zungengrundkarzinom": "C01"}


string = 'Karzinom des Zungengrundes'

string_list = string.split()
if 'des' in string_list:
    if string_list[2][-2:] == 'es':
        string_list[2] = string_list[2][:-2]
    elif string_list[2][-1:] == 's':
        string_list[2] = string_list[2][:-1]

string_list.pop(1)

new_string = re.split("der | des", string)






