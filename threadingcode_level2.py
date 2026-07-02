import time
import threading

def process_data(item_id):
    print(f"Processing item {item_id}...")
    time.sleep(2)

items_to_process = [101, 102, 103, 104, 105]
threads_list = [] # Ek khali list banayenge threads ko store karne ke liye

start_time = time.time()

# 1. Create and start threads
for item in items_to_process:
    t = threading.Thread(target=process_data, args=(item,))
    t.start()
    threads_list.append(t) # Thread ko list me save kar lo

# 2. Join all threads
for t in threads_list:
    t.join() # Sabka wait karo

print(f"All items processed in {time.time() - start_time:.2f} seconds!")
