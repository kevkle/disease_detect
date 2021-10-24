

disease_dict = {"Arterienriss": "I77.2",
                "Harnblaseninfektion": "N30.9",
                "Klaviculafraktur": "S42.00",
                "Ovarialzyste": "N83.2",
                "Schädelprellung": "S00.95",
                "Schenkelhalsfraktur": "S72.00",
                "Zungengrundkarzinom": "C01"}


def matching_codes(string):
    string_list = string.split()
    if 'des' in string_list:
        if string_list[2][-2:] == 'es':
            string_list[2] = string_list[2][:-2]
        elif string_list[2][-1:] == 's':
            string_list[2] = string_list[2][:-1]

    string_list.pop(1)
    assert len(string_list) == 2

    var = "not found"

    for word in disease_dict.keys():
        if string_list[0].lower() in word.lower() and string_list[1].lower() in word.lower():
            var = disease_dict[word]

    return var









