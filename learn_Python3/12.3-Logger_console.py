"""
Logger Demo
"""
import logging

class myLoggerConsole():

    def testLog(self):
        #create logger object that will create a log record object from the message string. It will pass it to the handler below
        my_logger = logging.getLogger('sample_log')
        #This sets the level of the logger. THis will print all but debug
        my_logger.setLevel(logging.INFO)

        #create console handle. Using stream Handler will cause it to print to the console
        my_handler = logging.StreamHandler()
        #Set handler level
        my_handler.setLevel(logging.INFO)


        #create a formatter which will process the log record object using desired format
        my_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        # add a formatter to the console handler my_handler
        my_handler.setFormatter(my_formatter)

        # add console handler to the logger
        my_logger.addHandler(my_handler)

        # logging messages
        my_logger.debug('This is the debug message')
        my_logger.info('This is the info message')
        my_logger.warning('This is the warning message')
        my_logger.error('This is the error message')
        my_logger.critical('This is the critical message')

demo = myLoggerConsole()
demo.testLog()

"""
import logging

class LoggerDemoConsole():

    def testLog(self):
        # create logger with any name. We'll use my_logger. logging.getLogger is from our imported module
        my_logger = logging.getLogger(LoggerDemoConsole.__name__)
        my_logger.setLevel(logging.INFO)

        # create console handler and set level to info
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

        # add formatter to console handler
        consoleHandler.setFormatter(formatter)

        # add console handler to logger
        my_logger.addHandler(consoleHandler)

        # logging messages
        my_logger.debug('debug message')
        my_logger.info('info message')
        my_logger.warn('warn message')
        my_logger.error('error message')
        my_logger.critical('critical message')

demo = LoggerDemoConsole()
demo.testLog()
"""