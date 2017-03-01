#!/usr/bin/python
# -*- coding:utf8 -*-
def transform(file_in,file_out):
	########################################## Total Line #######################################    
	count=0    
	myline=file_in.readline()    
	file_in.seek(0)
	#Return cursor to file's header    
	for word in myline:        
		if word==",":            
			count+=1        
		elif word=="\n":            
			count+=1
	########################################## head #######################################            
	i=0    
	temp=[]    
	while i<count:        
		if i==0:            
			minestr="\\begin{tabular}{c "        
		elif i+1==count:            
			minestr="c}"        
		else:            
			minestr="|c "        
		temp.append(minestr)        
		i+=1    
	temp=''.join(temp)    
	#print(temp,file=file_out)    
	#print("\\toprule",file=file_out)	
	print >> file_out, temp 
	print >> file_out, "\\hline"
	########################################## table #######################################    
	i=0    
	for line in file_in:        
		temp=[]        
		for word in line:            
			if word==",":                
				temp.append("&")   
			elif word=="\n":                        
				temp.append("\\\\")   
				temp=''.join(temp)                
				#print(temp,file=file_out)                
				print >> file_out, temp 
				if i==0:                    
					#print("\\midrule",file=file_out)       
					print >> file_out, "\\hline"
					i+=1            
			else:                
				temp.append(word)
					
	########################################## end #######################################             
	#print("\\bottomrule",file=file_out)    
	#print("\\end{tabular}",file=file_out)     
	print >> file_out,  "\\hline"
	print >> file_out,  "\\end{tabular}"
	file_in.close()    
	file_out.close()        
	#######################################
import os
currentpath=os.getcwd()
csvfile=[]
filenames=os.listdir(currentpath)
for names in filenames:    
	if names[-4:]==".csv" or names[-4:]==".CSV":        
		csvfile.append(names[0:-4])
		for names in csvfile:    
			file_in_name=names+".csv"    
			file_out_name=names+".tex"    
			file_in=open(file_in_name,"r")    
			file_out=open(file_out_name,"w")    
			transform(file_in,file_out)
