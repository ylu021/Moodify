import simplejson as json 

dummyContent = '[{"test1": 5, "test2": 7}]'
parseContent = json.loads(dummyContent)
for content in parseContent:
	print content['test1']
# print parseContent[0]['test1']
# print json.dumps(obj,separators=(',',':'),sort_keys=True, indent=4 * ' ')
