import cv2
import numpy as np
import os

def colorTran(source,target,number):
	sImg = cv2.imread('./sourceTarget/'+source)
	sImg = cv2.cvtColor(sImg, cv2.COLOR_BGR2LAB)
	tImg = cv2.imread('./sourceTarget/'+target)
	tImg = cv2.cvtColor(tImg, cv2.COLOR_BGR2LAB)

	#讀取平均值和標準差
	sMean, sStd = cv2.meanStdDev(sImg)
	tMean, tStd = cv2.meanStdDev(tImg)
	sMean = np.hstack(np.around(sMean, decimals=2))
	sStd = np.hstack(np.around(sStd, decimals=2))
	tMean = np.hstack(np.around(tMean, decimals=2))
	tStd = np.hstack(np.around(tStd, decimals=2))

	height, width, channel = sImg.shape
	for i in range (0,height): 
		for j in range (0,width): 
			for k in range (0,channel): 
				s = sImg[i,j,k] 
				s = (s - sMean[k]) * (tStd[k] / sStd[k]) + tMean[k]
				s = round(s)
				if s < 0:
					s = 0
				if s > 255:
					s = 255  
				sImg[i,j,k] = s
	sImg = cv2.cvtColor( sImg,cv2.COLOR_LAB2BGR) 
	cv2.imwrite('./result/tr'+str(number)+'.bmp',sImg)

#source images(s1-s6) and target images(t1-t6) in sourceTarget directory will be color transfered to directory result.
def main():
	print("轉換sourceTarget資料夾中的所有圖片")
	files= os.listdir('./sourceTarget')
	sources = ['s1.bmp','s2.bmp','s3.bmp','s4.bmp','s5.bmp','s6.bmp']
	targets = ['t1.bmp','t2.bmp','t3.bmp','t4.bmp','t5.bmp','t6.bmp']
	for i in range(6):
		if os.path.isfile('./sourceTarget/'+sources[i]) and os.path.isfile('./sourceTarget/'+targets[i]):
			print("轉換",sources[i],'中...')
			colorTran(sources[i],targets[i],i+1)
		else:
			print(sources[i]," doesn't exist.")

# os.system('pause')