import time
import numpy as np
def download_file(file_name):
    print(f"Started downloading {file_name}...")
    time.sleep(3) # Simulating a 3-second download time
    print(f"Finished downloading {file_name}!")

start_time = time.time()

# Normal execution (Ek ke baad ek)
download_file("Movie.mp4")
download_file("Song.mp3")

end_time = time.time()
print(f"Total time taken: {np.round(end_time - start_time,0)} seconds")
