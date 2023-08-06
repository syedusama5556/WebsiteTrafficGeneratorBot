import requests
import threading
import time
import os
from math import log

class ProgressBar:
    def __init__(self, total):
        self.total = total
        self.completed = 0
        self.lock = threading.Lock()

    def update(self, chunk_size):
        with self.lock:
            self.completed += chunk_size
            percent = round(self.completed / self.total * 100, 2)
            size, unit = self.format_size(self.completed)
            total_size, total_unit = self.format_size(self.total)
            print(f'\r[{"#" * int(percent / 10)}{" " * (10 - int(percent / 10))}] {percent}% {size:.2f} {unit}/{total_size:.2f} {total_unit} downloaded', end='')

    def format_size(self, size):
        if size == 0:
            return 0, 'B'
        size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
        i = int(log(size, 1024))
        p = 1024 ** i
        size = round(size / p, 2)
        return size, size_name[i]

def download_range(url, start, end, file, progress):
    headers = {'Range': 'bytes={}-{}'.format(start, end)}
    response = requests.get(url, headers=headers, stream=True)

    # Write chunk to file
    with open(file, 'r+b') as f:
        f.seek(start)
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
            progress.update(len(chunk))

def download(url, num_threads=4):
    # Get file size
    response = requests.head(url)
    file_size = int(response.headers.get('Content-Length', 0))

    # Create progress bar
    progress = ProgressBar(file_size)

    # Create file or resume download
    file = url.split('/')[-1]
    if os.path.exists(file):
        file_size_downloaded = os.path.getsize(file)
        if file_size_downloaded < file_size:
            # Resume download from where it left off
            print('Resuming download...')
            ranges = [(i + file_size_downloaded, (i + 1) * num_threads - 1 + file_size_downloaded) for i in range(num_threads)]
            ranges[-1] = (ranges[-1][0], file_size - 1)
            with open(file, 'ab') as f:
                pass
        else:
            print('File already exists.')
            return
    else:
        # Create empty file
        ranges = [(i * (file_size // num_threads), (i + 1) * (file_size // num_threads) - 1) for i in range(num_threads)]
        ranges[-1] = (ranges[-1][0], file_size - 1)
        with open(file, 'wb') as f:
            f.write(b'\0' * file_size)

    # Create threads to download each chunk
    threads = []
    for i in range(num_threads):
        args = (url, ranges[i][0], ranges[i][1], file, progress)
        thread = threading.Thread(target=download_range, args=args)
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    start_time = time.time()
    for thread in threads:
        thread.join()

    # Print download speed and estimated completion time
    end_time = time.time()
    duration = end_time - start_time
    download_speed = file_size / duration / 1024 / 1024
    remaining_size = file_size - progress.completed
    remaining_time = remaining_size / (download_speed * 1024 * 1024)
    print('\nDownload complete in {:.2f} seconds ({:.2f} MB/s)'.format(duration, download_speed))
    print('Estimated completion time: {:.2f} seconds'.format(remaining_time))

if __name__ == '__main__':
    url = 'https://cdn-141.anonfiles.com/Ja9bsdj4z5/10dee202-1680946118/bemusic-304.rar'
    download(url, num_threads=30)
