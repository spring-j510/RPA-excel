from openpyxl import Workbook  # 「pip install openpyxl」でインストールしておく


from datetime import date
today = str(date.today())
year = today[:4]
month = today[5:7]
day = today[8:10]
excel_title = year + month + day + str("_summary")+'.xlsx'


# ワークブックの新規作成と保存
wb = Workbook()
wb.save(excel_title)

# ワークブックの読み込み
from openpyxl import load_workbook

wb = load_workbook(excel_title)




# 変更したいシート名を指定する
old_sheet_name = 'Sheet'
new_sheet_name = 'summary'

# シート名を変更する
ws = wb[old_sheet_name]
ws.title = new_sheet_name


# ワークシートの選択
ws = wb['summary']  # ワークシートを指定
ws = wb.active  # アクティブなワークシートを選択


# セルに書き込み
ws['A1'] = 'Hello from Python'



wb.save(excel_title)  # overwrite myworkbook.xlsx


