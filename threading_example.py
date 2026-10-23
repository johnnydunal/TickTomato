# This was just me testing threading (will be removed later)

import threading
import time

def do(task_name, delay):
    print(f"[Starting] {task_name}...")
    time.sleep(delay)
    print(f"[Finished] {task_name}!")

thread1 = threading.Thread(target=do, args=("Download File A", 3))
thread2 = threading.Thread(target=do, args=("Download File B", 2))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All tasks complete!")