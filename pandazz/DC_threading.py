import threading
import time
import random

# Function to simulate work for each thread
def worker(id, work_load):
    print(f"Worker {id} started.")
    time.sleep(work_load / 1000.0)  # Convert workload to seconds
    print(f"Worker {id} completed.")

def main():
    num_threads = 5

    print(f"Creating {num_threads} threads...")

    # Create and start threads
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=worker, args=(i+1, 1000))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        print("join ",thread)
        thread.join()

    print("Main thread completed.")

if __name__ == "__main__":
    main()
