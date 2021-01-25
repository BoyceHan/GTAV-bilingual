# -*- coding: utf-8 -*-
import os

#- (english) Configs  -#
#- (chinese) 配置参数 -#
path_language1 = './chinesesimp/'
path_language2 = './american/'
path_merged = './merged/'

#- #### (english) DO NOT MODIFY ANYTHING BELOW UNLESS YOU HAVE KNOWLEDGE OF PYTHON #### -#
#- #### (chinese)          除非您懂得PYTHON语言，否则不要修改下方的代码            #### -#

NO_NEWLINE_FILES = ['clo_mnu.gxt2']
cnt_all = 0
cnt_skip = 0

def readl(f):
	#read 4-bits little-endian
	s = f.read(4)
	return (s[0])+(s[1]<<8)+(s[2]<<16)+(s[3]<<24)
#enddef readl

def readu(f,endsign):
	#read all bits until `endsign`
	ret = b''
	now = b''
	while True:
		now = f.read(1)
		if len(now)==0 or now==endsign:
			break
		ret += now
	return ret
#enddef readu

def not_same(a,b):
	miu = str(b'\xc2\xb5',encoding='utf-8')
	
	if a==b:
		return False
	try:
		sa = str(a,encoding='utf-8')
		sb = str(b,encoding='utf-8')
		if sa==sb:
			return False
			
		sa = sa.replace(miu,' ')
		sb = sb.replace(miu,' ')
		if sa==sb:
			return False

	except:
		pass
	return True
#enddef not_same

def judge_newline_globalgxt2(chinese,english):
	# THIS FUNCTION WORKS FOR CHINESE US-ENGLISH MERGEING ONLY
	
	CHINESE_FULLSTOP_SIGN = '。'
	CHINESE_FULLSTOP_SIGN_UTF8 = bytes(CHINESE_FULLSTOP_SIGN,encoding='utf-8')
	CHINESE_COMMA = '，'
	CHINESE_COMMA_UTF8 =  bytes(CHINESE_COMMA,encoding='utf-8')
	CHINESE_QUESTION_MARK = '？'
	CHINESE_QUESTION_MARK_UTF8 = bytes(CHINESE_QUESTION_MARK,encoding='utf-8')
	CHINESE_EXCLAMATION_MARK = '！'
	CHINESE_EXCLAMATION_MARK_UTF8 = bytes(CHINESE_EXCLAMATION_MARK,encoding='utf-8')
	TARGETS = [CHINESE_FULLSTOP_SIGN_UTF8,CHINESE_COMMA_UTF8,CHINESE_QUESTION_MARK_UTF8,CHINESE_EXCLAMATION_MARK_UTF8]
	
	if path_language1.find('chinese')<0 and path_language2.find('chinese')<0:
		return b''
	if path_language2.find('chinese')>=0:
		chinese,english = english,chinese
	
	if english.find(b'~n~')>=0:
		return b'~n~'
	
	for i in TARGETS:
		if chinese.find(i)>=0:
			return b'~n~'
		
	return b''
#enddef judge_newline_globalgxt2

class GXT2:
	n_records = 0
	recordsbyid = {}
	fname = ''
	
	def __init__(self,path,fname):
		self.fname = fname
		fsize = os.path.getsize(path)
		if fsize==0:
			return
		f = open(path,'rb')
		
		
		
		# part 1
		if f.read(4)!=b'2TXG':
			raise Exception('Bad GXT2 Format 1: '+path)

		self.n_records = readl(f)
		recordsbyoff = {}
		self.recordsbyid = {}
		
		for i in range(self.n_records):
			id = f.read(4)
			offset = readl(f)
			if offset in recordsbyoff:
				raise Exception('Bad GXT2 Format 2:'+path)
			recordsbyoff[offset] = (id,b'')
		
		#part2
		if f.read(4)!=b'2TXG':
			raise Exception('Bad GXT2 Format 3'+path)
		if readl(f)!=fsize:
			raise Exception('Bad GXT2 Format 4'+path)
		nowoff = 8+8*self.n_records+8
		while True:
			s = readu(f,b'\x00')
			if len(s)==0:
				break
			if nowoff not in recordsbyoff:
				raise Exception('Bad GXT2 Format 5: '+path)
			r = recordsbyoff[nowoff]
			if r[0] in self.recordsbyid:
				raise Exception('Bad GXT2 Format 6: '+path)
			self.recordsbyid[r[0]] = s
			nowoff += len(s)+1
			
		f.close()
	#enddef __init__
	
	def append_another(self,ano):
		global cnt_all,cnt_skip,NO_NEWLINE_FILES
		for id in self.recordsbyid:
			if id in ano.recordsbyid:
				cnt_all += 1
				if not_same(self.recordsbyid[id],ano.recordsbyid[id]):
					if self.fname in NO_NEWLINE_FILES:
						self.recordsbyid[id] = self.recordsbyid[id] + ano.recordsbyid[id];
					elif self.fname=='global.gxt2':
						self.recordsbyid[id] = self.recordsbyid[id] + judge_newline_globalgxt2(self.recordsbyid[id],ano.recordsbyid[id]) + ano.recordsbyid[id];
					else:
						self.recordsbyid[id] = self.recordsbyid[id] + b'~n~' + ano.recordsbyid[id];
				else:
					cnt_skip += 1
	#enddef merge
	
	
	def save(self,path):
		offsets = {}
		output = []
		nowoff = 8+8*self.n_records+8
		ids = list(self.recordsbyid.keys())
		for id in ids:
			offsets[id] = nowoff
			nowoff += len(self.recordsbyid[id])+1
			
		f = open(path,'wb')
		#part 1
		f.write(b'2TXG')
		f.write(int(self.n_records).to_bytes(length=4,byteorder='little'))
		for id in offsets:
			f.write(id)
			f.write(int(offsets[id]).to_bytes(length=4,byteorder='little'))
		#part 2
		f.write(b'2TXG')
		f.write(int(nowoff).to_bytes(length=4,byteorder='little'))
		for id in ids:
			f.write(self.recordsbyid[id])
			f.write(b'\x00')
		f.close()
	#enddef save
	
#endclass GXT2

A = os.listdir(path_language1)
A.sort()
A2 = os.listdir(path_language2)
A2.sort()
if A!=A2:
	raise Exception('Error: Language Packages are Different.')
for fname in A:
	print(fname,end=' ')
	f1 = GXT2(path_language1+'/'+fname,fname)
	f2 = GXT2(path_language2+'/'+fname,fname)
	f1.append_another(f2)
	f1.save(path_merged+fname)
	ftest = GXT2(path_merged+fname,fname)
	print('DONE')

print('All=%d Merged=%d Skipped=%d\n'%(cnt_all,cnt_all-cnt_skip,cnt_skip))
