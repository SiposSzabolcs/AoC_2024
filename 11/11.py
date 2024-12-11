input = "773 79858 0 71 213357 2937 1 3998391"

input_list = input.split(" ")

input_list = [int(input) for input in input_list]

for i in range(25):
    j = 0
    while j < len(input_list):
        if input_list[j] == 0:
            input_list[j] = 1
        elif len(str(input_list[j])) % 2 == 0:
            input_str = str(input_list[j])
            length = len(input_str)
            half1 = int(input_str[:length // 2])
            half2 = int(input_str[length // 2:]) 
            input_list[j] = half1
            input_list.insert(j + 1, half2)
            j += 1
        else:
            input_list[j] = input_list[j] * 2024
        j += 1
    print(i, "Finished")
print("Final:" , input_list)
print("Length:" , len(input_list))
        
