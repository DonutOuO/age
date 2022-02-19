driving = input('請問你有沒有開過車?')
age=input('請問你的年齡:')
age=int(age)
if driving =='有' :
	if age >= 18 :
		print('你通過測驗了')
	else:
		print('安餒母湯')
elif driving =='沒有' :
	if age >= 18 :
		print("還不去考R")
	else:
		print('再過幾年')
else:
	print('只能輸入 有 or 沒有')
