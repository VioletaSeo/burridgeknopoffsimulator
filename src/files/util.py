import glob
import os
import sys

from files.data import Data

def read_data(file_name):
    with open(file_name, 'rb') as file:
        data, index =  Data.from_byte_array(bytearray(file.read()))
        return data

def write_data(file_name, data):
    with open(file_name, 'wb') as file:
        file.write(data.to_byte_array())

def get_file_name():
    if len(sys.argv) == 1:
        files = glob.iglob('data/*')
        return max(files, key=os.path.getctime)
    elif len(sys.argv) == 2:
        return os.path.join('data', sys.argv[1])
    else:
        raise TypeError('Usage: [filename]')

def data_desc(data):
        return ('rows: {}\n' +
               'cols: {}\n' +
               'm:    {}\n' +
               'v:    {}\n' +
               'l:    {}\n' +
               'k_b:  {}\n' +
               'k_p:  {}\n' +
               'u_s:  {}\n' +
               'u_k:  {}\n' +
               'dt:   {}').format(data.rows.get(), data.cols.get(), data.mass.get(),
                               data.plate_velocity.get(),
                               data.spring_length.get(),
                               data.spring_constant.get(), data.plate_spring_constant.get(),
                               data.static_friction.get(), data.kinetic_friction.get(),
                               data.time_interval.get())
def scaled_data_desc(data):
        return ('rows: {}\n' +
                'cols: {}\n' +
                'L:    {}\n' +
                'v:    {}\n' +
                'a:    {}\n' +
                'l:    {}\n' +
                'dt:   {}').format(data.rows.get(), data.cols.get(),
                                   data.spring_length.get(),
                                   data.plate_velocity.get(),
                                   data.alpha.get(),
                                   data.l.get(),
                                   data.time_interval.get())