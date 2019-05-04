import requests


data_example = {'temp_1': 100, 'temp_2': 150}

def sendData(data):
	response = requests.post('http://10.0.0.234:5000/pi', json=data)
	if response.ok:
	    print(response.json()) #--> {'temp_1': 100, 'temp_2': 150}

if __name__ == '__main__':
    sendData(data_example)