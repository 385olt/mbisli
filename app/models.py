import datetime
from config import data

def getThoughts(month, day):
	return data[month][day]

def getDate():
	today = datetime.date.today()
	months = ("Января", "Февраля", "Марта", "Апреля", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октября", "Ноября", "Декабря")
	return str(today.day) + " " + months[today.month - 1] + " " + str(today.year), today.month, today.day	