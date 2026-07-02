# The Danger of Threading (Race Conditions)
Threading bahut powerful hai, but isme ek risk hota hai. Agar multiple threads ek hi variable ko ek sath change karne ki koshish karein, toh data corrupt ho sakta hai. Isko tech ki bhasha me "Race Condition" kehte hain.
Isko fix karne ke liye hum **Lock** use karte hain. Lock ensure karta hai ki ek time par sirf ek hi thread us specific data ko modify kare.

### Code:
```plaintext
import threading

counter = 0
lock = threading.Lock() # Lock create kiya

def increase_counter():
    global counter
    for _ in range(100000):
        # Lock acquire karo, taaki koi aur thread interfere na kare
        with lock: 
            counter += 1

# Create 2 threads that modify the SAME variable
t1 = threading.Thread(target=increase_counter)
t2 = threading.Thread(target=increase_counter)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Final Counter Value: {counter}") # Hamesha exactly 200000 aayega
```
