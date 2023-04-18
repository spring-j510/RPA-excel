def excel_title():
    from datetime import date
    today = str(date.today())
    year = today[:4]
    month = today[5:7]
    day = today[8:10]
    day_name = year + month + day + str("_summary")+'.xlsx'
    return day_name

