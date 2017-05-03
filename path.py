#coding=UTF-8
import os

def root_path():
	return os.path.dirname(__file__)
def excl_path():
	return os.path.join(root_path(),'excl')
def mark_path():
	return os.path.join(root_path(),'mark')