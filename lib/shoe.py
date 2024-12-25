#!/usr/bin/env python3

class Shoe:
    def __init__ (self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = 'Old'

    @property
    def size(self):
        """The size property"""
        return self._size
    
    @size.setter
    def size (self, size):
        """Size must be an integer"""
        if isinstance(size, int):
            self._size = size
        else:
            print('size must be an integer')
    
    def cobble(self):
        """says that the shoe has been repaired"""
        self.condition = 'New'
        print('Your shoe is as good as new!')