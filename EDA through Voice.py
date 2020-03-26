import speech_recognition as sr
import pyaudio
import os
import matplotlib.pyplot as plt
import pandas as pd
import webbrowser
import sys
from os import walk


os.chdir('C:/Users/Akash/Desktop/Works/speech to text')
from word2number import w2n

print('Welcome!')

def myCommand():   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
    	global query 
    	query= r.recognize_google(audio, language='en-in')
    	print('Command: ' + query + '\n')
    	query= query.lower()
    	return query
    	
    except sr.UnknownValueError:
    	print('Could you please repeat')

def create_df(filename):
	global df
	global name_of_df
	print("Speak name of df where you want to store the data")
	name_of_df = myCommand()
	df= pd.read_csv(filename)
	print("DF created successfuly and stored in the dataframe-{}" .format(name_of_df))


def load():
	print("Speak name of file to load")
	name_of_file= myCommand()
	filename= name_of_file +"."+ 'csv'
	a=os.path.exists(os.getcwd()+"\\"+ filename)
	if a==True:
		create_df(filename)		
	else:
		print('File not found')
		print('Try Again')
		load()


# def show_possible_operations():
# 	pass

def describe_df():
	print(df.describe())

def plot_df():
	df.plot()

def col_names():
	print(list(df.columns.values))
# def web_search():
# 	webbrowser.open('www.stackoverflow.com'+' '+query)

def find_col_value():
	if (any(i.isdigit() for i in query) == True):
		res = [int(i) for i in query.split() if i.isdigit()]
		n_value = (res[0])
	else:
		n_value= w2n.word_to_num(query)
	return n_value

def call_head():
	n_value = find_col_value()
	print(df.head(n=n_value))
	

def call_tail():
	n_value = find_col_value()
	print(df.tail(n=n_value))

def box_plot():
	n_value = find_col_value()
	df.boxplot(column=df.columns.values[n_value])
	plt.show()


def bar_plot():
	n_value = find_col_value()
	df.plot.bar(y=df.columns.values[n_value], rot=0)
	plt.show()

def current_directory():
	print(os.getcwd())


def show_files():
	f = []
	for (dirpath, dirnames, filenames) in walk(os.getcwd()):
		f.extend(filenames)
	print(f)
	print('\n')



while True:
	query= myCommand()
	query= query.lower()
	if 'load' in query or 'load data' in query or 'load dataframe' in query or 'load dataset' in query or 'load the data' in query:
		load()

	elif 'describe' in query:
		describe_df()

	elif 'show line chart of all columns' in query or 'show line chart' in query:
		plot_df()
		plt.show()

	elif 'bye' in query or 'stop' in query:
		sys.exit()

	elif 'show null values' in query or 'sum of null values' in query:
		print(df.isna().sum())

	elif 'search web' in query:
		query = myCommand()
		print(query)
		webbrowser.open(query + " " + 'stackoverflow')

	elif 'show column names' in query:
		col_names()

	elif 'show first' in query or 'show top' in query: 
		call_head()

	elif 'show last' in query or 'show bottom' in query: 
		call_tail()
	
	elif 'show box plot of' in query or 'make box plot of' in query: 
		box_plot()

	elif 'show bar graph of' in query or 'make bar chart of' in query:
		bar_plot()

	elif 'show current directory' in query or 'show directory' in query:
		current_directory()

	elif 'show files' in query or 'show files from directory' in query:
		show_files()
