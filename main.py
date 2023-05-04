import pandas as pd
import function

c_list = []
count = 0
flag = 0
while flag != 1:
    count += 1
    input_list = []
    for i in range(5):
        input_str = str(input())
        index_of_colon = input_str.find(":")
        input_str = input_str[index_of_colon+1:]
        input_list.append(input_str)

    input_list.insert(0, count)
    c_list.append(input_list)

    input_str = input("Press Enter to continue. To exit, enter 1.")

    if input_str == "":
        print("To be continued.")
    elif input_str == "1":
        print("Termination.")
        flag = 1

print(c_list)

df = pd.DataFrame(c_list, columns=['','Name', 'Mail','Mobile','Adress','reason for (ones) desire'])

print(df)

path = "xlsx/" + function.excel_title()

df.to_excel(path, index=False)

print("Converted to Excel file.")