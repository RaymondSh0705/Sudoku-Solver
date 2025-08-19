class tile:
    cord = tuple()
    value = int
    domain = None
    counter = None
    memberOf = None
    def __init__(self, cord, value):
        """
        Creates a tile at coord(x,y) with a value
        """
        self.cord = cord
        self.value = value
        self.domain = [1,2,3,4,5,6,7,8,9]
        self.counter = 0 #Stores the current index of the domain selected
        self.memberOf = []#Keeps track of which groups the tile belongs to
    def getValue(self):
        return self.value
    def setValue(self):
        """
        Sets the value of a cord from a choice in the domain
        Increases counter to indicate that if setValue for the same tile 
        is called again, the next value in the domain is used instead.
        
        Returns false if no value can be set
        """
        try:
            self.value = self.domain[self.counter]
            self.counter+=1
        except:
            return False

    def __repr__(self): #Used for checking
        return f"-:{self.cord}, {self.value}:-"
    def __str__(self):
        return f"-:{self.cord}, {self.value}:-"
    
    def updateDomain(self):
        """
        Updates the domain of a tile to the intersection of 
        the groups the tile belongs to
        """
        self.domain = list(self.memberOf[0].getDomain() & self.memberOf[1].getDomain() & self.memberOf[2].getDomain())


class groups(list): 
    domain = set()
    def __init__(self, board, domain): #Creates a list of tiles
        super().__init__(board or [])
        self.domain = domain
    
    def updateDomain(self):
        """
        Updates the domain by removing any non-0 value
        from the tiles in it from its domain
        """
        removedDomains = set()
        counter = 1
        for tile in self:
            if tile.getValue() != 0:
                try:
                    self.domain.remove(tile.getValue())
                    removedDomains.add(tile.getValue())
                except:
                    self.domain.update(removedDomains)
                    return False
            counter +=1

    def append(self, tile): #Adds tiles to the grouping
        if hasattr(tile, "memberOf"):
            tile.memberOf.append(self)
        super().append(tile)

    def getDomain(self):
        return self.domain
