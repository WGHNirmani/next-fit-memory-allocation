from bin import Bin

class NextFitMemoryAllocator:
    """Simulates memory allocation using the Next Fit algorithm."""
    
    def __init__(self, bin_capacity):
        """Initialize the memory allocator with a given bin capacity."""
        self.bin_capacity = bin_capacity
        self.bins = [Bin(bin_capacity)]  # Start with one bin
        self.current_bin_index = 0  # The index of the active bin
    
    def allocate_memory(self, item_size):
        """Allocate memory for a new item using the Next Fit algorithm."""
        if item_size <= 0:  # Handle invalid input (zero or negative memory request)
            print(f"Invalid request size: {item_size}. Skipping this request.")
            return  # Skip negative or zero requests

        current_bin = self.bins[self.current_bin_index]
        
        if not current_bin.add_item(item_size):
            # If the item doesn't fit, create a new bin and add it there
            new_bin = Bin(self.bin_capacity)
            new_bin.add_item(item_size)
            self.bins.append(new_bin)
            self.current_bin_index += 1  # Move to the new bin
    
    def display_bins(self):
        """Display the current state of all bins."""
        for i, bin in enumerate(self.bins):
            print(f"Bin {i + 1}: {bin}")
    
    def get_memory_usage(self):
        """Return the total usage and total space available in all bins."""
        total_used = sum((bin.capacity - bin.remaining_space) for bin in self.bins)
        total_capacity = len(self.bins) * self.bin_capacity
        return {"total_used": total_used, "total_capacity": total_capacity}
