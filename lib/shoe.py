#!/usr/bin/env python3

class Shoe:
    def _init_(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"  # Initialize condition as "New"

    def cobble(self):
        # Repair the shoe
        self.condition = "New"
        print("Your shoe is as good as new!")

if _name_ == "_main_":
    # You can add some code here to test the Shoe class directly if needed
    pass