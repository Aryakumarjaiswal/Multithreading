import time
import threading # Step A: Import the threading module

def download_file(file_name):
    print(f"Started downloading {file_name}...")
    time.sleep(3)
    print(f"Finished downloading {file_name}!")

start_time = time.time()

# Step B: Create Threads
# target = function ka naam (without parentheses)
# args = function ke parameters (must be a tuple, isiliye comma lagaya hai)
thread1 = threading.Thread(target=download_file, args=("Movie.mp4",))
thread2 = threading.Thread(target=download_file, args=("Song.mp3",))

# Step C: Start the threads
thread1.start() # Ye background me start ho jayega
thread2.start() # Ye bhi turant start ho jayega

# Step D: Wait for threads to finish (Join)
thread1.join()
thread2.join()

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")
