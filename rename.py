#!/usr/bin/env python

##########################################################################
#	CopyRight	(C)	THORNBIRD,2030	All Rights Reserved!
#
#	Module:		rename File
#
#	File:		rename.py
#
#	Author:		thornbird
#
#	Date:		2022-04-28
#
#	E-mail:		wwwthornbird@163.com
#
###########################################################################

###########################################################################
#
#	History:
#	Name		Data		Ver		Act
#--------------------------------------------------------------------------
#	thornbird	2022-04-28	v1.0		create
#
###########################################################################

import sys,os,string,re

SW_VERSION='0.1'

Src_name='1'
Dst_name='100'

ScanPath=''

# log var
debugLog = 0
debugLogLevel=(0,1,2,3)	# 0:no log; 1:op logic; 2:op; 3:verbose


def FileCheck(dirname,filename):
    if debugLog >= debugLogLevel[-1]:
        print( 'Scan Log:  '+filename)
    
    dst=filename.replace(Src_name,Dst_name)
    if debugLog >= debugLogLevel[1]:
        print( 'Rename:  '+dst)

    os.rename(filename,dst)

def ScanFile(dirname,file):
    if debugLog >= debugLogLevel[-1]:
        print( 'Scan File:\n '+dirname+file)


    fileType = re.compile(Src_name)

    if debugLog >= debugLogLevel[-1]:
        print( file)
		
    m = re.search(fileType,file)
    if m:
        path,name = os.path.split(dirname)

        if debugLog >= debugLogLevel[-1]:
            print( 'Find Dir: '+dirname)
		
        if debugLog >= debugLogLevel[1]:
            print( 'Find Match File: '+file)

			
        if debugLog >= debugLogLevel[-1]:
            print( 'INFO: open file :'+os.path.join(dirname,file))
                
        FileCheck(dirname,file)



def ScanDir(Dir):
    CamDirs=[]
    print( 'Scan DIR: '+Dir+'\n')

    #os.path.walk(Dir,ScanFile,())
    #print(os.listdir(Dir))
    with os.scandir(Dir) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                ScanFile(Dir,entry.name)


def ParseArgv():
	if len(sys.argv) > appParaNum+1:
		HelpInfo()
		sys.exit()
	else:
		for i in range(1,len(sys.argv)):
			if sys.argv[i] == '-h':
				Usage()
				sys.exit()
			elif sys.argv[i] == '-d':
				if sys.argv[i+1]:
					debug = int(sys.argv[i+1])
					if type(debug) == int:
						global debugLog
						debugLog = debug						
						print( 'Log level is: '+str(debugLog))
					else:
						print( 'cmd para ERROR: '+sys.argv[i+1]+' is not int num!!!')
				else:
					CameraOpenKPIHelp()
					sys.exit()
			elif sys.argv[i] == '-s':
				if sys.argv[i+1]:
					global Src_name
					Src_name = sys.argv[i+1]
					print( 'OutFileName is '+Src_name)
				else:
					Usage()
					sys.exit()
			elif sys.argv[i] == '-t':
				if sys.argv[i+1]:
					global Dst_name
					Dst_name = sys.argv[i+1]
					print( 'Scan dir path is '+Dst_name)
				else:
					Usage()
					sys.exit()

def Usage():
	print( 'Command Format :')
	print( '		rename [-d 1/2/3] [-s s_name] [-t d_name]  [-h]')

appParaNum = 6

if __name__ == '__main__':
        print( 'Version: '+SW_VERSION)

        ParseArgv()

        if not ScanPath.strip():
                spath = os.getcwd()
        else:
                spath = ScanPath

        ScanDir(spath)
