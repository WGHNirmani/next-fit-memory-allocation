from allocator import NextFitMemoryAllocator

def main():
    """Main function to run the Next Fit Memory Allocation system."""
    
    # 1. Ask the user for bin capacity
    while True:
        try:
            bin_capacity = int(input("Enter the capacity of each bin (positive integer): "))
            if bin_capacity > 0:
                break
            else:
                print("Capacity must be a positive integer.")
        except ValueError:
            print("Please enter a valid number.")
    
    # 2. Ask the user for memory requests
    while True:
        try:
            memory_requests_input = input("Enter memory requests as a comma-separated list (e.g., 4,8,1,4,2,1): ")
            memory_requests = [int(x) for x in memory_requests_input.split(",")]
            if all(x > 0 for x in memory_requests):
                break
            else:
                print("Memory request sizes must be positive integers.")
        except ValueError:
            print("Please enter a list of numbers separated by commas.")
    
    # 3. Create an instance of the memory allocator
    allocator = NextFitMemoryAllocator(bin_capacity=bin_capacity)
    
    # 4. Allocate memory for each request
    for request in memory_requests:
        print(f"Allocating {request} units of memory...")
        allocator.allocate_memory(request)
    
    # 5. Display the final status of bins
    print("\nFinal Bins Status")
    allocator.display_bins()
    
    # 6. Display total memory usage
    usage = allocator.get_memory_usage()
    print(f"\nTotal Memory Used: {usage['total_used']} / {usage['total_capacity']}")

if __name__ == "__main__":
    main()
