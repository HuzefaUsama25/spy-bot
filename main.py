import pyautogui
import time
import datetime
import os
import shutil
import zipfile


def get_current_time():
    e = datetime.datetime.now()
    current_time = e.strftime("%a %b %d, %Y -- %I.%M.%S %p")
    return current_time


def take_and_save_screenshot(session_folder, current_time):
    screenshot = pyautogui.screenshot()
    filepath = f'{session_folder}/{current_time}.png'
    screenshot.save(filepath)


def start_session():
    folder_name = datetime.datetime.now().strftime("%d %b, %Y")

    if folder_name in os.listdir():
        folder_name = folder_name + " -- " + \
            str(datetime.datetime.now().strftime("%H.%M.%S"))

    os.mkdir(folder_name)

    while True:
        take_and_save_screenshot(folder_name, get_current_time())


def zip_old_session():
    old_session_name = str([i for i in os.listdir() if "." not in i][0])
    shutil.make_archive(old_session_name, 'tar', old_session_name)


def main():
    try:
        zip_old_session()
    except Exception as e:
        print(e)
    start_session()


if __name__ == "__main__":
    main()
