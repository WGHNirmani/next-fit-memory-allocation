class Bin:
    """Represents a bin (memory block) with a fixed capacity."""
    
    def __init__(self, capacity):
        """Initialize the bin with a given capacity."""
        self.capacity = capacity
        self.remaining_space = capacity
        self.items = []  # Items in this bin
    
    def can_fit(self, item_size):
        """Check if an item can fit into the current bin."""
        return self.remaining_space >= item_size
    
    def add_item(self, item_size):
        """Add an item to the bin if it fits."""
        if self.can_fit(item_size):
            self.items.append(item_size)
            self.remaining_space -= item_size
            return True
        return False
    
    def __str__(self):
        """Return a string representation of the bin and its contents."""
        return f"Bin(capacity={self.capacity}, used={self.capacity - self.remaining_space}, remaining={self.remaining_space}, items={self.items})"
