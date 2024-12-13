from datetime import datetime

created_date = '13-06-2024'
issue_date = '13-12-2024'

created_date_obj = datetime.strptime(created_date, '%d-%m-%Y')
issue_date_obj = datetime.strptime(issue_date, '%d-%m-%Y')

created_date_obj = created_date_obj.strftime('%d-%m')
issue_date_obj = issue_date_obj.strftime('%d-%m')

print(created_date_obj,issue_date_obj)