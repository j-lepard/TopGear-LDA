import time

# Disk I/O benchmark
def disk_io_benchmark():
    size = 100000000
    data = bytearray(size)
    
    # Write benchmark
    start_time = time.time()
    with open("test_file.bin", "wb") as f:
        f.write(data)
    end_time = time.time()
    print(f"Disk Write Benchmark: {end_time - start_time} seconds")
    
    # Read benchmark
    start_time = time.time()
    with open("test_file.bin", "rb") as f:
        data = f.read()
    end_time = time.time()
    print(f"Disk Read Benchmark: {end_time - start_time} seconds")

disk_io_benchmark()