from datetime import datetime
import os


class Logger():

    def __init__(self, log_dir):
        try:
            os.mkdir(log_dir)
        except Exception as e:
            print(e)
        self.log_file = open("{}/log.txt".format(log_dir), "a+")

    def log_info(self, data):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.log_file.write("[{} INFO] {}\n".format(dt_string, data))

    def log_error(self, data):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.log_file.write("[{} ERROR] {}\n".format(dt_string, data))
