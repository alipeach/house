# -*- encoding: utf8 -*-
import requests
import os

class FileUtil():


	#获取
	def get_file_full_path(self,relative_path):
		current_path = os.getcwd()
		file_full_path = str(current_path) + str(relative_path)
		return file_full_path

	#判断文件是否存在
	#参数穿该目录县的相对路径
	def exists(self,file_full_path):
		return os.path.exists(file_full_path)


	#读文件
	def read(self,relative_path):

		file_full_path = self.get_file_full_path(relative_path)

		if not self.exists(file_full_path):
			print '当前文件不存在' + str(file_full_path)
			return None
		else:
			file_handler = open(file_full_path,'r')
			try:
				return file_handler.read()
				pass
			except Exception, e:
				print '读文件异常' + str(file_full_path)
				return None
			finally:
				file_handler.close()
				pass

	#覆盖写文件
	def over_write(self,relative_path,text):
		file_full_path = self.get_file_full_path(relative_path)

		if self.exists(file_full_path):
			print '当前文件已存在,覆盖'
		else:
			print '当前文件不存在,新建'

		file_handler = open(file_full_path,'w+')
		try:
			file_handler.write(str(text))
			return True
			pass
		except Exception, e:
			print '写文件异常'
			raise e
			return False
		finally:
			file_handler.close()
			pass
		return True

	#覆盖写文件
	def append_write(self,relative_path,text):
		file_full_path = self.get_file_full_path(relative_path)

		if self.exists(file_full_path):
			print '当前文件已存在,覆盖'
		else:
			print '当前文件不存在,新建'

		file_handler = open(file_full_path,'a')
		try:
			file_handler.write(str(text))
			return True
			pass
		except Exception, e:
			print '写文件异常'
			raise e
			return False
		finally:
			file_handler.close()
			pass
		return True

