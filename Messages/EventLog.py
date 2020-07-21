import logging
from os import mkdir
from os.path import exists, abspath, join
from time import localtime

from String import PathString, NameString


class EventLog:
    def __init__(self):
        self.path_string = PathString()
        self.name_string = NameString()
        self.localtime = None
        self.log_path = None

    def logger(self, remove_name):
        self.localtime = localtime()
        if not exists(abspath(self.path_string.event_log_path)):
            mkdir(abspath(self.path_string.event_log_path))
        self.log_path = join(self.path_string.event_log_path, str(self.localtime.tm_year) + '-' +
                             str(self.localtime.tm_mon) + '-' + str(self.localtime.tm_mday) + '.log')

        logging.basicConfig(level=logging.INFO,
                            format=self.name_string.logger_format,
                            datefmt=self.name_string.log_date_format,
                            filename=self.log_path)

        log_msg = remove_name + ' ' + self.name_string.remove_data_success_log_msg
        logging.info(log_msg)
