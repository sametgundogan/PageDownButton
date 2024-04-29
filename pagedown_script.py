import pyautogui
import time
import threading

def press_page_down():
    while not stop_thread.is_set():
        pyautogui.press('pagedown')
        time.sleep(0.1)  # Adjust the sleep time as needed

        if pyautogui.press('enter'):
            break

def listen_for_stop():
    if pyautogui.press('enter'):
        stop_thread.set()

if __name__ == "__main__":
    stop_thread = threading.Event()

    print("The program will start after 5 seconds. Switch to the window where you want to press 'Page Down'.")
    time.sleep(5)  # Wait for 5 seconds before starting

    page_down_thread = threading.Thread(target=press_page_down)
    listen_thread = threading.Thread(target=listen_for_stop)

    page_down_thread.start()
    listen_thread.start()

    listen_thread.join()  # Wait for the listen thread to finish
    page_down_thread.join()  # Ensure the page down thread is also stopped before exiting
