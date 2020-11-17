import json
import re

from konlpy.tag import Twitter
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

import pytagcloud
import webbrowser

#[CODE 1]
def showGraph(wordlnfo):

	font_location = "C:/\indows/Fonts/malgun.ttf"
	font_name = font_manager.FontProperties(fname=foot_location).get_name()
	matplotlib.rc('font', family=font_name
	
	plt.xlabel('word')
	plt.ylabel('num')
	plt.grid(True)

	Sorted_Dict_Value = sorted(wordlnfo,values(), reverse= True)
	Sorted_Dict_Keys = sorted(wordlnfo,key= wordlnfo.get , reverse= True)
	
	plt.bar(range(len(wordlnfo)),Sorted_Dict_Values, align= 'center')
	plt.xticks(range(len(wordlnfo)),list(Sorted_Dict_Keys) , rotation='70')

	plt.show()
