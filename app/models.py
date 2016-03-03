# coding=utf-8

import datetime
from pytz import timezone
import pytz
from config import data

def getThoughts(month, day):
	return data[month][day]

def getDate():
	today = datetime.datetime.now(timezone('Europe/Moscow'))
	months = ("Января", "Февраля", "Марта", "Апреля", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октября", "Ноября", "Декабря")
	return str(today.day) + " " + months[today.month - 1] + " " + str(today.year), today.month, today.day	

def getImage(month, day):
	return (month * 31 + day) % 13 