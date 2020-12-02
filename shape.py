class Shape:
    def __init__(self, id, shape, top_open, side_open):
        self.shape = shape
        self.top_open = top_open
        self.side_open = side_open
        self.id = id

    def get_shape(self):
        return self.shape
    
    def is_top_open(self):
        return self.top_open
    
    def is_side_open(self):
        return self.side_open

    def get_id(self):
        return self.id