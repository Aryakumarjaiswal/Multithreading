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


```plaintext
import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def thread1():
    with lock1:
        print("Thread 1: Lock1 acquired")
        time.sleep(1)

        print("Thread 1: Waiting for Lock2")
        with lock2:
            print("Thread 1: Lock2 acquired")


def thread2():
    with lock2:
        print("Thread 2: Lock2 acquired")
        time.sleep(1)

        print("Thread 2: Waiting for Lock1")
        with lock1:
            print("Thread 2: Lock1 acquired")


t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()

### 2. The Nightmare of Threading: Deadlocks
Humne seekha tha ki data corrupt hone se bachane ke liye hum `Lock` use karte hain. But locks ek nayi problem create kar sakte hain jisko **Deadlock** kehte hain.

**Deadlock kya hai?**
Imagine Thread A ke paas `Lock 1` hai aur usko apna kaam khatam karne ke liye `Lock 2` chahiye. At the same time, Thread B ke paas `Lock 2` hai aur usko `Lock 1` chahiye. 
* Result: Dono ek dusre ka wait karte rahenge infinite time ke liye, aur aapka program hamesha ke liye hang ho jayega! Software engineering mein Deadlocks ko fix karna sabse mushkil kaamon mein se ek hai.

---

### 3. Daemon Threads (Background Workers)
Normally, Python program tab tak close nahi hota jab tak saare threads apna kaam finish na kar lein. But sometimes, you want a thread to run silently in the background (like an auto-save feature in MS Word, or a background clock).

Agar aap kisi thread ko **Daemon** bana dete ho, toh main program uske finish hone ka wait nahi karta. Jaise hi main program khatam hoga, Daemon thread automatically kill ho jayega.

```python
import threading
import time

def background_task():
    while True:
        print("Running in background...")
        time.sleep(1)

# daemon=True set karne se ye background worker ban jayega
t = threading.Thread(target=background_task, daemon=True)
t.start()

time.sleep(3)
print("Main program finished! Background thread will die now.")
# Program will exit here, and the background task will be killed instantly.
```

---

### 4. The Python Secret: The GIL (Global Interpreter Lock)
This is a very famous interview question! Python mein ek limitation hai jisko **GIL** kehte hain. 

Because of the GIL, Python mein multiple threads *actually* ek hi exact microsecond par multiple CPU cores par run nahi kar sakte. Python unke beech mein itni fast switch karta hai ki humein lagta hai wo ek sath chal rahe hain.

**Toh iska kya matlab hai?**
* **I/O Bound Tasks (Network/Files):** Jaise downloading files, database queries, API calls. Yahan CPU waise bhi wait kar raha hota hai. **Threading works perfectly here!** (Jo humne abhi tak seekha).
* **CPU Bound Tasks (Heavy Math/Gaming):** Jaise video rendering, AI model training, ya heavy calculations. Yahan threading Python mein program ko fast *nahi* karegi. Aise tasks ke liye humein threading ki jagah **`multiprocessing`** module use karna padta hai (jo threads ki jagah poore naye processes banata hai).

### Summary
Agar aapne basic `Thread`, `.start()`, `.join()`, `Lock`, aur `ThreadPoolExecutor` seekh liya hai, toh aap 95% real-world applications easily bana sakte ho. Deadlocks aur GIL advanced topics hain jo aapko ek better software engineer banne mein help karenge!

```
1. Thread Communication (The Producer-Consumer Problem)
Abhi tak humare threads apna kaam akele kar rahe the. But what if Thread A ko continuously data generate karna hai aur Thread B ko us data ko process karna hai?
Concept: Iske liye hum queue.Queue use karte hain. Ye ek special thread-safe pipe hai. Thread A isme data daalta rehta hai, aur Thread B isme se data nikalta rehta hai bina kisi race condition ke.


2. Advanced Synchronization (Beyond Simple Locks)
Humne Lock seekha (jo sirf 1 thread ko allow karta hai). But real world me aur bhi tools hote hain:
Semaphore: Imagine a club with a bouncer. Agar club me sirf 50 logon ki jagah hai, toh bouncer sirf 50 ko andar jane dega. Semaphore exactly yahi karta hai. Agar aap chahte ho ki database par ek sath max 5 threads hi query karein (taaki database crash na ho), toh aap Semaphore use karte ho.
Event: Ye ek traffic signal ki tarah hai. Ek thread wait kar raha hota hai, aur dusra thread usko "Green Light" (signal) deta hai ki "Mera kaam ho gaya hai, ab tu apna kaam start kar".
RLock (Reentrant Lock): Agar ek thread galti se same Lock ko do baar lock karne ki koshish kare, toh wo khud hi deadlock me phas jata hai. RLock ek smart lock hai jo same thread ko multiple times lock acquire karne allow karta hai.


3. Thread-Local Storage (threading.local())
Kabhi kabhi hum chahte hain ki har thread ka apna ek private variable ho jo dusre threads na dekh sakein. For example, agar 100 users aapki website use kar rahe hain (100 threads), toh har thread me user ka apna private session data hona chahiye. Iske liye Thread-Local memory use hoti hai.


4. The Modern Alternative: asyncio (Asynchronous Programming)
Aaj kal tech industry me (especially Python aur JavaScript me) heavy network tasks ke liye traditional threading thodi purani ho gayi hai.
Uski jagah hum asyncio use karte hain. Ye single-thread me hi multithreading jaisa kaam karta hai using an "Event Loop". Ye traditional threading se much faster aur memory-efficient hota hai for web servers (jaise FastAPI).

