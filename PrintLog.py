# Standard Library modules
from email.policy import default
import os
import time
from pyclbr import Class
import sys
import contextlib
import platform
import socket
import datetime
import logging
from collections import UserList

# 3rd-Party modules
# import cpuinfo
# import pyuac
# import psutil
# import numpy as np
# # import Pytest

# # local modules (in-house modules)
# import pathsetup
# # import dependancies

# memory=psutil.virtual_memory()

# def memory_gb(memory_bytes):
#     x=memory_bytes/(1024**3)
#     x=int(np.round(x))
#     return(x)

# The code aboveakes the total system memnory, in bytes and recalculates int to Gigabytes.
# system_memory=memory_gb(memory.total)


# Change the current working directory
os.chdir('C:\git_repo\My Test Project\My Test Project\OutputLogs')

path = ('C:\git_repo\My Test Project\My Test Project\OutputLogs')

def timeStamped(fname, fmt='%Y-%m-%d_%H.%M.%S. - {fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

today = datetime.datetime.now()
date_time = today.strftime("%H:%M:%S, on %d/%m/%Y")

#Records Current date & time and appends it to the file name of the txt log created at the end of this script.

# Standard Logging Levels
# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

#adds in an aditiional logging level between debug and info 
from functools import partial, partialmethod
logging.TITLE = 11
logging.addLevelName(logging.TITLE, "TITLE")
logging.Logger.title = partialmethod(logging.Logger.log, logging.TITLE)
logging.title = partial(logging.log, logging.TITLE)

logging.SUCCESS = 12
logging.addLevelName(logging.SUCCESS, "SUCCESS")
logging.Logger.success = partialmethod(logging.Logger.log, logging.SUCCESS)
logging.success = partial(logging.log, logging.SUCCESS)


stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler(timeStamped ('Test Log.txt'))

PrintLog = logging.getLogger(__name__)
PrintLog.setLevel(logging.DEBUG)
PrintLog.addHandler(stream_handler)
PrintLog.addHandler(file_handler)

logList = []

class FileFormatter(logging.Formatter):
    

    # Custom formatters for the differnt levels of logging.
    debug_fmt  = "%(levelname)s: %(asctime)s: %(module)s: Line %(lineno)s:\n %(message)s"
    info_fmt = "%(message)s"
    success_fmt = "%(module)s: %(message)s %(asctime)s"
    error_fmt = "%(levelname)s: %(asctime)s: %(module)s: Line %(lineno)s: \n %(message)s"
    critical_fmt = "%(levelname)s: %(asctime)s: %(module)s: Line %(lineno)s: \n CRITICAL ERROR!! - %(message)s"
       
    def __init__(self):
        super().__init__(fmt="%(levelno)d: %(module)s: %(msg)s", datefmt='%H.%M_%d-%m-%Y', style='%')  
    
    def format(self, record):

        # Save the original format configured by the user
        # when the logger formatter was instantiated
        format_orig = self._style._fmt

        # Replace the original format with one customized by logging level
        if record.levelno == logging.DEBUG:
            self._style._fmt = FileFormatter.debug_fmt

        elif record.levelno == logging.INFO:
            self._style._fmt = FileFormatter.info_fmt
            
        elif record.levelno == logging.TITLE:
            self._style._fmt = FileFormatter.debug_fmt
            
        elif record.levelno == logging.SUCCESS:
            self._style._fmt = FileFormatter.success_fmt    

        elif record.levelno == logging.ERROR:
            self._style._fmt = FileFormatter.error_fmt
            
        elif record.levelno == logging.CRITICAL:
            self._style._fmt = FileFormatter.critical_fmt
            
        # Call the original formatter class to do the grunt work
        result = logging.Formatter.format(self, record)
        
        # Restore the original format configured by the user
        self._style._fmt = format_orig

        return result


class ConsoleFormat(logging.Formatter):
    bold_red = "\x1b[31;1m"
    red = "\x1b[31;20m"
    green = "\x1b[32;20m"
    yellow = "\x1b[33;20m"
    blue = "\x1b[34;20m"
    magenta = "\x1b[35;20m"
    cyan = "\x1b[36;20m"
    reset = "\x1b[0m"

    # Custom formatters for the differnt levels of logging.
    debug_fmt  = "%(module)s: %(message)s"
    info_fmt = "%(message)s"
    title_fmt = cyan + "%(module)s: %(message)s: %(asctime)s" + reset
    success_fmt = green + "%(module)s: %(message)s %(asctime)s" + reset
    error_fmt = yellow + "ERROR! - %(asctime)s: %(module)s: Line %(lineno)s:\n %(message)s \n" + reset
    critical_fmt = red + "CRITICAL ERROR!! \n %(asctime)s: %(module)s: Line %(lineno)s: \n %(message)s" + reset
       
    def __init__(self):
        super().__init__(fmt="%(levelno)d: %(module)s: %(msg)s", datefmt='%H.%M_%d-%m-%Y', style='%')  
    
    def format(self, record):

        # Save the original format configured by the user
        # when the logger formatter was instantiated
        format_orig = self._style._fmt

        # Replace the original format with one customized by logging level
        if record.levelno == logging.DEBUG:
            self._style._fmt = ConsoleFormat.debug_fmt

        elif record.levelno == logging.INFO:
            self._style._fmt = ConsoleFormat.info_fmt
        
        elif record.levelno == logging.TITLE:
            self._style._fmt = ConsoleFormat.title_fmt
            
        elif record.levelno == logging.SUCCESS:
            self._style._fmt = ConsoleFormat.success_fmt

        elif record.levelno == logging.ERROR:
            self._style._fmt = ConsoleFormat.error_fmt
            
        elif record.levelno == logging.CRITICAL:
            self._style._fmt = ConsoleFormat.critical_fmt
            
        # Call the original formatter class to do the grunt work
        result = logging.Formatter.format(self, record)
        
        # Restore the original format configured by the user
        self._style._fmt = format_orig

        return result

PrintLog.propagate = False

fmt = FileFormatter()
file_handler.setFormatter(fmt)   

stream = ConsoleFormat()
stream_handler.setFormatter(stream)


class testfail(logging.Formatter):
           
      def __init__(self): 
          PrintLog.error ("Test Failed!")
      
          

class testsucess(logging.Formatter):
      def __init__(self):          
          PrintLog.success ("Test succeeded at")
          PrintLog.info('\n')
      
            

# today = datetime.datetime.now()
# date_time = today.strftime("%H:%M:%S, on %d/%m/%Y")   


class SysInfo():
    def __init__(self,iterable):
        PrintLog.info('Operating System:')
        PrintLog.info([platform.system()])
        PrintLog.info('Release Name / Number:')
        PrintLog.info([platform.release()])
        PrintLog.info('Version Number:')
        PrintLog.info([platform.version()])  
        PrintLog.info('\n')
        PrintLog.info('Machine ID:')
        PrintLog.info([socket.gethostname()])
        PrintLog.info('Processor:')
        # PrintLog.info([platform.processor()])
        # PrintLog.info([cpuinfo.get_cpu_info()['brand_raw']])
        # PrintLog.info('System Memory:')
        # PrintLog.info([(str(system_memory)) + 'GB'])
        PrintLog.info('\n')
        PrintLog.info('User:')
        PrintLog.info([os.path.expanduser('~')])
        PrintLog.info('\n')
        

    #Adds start time and OS information at the start of the log file.

class StartLog():
    def __init__(self, iterable):
        PrintLog.info('START OF LOG')
        PrintLog.debug('Operation commenced at ' )
        PrintLog.info('\n')
        SysInfo('current system')
 
        
class ListFormatter(UserList):
    def __init__(self, iterable):
        super().__init__(str(item) for item in iterable)

    def __setitem__(self, index, item):
        self.data[index] = str(item),'\n'

    def insert(self, index, item):
        self.data.insert(index, str(item),'\n')

    def append(self, item):
        self.data.append(str(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(str(item) for item in other)    
        

class ConcludeLogging():
    def __init__(self):
        today = datetime.datetime.now()
        date_time = today.strftime("%H:%M:%S, on %d/%m/%Y")
        PrintLog.info('\n------------------\n')    
        PrintLog.info('Testing Concluded at ' + date_time +'.')
        PrintLog.info('\nEND OF LOG')
        time.sleep(0.5)
        RemoveOrphans('Deletes 0KB duplicate logs')
    
#Removes any 0KB logs in the Output Logs folder, exculing any created by (and therfore "in use" the current instance of Python).
   
class RemoveOrphans():
    def __init__(self, iterable):
        for root, dirs, files in os.walk(path): 
            for file in files: 
                file_path = os.path.join(root, file) 
                with contextlib.suppress(PermissionError):
                    if os.path.getsize(file_path) == 0: 
                        os.remove(file_path) 
               
 