COLORS = {'RED': '#ff0000', 'GREEN': '#00ff00', 'BLUE': '#0000ff', 'YELLOW': '#ffff00',\
    'BLACK': '#000000', 'WHITE': '#ffffff', 'CYAN': '#00ffff', 'MAGENTA': '#ff00ff'}

class Peg:
    RADIUS = 10
    def __init__(self, canvas, color, xpos, ypos, callback):
        self._canvas = canvas
        self.color = color
        self.x = xpos
        self.y = ypos
        self._callback = callback
        self._id = draw_circle(canvas, xpos, ypos, Peg.RADIUS, fill=COLORS[color], tags=('peg'))
        self._canvas.tag_bind(self._id, '<B1-Motion>', self.drag)
        self._canvas.tag_bind(self._id, '<ButtonRelease-1>', self.drop)
        self._frozen = False

    def drag(self, event):
        '''Move with the mouse cursor'''
        if not self._frozen:
            self.move_to(event.x, event.y)

    def drop(self, event):
        '''Signal to callback that the peg has been dropped
        and in what position'''
        if not self._frozen:
            self._callback.place_peg(event.x, event.y, self)

    def move_to(self, x, y):
        '''Move to the absolute coordinates'''
        self._canvas.move(self._id, x - self.x, y - self.y)
        self.x = x
        self.y = y

    def remove(self):
        '''Remove the peg from the board'''
        self._canvas.delete(self._id)

    def freeze(self):
        '''Freezes the peg so it can't be moved'''
        self._frozen = True

class Grid():
    def __init__(self, canvas, xpos, ypos, rows, columns, rowheight, colwidth):
        self._canvas = canvas
        self._x = xpos
        self._y = ypos
        self._cols = columns
        self._rows = rows
        self._rh = rowheight
        self._cw = colwidth
        self._h = rows * rowheight
        self._w = columns * colwidth

    def draw(self):
        '''Draw a grid according to specs'''
        for col in range(self._cols + 1):
            x = self._x + self._cw * col
            self._canvas.create_line(x, self._y, x, self._y + self._h, width=2, fill='#444444')

        for row in range(self._rows + 1):
            y = self._y + self._rh * row
            self._canvas.create_line(self._x, y, self._x + self._w, y, width=2, fill='#444444')

    def get_field_center(self, row, col):
        '''Returns the coordinates of the center of a field'''
        center_x = self._x + (col * self._cw) + self._cw // 2
        center_y = (self._y + self._h) - ((row * self._rh) + self._rh // 2)

        return center_x, center_y

    def get_field(self, x, y):
        '''Get a field from coordinates, return None if
        outside the grid'''
        rel_x = x - self._x
        rel_y = y - self._y
        if rel_x < 0 or rel_x > self._w or rel_y < 0 or rel_y > self._h:
            return None
        col = rel_x // self._cw
        row = (self._rows - 1) - rel_y // self._rh

        return {'row': row, 'col': col}

def draw_circle(canvas, xpos, ypos, radius, **kwargs):
    '''Draw a circle centered at (xpos, ypos) with specified radius'''
    x1 = xpos - radius
    y1 = ypos - radius
    x2 = xpos + radius
    y2 = ypos + radius

    return canvas.create_oval(x1, y1, x2, y2, **kwargs)
