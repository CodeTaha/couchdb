import requests
import json
from pprint import pprint



for index in range(1550,1561):
	print index
	json_data=open("books-json/book" + str(index) + ".json").read()
	with open('books-json/book'+str(index)+'.json') as data_file:    
    		data = json.load(data_file)
		response = requests.put("http://127.0.0.1:5984/bk/"+unicode(data['_id']), str(json_data))
	print index

