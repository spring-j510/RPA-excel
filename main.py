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

    input_str = input("Enterを押して続行。終了する場合は1を入力してください。")

    if input_str == "":
        print("続行します。")
    elif input_str == "1":
        print("終了します。")
        flag = 1

print(c_list)

df = pd.DataFrame(c_list, columns=['','Name', 'Mail','Mobile','Adress','reason for (ones) desire'])

print(df)

path = "xlsx/" + function.excel_title()

# データフレームをExcelファイルに変換する
df.to_excel(path, index=False)

print("Excelファイルに変換しました。")