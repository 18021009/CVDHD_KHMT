from Point import point
from Map import map
from math import isnan
import numpy as np

class station:
    def __init__(self, _point = 0, _radius_buffer = 0, _buffer_value = 0) -> None:
        self.point = _point
        self.radius_buffer = _radius_buffer
        self.bufferValue = _buffer_value
    
    def isInBuffer(self, _x, _y) -> bool:
        if(pow(self.point.x_on_matrix - _x, 2) + pow(self.point.y_on_matrix - _y, 2) <= pow(self.radius_buffer, 2)):
            return True
        else: return False

    def setBufferValue(self, _map):
        if(self.point.x_on_matrix - self.radius_buffer <= 0):
            x = 0
        else:
            x = self.point.x_on_matrix - self.radius_buffer
        list_point_in_station_buffer = []
        while(x <= _map.matrixSizeX and x <= self.point.x_on_matrix + self.radius_buffer):

            if(self.point.y_on_matrix - self.radius_buffer <= 0):
                y = 0
            else:
                y = self.point.y_on_matrix - self.radius_buffer

            while(y <= _map.matrixSizeY and y <= self.point.y_on_matrix + self.radius_buffer):
                if(self.isInBuffer(x, y)):
                    if(_map.matrix[y][x] >= 0 and not isnan(_map.matrix[y][x])):
                        _value = _map.matrix[y][x]
                        list_point_in_station_buffer.append(_value)
                y = y + 1
            x = x + 1

        _sumValue = 0
        for _value_point in list_point_in_station_buffer:
            _sumValue = _sumValue + _value_point
        if(len(list_point_in_station_buffer) > 0):
            self.bufferValue = _sumValue / len(list_point_in_station_buffer)
        else:
            self.bufferValue = np.nan
