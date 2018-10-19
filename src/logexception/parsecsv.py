# from src.logexception.exceptionhandler import CustomUserException
# Error & Exception handling
from src.logexception.exceptionhandler import *
import logging.config
import yaml

with open('logging.yml', 'r') as stream:
    config = yaml.load(stream)
logging.config.dictConfig(config)
logger_S = logging.getLogger("S_module")

def parse_csv_and_get_columns(filename):
    count = 0
    csvFile = open(filename, 'r')
    lines = csvFile.readlines()
    logger_S.error("Logging the error!")
    for line in lines:
        val = line.split(",")
        # try:
        #     test_str_div = val[0] / val[11]
        #     print(test_str_div)
        # except TypeError:
        #     raise Typecastcheck

        try:
           test_zero_div =  (int(val[0]) / int(val[11]))
        except ZeroDivisionError:
            raise ZeroException

if __name__ == "__main__":
    parse_csv_and_get_columns(filename="dataS.csv")
