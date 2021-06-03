class point:
    def __init__(self, _x = 0, _y = 0, _value = 0, _x_on_matrix = 0, _y_on_matrix = 0) -> None:
        self.x = _x
        self.y = _y
        self.value = _value
        self.x_on_matrix = _x_on_matrix
        self.y_on_matrix = _y_on_matrix

    def set_position_on_matrix(self, _map):
        self.x_on_matrix = int((self.x - _map.mapInfo[0]) / _map.mapInfo[1])
        self.y_on_matrix = int((self.y - _map.mapInfo[3]) / _map.mapInfo[5])

