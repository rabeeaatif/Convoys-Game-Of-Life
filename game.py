import time
from tkinter import *
import random

var = 32

class ChainedSet():
    
    def __init__(self, state):
        self._initialize()
        for i in state:
            self.add(i)
#             print("loops", self.table)
        
    def _initialize(self):
        self.initial_len = 1
        self.table = [[] for _ in range((1<<self.initial_len))]
        self.z = random.randrange(1<<var) | 1
        self.n = 0

            
    def clear(self):
        self.initial_len = 1
        self.table = [[] for _ in range((1<<self.initial_len))]
        self.n = 0
        

    
    def _resize(self):
        self.initial_len = 1
        while (1 << self.initial_len) <= self.n:
            self.initial_len += 1
            self.n = 0
            temp = self.table
            self.table = [[] for _ in range((1<<self.initial_len))]
        for i in range(len(temp)):
            for x in temp[i]:
                self.add(x)
                
    
    def _hash(self, x):
        return ((self.z * hash(x)) % (1<<var)) >> (var-self.initial_len)
    
    def add(self, x):
        if self.find(x) is not None:
            return False
        
        if self.n+1 > len(self.table):
            self._resize()
        
            
        self.table[self._hash(x)].append(x)
#         print("resize", self.table)
        self.n += 1
        return True
    
    def discard(self, x):
        v = self.table[self._hash(x)]
        for y in v:
            if y == x:
                v.remove(y)
                self.n -= 1
                if 3*self.n < len(self.table):
                    self._resize() 
                return y
        return None 
        
    def find(self, x):
        for y in self.table[self._hash(x)]:
            if y == x:
                return y
        return None
    
    def __iter__(self):
        for y in self.table:
            for x in y:
                yield x
    
    def returntable(self):
        return self.table
# def main():
# glider = [(20, 40), (21, 40), (22, 40),
#               (22, 41), (21, 42)]


# c = ChainedSet(glider)
# 
# print(c.returntable())
    
#--------------------------------------------------------------------
"""A Set implementation that uses hashing with chaining"""
import random



var = 32

class ChainedDict:
    
    def __init__(self):
        self._initialize()
        
    def _initialize(self):
        self.initial_len = 1
        self.table = [[] for _ in range((1<<self.initial_len))]
        self.z = random.randrange(1<<var) | 1
        self.n = 0
        
    def clear(self):
        self.table = []
        
    def get(self,coord,i):
#         print("entered")
#         index = self.find(coord)
#         if index == None:
#             print("index",index)
#             return 0
#             self.add(coord)
#             print(index)
#         index = self.find(coord)
        for x in self.table[self._hash(coord)]:
            if x[0] == coord:
                return x[1]
        return i
#                 print("nbr", x[1])
#         return index
            
    def items(self):
        item_array =[]
        for x in self.table:
            for y in x:
                item_array.append(y)
        return item_array
            
    def clear(self):
        self.initial_len = 1
        self.table = [[] for _ in range((1<<self.initial_len))]
        self.n = 0
        
    def _alloc_table(self, s):
        return [[] for _ in range(s)]
    
    def _resize(self):
        self.initial_len = 1
        while (1 << self.initial_len) <= self.n:
            self.initial_len += 1
            self.n = 0
            temp = self.table
            self.table = [[] for _ in range((1<<self.initial_len))]
        for i in range(len(temp)):
            for x in temp[i]:
                self.add(x)
                
    
    def _hash(self, x):
        return ((self.z * hash(x)) % (1<<var)) >> (var-self.initial_len)
    
    def add(self, x):
        if self.find(x) is not None: return False
        
        if self.n+1 > len(self.table):
            self._resize()
        
            
        self.table[self._hash(x)].append((x,0))
        print("resize", self.table)
        self.n += 1
        return True
    
    def discard(self, x):
        v = self.table[self._hash(x)]
        for y in v:
            if y == x:
                v.remove(y)
                self.n -= 1
                if 3*self.n < len(self.table):
                    self._resize() 
                return y
        return None 
        
    def find(self, x):
        print("cord to find",x)
        for y in self.table[self._hash(x)]:
            if y[0] == x:
#                 print("y", y)

                return self._hash(x)

        return None
        
    
    def __iter__(self):
        for y in self.table:
            for x in y:
                yield x
    
    def returntable(self):
        return self.table
    
    def __setitem__(self,k, v):
        h = self._hash(k)
        l = len(self.table[h])
        for x in range(l):
                if self.table[h][x][0] == k:
                               self.table[h][x] = (k,v)
        self.table[h].append((k,v))

    

class Config:
    """Config class.

    Contains game configurations .
    """

    # Some starting configurations.
    glider = [(20, 40), (21, 40), (22, 40),
              (22, 41), (21, 42)]  # simple glider
    dense = [(21, 40), (21, 41), (21, 42), (22, 41),
             (20, 42)]  # explodes into a dense network
    oscillator = [(1, 4), (2, 4), (3, 4)]  # oscillator
    block = [(4, 4), (5, 4),
             (4, 5), (5, 5)]  # Block

    def __init__(self) -> None:
        """Provides a default configuration.

        Args:
        - self: automatic object reference.

        Returns:
        none
        """
        # ===== Life parameters
        self.start = Config.glider  # starting shape
        self.rounds = 5000  # number of rounds of the game

        # ===== Animation parameters
        self.animate: bool = False  # switch animation on or off
        # Screen dimensions
        self.width: int = 800
        self.height: int = 800
        # HU colors
        self.bg_color = '#e6d19a'
        self.cell_color = '#580f55'
        # Cell size. Cells are drawn at resolution CELL_SIZE x CELL_SIZE pixels.
        self.cell_size: int = 10
        # Animation speed. Positive integers, bigger is faster animation.
        self.speed: int = 1


class Life:
    """

    Life class.
    The state of the game.
    
    """

    def __init__(self, state: [(int, int)], chain: bool = True) -> None:
        """Initializes game state and internal variables.

        Args:
        - self: automatic object reference.
        - state: initial congifuration - (x,y) coordinates of live cells
        - chain: controls whether to use chaining (True) or linear probiing (False)

        Returns:
        none
        """
        # USet implementations.
        self._alive = None  # intial config: (x, y) coordinates of alive cells.
        self._nbr_count = None  # stores count of live neighbors for cells.

        if chain:
            self._alive: ChainedSet = ChainedSet(state)
            self._nbr_count: ChainedDict = ChainedDict()
        else:
            self._alive: LinearSet = LinearSet(state)
            self._nbr_count: LinearDict = LinearDict()

    def step(self) -> None:
        """One iteration of the game.

        Applies game rules on current live cells in order to compute the next state of the game.

        Args:
        - self: automatic object reference.

        Returns:
        none
        """
        # Compute neighbors of current live cells.
        deltas = [(-1, -1), (0, -1), (1, -1),
                  (-1,  0),          (1,  0),
                  (-1,  1), (0,  1), (1,  1)]
        neighbors = [(x+dx, y+dy) for x, y in self._alive
                     for dx, dy in deltas]
        # Collect the number of times each coordinate appears as a
        # neighbor. That provides a count of the number of live neighbors of
        # these cells.
        for coord in neighbors:
            self._nbr_count[coord] = self._nbr_count.get(coord, 0) + 1
        # Apply rules based on numberof neighbors.
        for coord, count in self._nbr_count.items():
            # Alive cells with too few or too many alive neighbors die.
            if count == 1 or count > 3:
                self._alive.discard(coord)
            # Cells with 3 alive neighbors come alive.
            elif count == 3:
                self._alive.add(coord)
            # All other live cells survive.
        # Clear for next iteration.
        self._nbr_count.clear()

    def state(self) -> [(int, int)]:
        """Returns the current state of the game.

        Args:
        - self: automatic object reference.

        Returns:
        Coordinates of live cells .
        """
        # self._alive must be iterable, https://stackoverflow.com/a/37639615/1382487
        return list(self._alive)


class Game:
    def run(life, config) -> None:
        """Runs the game as per config.

        Args:
        - life: the instance to run.
        - config: contains game configurations.

        Returns:
        nothing.
        """
        # Set up animation if required.
        if config.animate:
            # Use tkinter. Set up the rendering window.
            tk = Tk()
            canvas = Canvas(tk, width=config.width, height=config.height)
            tk.title("Game of Life")
            canvas.configure(background=config.bg_color)
            # Indicate that rendering will be in cells.
            canvas.pack()
            # Number of rendered cells in each direction.
            cells_x = config.width // config.cell_size
            cells_y = config.height // config.cell_size

        # Make the required number of iterations.
        for i in range(config.rounds):
            # Animate if specified.
            if config.animate:
                # Clear canvas and add cells as per current state.
                canvas.delete('all')
                for x, y in life.state():
                    # Wrap cell around screen boundaries. Comment for no wrap.
                    x %= cells_x
                    y %= cells_y
                    # Add cell to canvas.
                    x1, y1 = x * config.cell_size, y * config.cell_size
                    x2, y2 = x1 + config.cell_size, y1 + config.cell_size
                    canvas.create_rectangle(
                        x1, y1, x2, y2, fill=config.cell_color)
                # Render cells, pause for next iteration.
                tk.update()
                time.sleep(0.1 / config.speed)
            # Advanmce the game by one step.
            life.step()






    
def main():
    config = Config()
    config.animate = True
    config.rounds = 1000
    config.start = Config.glider
    config.speed = 5
    life = Life(config.start)
    Game.run(life, config)


if __name__ == '__main__':
    main()
    
