from saveable.composite import Composite
from saveable.saveablearray import array
from saveable.saveablefloat import SaveableDouble
from saveable.saveableint import U16
from files.timeslice import Timeslice


class ScaledData(Composite):
    VERSION = 1

    rows = U16
    cols = U16
    spring_length = SaveableDouble
    plate_velocity = SaveableDouble
    alpha = SaveableDouble
    l = SaveableDouble
    time_interval = SaveableDouble
    total_time = SaveableDouble
    times = array(SaveableDouble)
    values_list = array(Timeslice)

    def __init__(self):
        Composite.__init__(self)
        self._version = U16(ScaledData.VERSION)

    def add_slice(self, time, values):
        self.times.append(time)
        self.values_list.append(Timeslice(values))

    def to_byte_array(self):
        byte_array = self._version.to_byte_array()
        byte_array += Composite.to_byte_array(self)
        return byte_array

    def load_in_place(self, byte_array, index=0):
        index = self._version.load_in_place(byte_array, index)
        if self._version.get() != ScaledData.VERSION:
            raise TypeError("Incorrect file version: '{}'".format(self._version.get()))
        Composite.load_in_place(self, byte_array, index)
        return index