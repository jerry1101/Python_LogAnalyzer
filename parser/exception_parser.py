"""parse logs with exceptions"""
import datetime
from . import ParsedIncident


class ExceptionParser:
    """class to parse logs with exceptions"""
    def parse(self, file_path):
        """method to parse logs with exceptions"""
        # find timestamp
        with open(file_path) as log_file:
            self.__put_incident_into_array(log_file)
            # for line in f:
            #     print(line)
            #     if 'str' in line:
            #         break
    # when '**', detail

    # when '**', happened_at

    # when inner exception, topic

        return ParsedIncident(datetime.date.today, '', '', '')
    @staticmethod
    def __put_incident_into_array(file):
        contant_array = [None]*5
        is_fist_line = True
        session_number = 1
        for line in file:
            if is_fist_line:
                contant_array[session_number] = line.strip()
                session_number += 1
                is_fist_line = False
                break
            if line.strip().startWith('***'):
                session_number += 1
                break
            else:
                contant_array[session_number] += line

        return contant_array
