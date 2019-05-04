import requests
import os

url = 'http://10.0.0.234:5000'

json_data_example = {'This': 69, 'Is a test': 420}

def sendJsonData(json):
	response = requests.post(url+'/pi', json=json)
	if response.ok:
		print(response.json())

def sendImageData(img_url):
	image = open(img_url, 'rb')
	name_img = os.path.basename(img_url)
	files= {'image': (name_img,image,'multipart/form-data',{'Expires': '0'}) }

	response = requests.post(url+'/detect', files=files)

	if response.ok:
		print(response)

	image.close()

if __name__ == '__main__':
	# JSON example
	#sendJsonData(json_data_example)

	# Image example
	
	sendImageData('cat.jpg')
	
