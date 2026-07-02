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

Absolutely! Let's learn how to build a multi-threaded application from scratch. Hum Python use karenge because it is very beginner-friendly aur isme threading implement karna kaafi asaan hai.
We will go step-by-step. Pehle hum ek normal (slow) program likhenge, and then hum usko multi-threading se fast banayenge.
Step 1: The Problem (Without Threading)
Imagine you are building an app that downloads 2 files from the internet. Har file ko download hone mein 3 seconds lagte hain.
Let's write a normal, single-threaded program first:
code
Python
import time

def download_file(file_name):
    print(f"Started downloading {file_name}...")
    time.sleep(3) # Simulating a 3-second download time
    print(f"Finished downloading {file_name}!")

start_time = time.time()

# Normal execution (Ek ke baad ek)
download_file("Movie.mp4")
download_file("Song.mp3")

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")
What happens here?
Program pehle "Movie.mp4" download karega. Jab tak wo finish nahi hota, "Song.mp3" start nahi hoga. Total time 6 seconds lagega. Ye kaafi inefficient hai, right?
Step 2: The Solution (Using Multi-Threading)
Now, let's use Python's built-in threading module to do both tasks at the exact same time.
code
Python
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
# Let's understand the magic here:

# threading.Thread(...): Yahan humne do alag "workers" (threads) banaye. Humne unko bataya ki kaunsa function run karna hai (target) aur kya data dena hai (args).

# .start(): Jaise hi aap .start() call karte ho, thread apna kaam shuru kar deta hai aur main program aage badh jata hai bina wait kiye.

# .join(): This is very important! Ye main program ko bolta hai ki "Bhai, aage mat badhna jab tak thread1 aur thread2 apna kaam finish na kar lein." Agar aap .join() nahi lagaoge, toh program turant end ho jayega aur total time 0 seconds dikhayega, even though background me download chal raha hoga.
# Result: Ab dono files ek sath download ho rahi hain, so total time will be just 3 seconds!
