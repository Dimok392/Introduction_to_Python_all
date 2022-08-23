from datetime import datetime as dt
from time import time
def check(data):
    time = dt.now().strftime('%h:%m')
    with open("7\log_file.csv",'a') as file:
        file.write('{}:value;{}\n'.format(time,data) )
    
