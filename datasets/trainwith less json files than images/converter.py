import glob 
import cv2

lst = glob.glob("./img/*")
# lst2 = glob.glob("./ann/*.json")
# for i in range(len(lst1)):
# 	lst1[i] = lst1[i][6:len(lst1[i])-4]
# for i in range(len(lst2)):
# 	lst2[i] = lst2[i][6:len(lst2[i])-5]
# lst1.sort()
# lst2.sort()
# for i in range(len(lst1)):
# 	print(lst1[i], lst2[i])
for l in lst:
	img = cv2.imread(l)
	height, width = img.shape[0], img.shape[1]
	length = len(l)
	cutted = l[6:length-4]
	print(cutted, height, width)
	f = open("./ann/"+cutted+".json", "w")
	f.write("{\"description\":\""+cutted+"\",\"name\":\""+cutted+"\",\"region_id\":\"7\",\"stated_id\":\"2\",\"size\":")
	f.write("{\"width\":"+ str(width) +",\"height\":"+ str(height)+"},\"moderation\":")
	f.write("{\"isModerated\":1,\"moderatedBy\":\"AzimovS\"}}")
