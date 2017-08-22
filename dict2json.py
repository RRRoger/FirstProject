# -*- encoding: utf-8 -*-
import json

json_data = []

# print len(json_data)

if type(json_data) == type(''):
	data = json.loads(json_data)
else:
	data = json_data
print json.dumps(data, indent=4).decode('unicode-escape')