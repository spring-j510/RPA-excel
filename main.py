from openpyxl import Workbook
import function

input_list = []

# ４行の入力をリストに追加する
for i in range(5):
    input_list.append(input())

# 受け取ったリストを表示する
print(input_list)


"""
class MyClass():
    def __init__(self, message):
        self.value = message

myinstance = MyClass("Hello!")
print(myinstance.value)



class hr:
    def __init__(self, name,mail,mobile,motive):
        self.name = name
        self.mail = mail
        self.mobile = mobile
        self.motive = motive


myinstance = hr(1,2,3,4)
print(myinstance.name)
"""


"""
name:
mail:
mobile:
adress:
reason for (one's) desire:
"""


# # ワークブックの新規作成と保存
# wb = Workbook()
# wb.save(function.excel_title())

# # ワークブックの読み込み
# from openpyxl import load_workbook

# wb = load_workbook(function.excel_title())

# # 変更したいシート名を指定する
# old_sheet_name = 'Sheet'
# new_sheet_name = 'summary'

# # シート名を変更する
# ws = wb[old_sheet_name]
# ws.title = new_sheet_name


# # ワークシートの選択
# ws = wb['summary']  # ワークシートを指定
# ws = wb.active  # アクティブなワークシートを選択

# # セルに書き込み
# ws['B2'] = 'No.'
# ws['C2'] = 'name'
# ws['D2'] = 'Mail'
# ws['E2'] = 'Mobile'
# ws['F2'] = 'Adress'
# ws['G2'] = 'reason for (ones) desire'







# wb.save(function.excel_title())  # overwrite myworkbook.xlsx