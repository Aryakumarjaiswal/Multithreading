import concurrent.futures
import time

def download_file(file_id):
    print(f"Downloading file {file_id}...")
    time.sleep(2)
    return f"File {file_id} done!"

files_to_download = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a pool of only 3 workers
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # map() automatically assigns tasks to the 3 workers
    results = executor.map(download_file, files_to_download)

    for result in results:
        print(result)
