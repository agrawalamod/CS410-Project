import csv
def read_file(filename):
	with open(filename) as f:
		 content = f.readlines()
	return content

subs = read_file("subtitles.vtt")
#for index, line in enumerate(subs):
	#print index, line
# m,.l;io x0/=`	21	 print subs
print "-----------------------"
time_index = {}

flag = 0
for line in subs:
	line = line.strip('\n')
	if('-->' in line):
		if(flag==0):
			#start recording
			flag = 1
			timestamps = line.split('-->')
			timestamps[0]=timestamps[0].strip(' ').replace(' ','')
			timestamps[1]=timestamps[1].strip('\n').replace(' ','')
			content = ""
		elif(flag==1):
			#end recording, start new
			time_index[(timestamps[0],timestamps[1])] = str(content)
			#print time_index[(timestamps[0],timestamps[1])]
			timestamps = line.split('-->')
			timestamps[0]=timestamps[0].strip(' ').replace(' ','')
			timestamps[1]=timestamps[1].strip('\n').replace(' ','')
			content = ""
		else:
			print "something went very wrong"
	else:
		if(flag==1):
			#add to record
			print line
			if(line != "[SOUND]" and not line.isdigit() and line != ''):
				content = content + ' ' + line.replace('\n','').replace('"', '')
			else:
				print line, "useless"
		else:
			#ignore the fuck out
			print line, "ignored"	


print "---------------"
print time_index

with open("time_index.csv", "w") as csv_file:
		  writer = csv.writer(csv_file, delimiter=',')
		  index = 1
		  for key in time_index.keys():
		  	line = [index, key[0], key[1], time_index[key]]
			writer.writerow(line)
			index = index + 1




