import pymem
import os
import pydirectinput
import keyboard
import time
import threading

def aob_injection(process, aob):
    
    pm = pymem.Pymem(process)
    aob_address = pymem.pattern.pattern_scan_all(pm.process_handle, aob)
    print(aob_address)
    offset_x = 0xBB
    offset_y = 0xBB + 0x4
    aob_address_x = (aob_address + offset_x)
    aob_address_y = (aob_address + offset_y)

    move_char_x = 50000000
    move_char_y = 500000000

    time_to_sleep = 0.05

    def tp_right():
        current_value = pm.read_int(aob_address_x)
        new_value = current_value + move_char_x
        pm.write_int(aob_address_x, new_value)
        print("tp_right")
    def tp_left():
        current_value = pm.read_int(aob_address_x)
        new_value = current_value - move_char_x
        pm.write_int(aob_address_x, new_value)
        print("tp_left")

    def tp_up():
        current_value = pm.read_int(aob_address_y)
        new_value = current_value - move_char_y
        pm.write_int(aob_address_y, new_value)
        print("tp_up")

    def tp_down():
        current_value = pm.read_int(aob_address_y)
        new_value = current_value + move_char_y
        pm.write_int(aob_address_y, new_value)
        print("tp_down")

    while True:
        if keyboard.is_pressed('up') and keyboard.is_pressed('right'):
            tp_up()
            tp_right()
            time.sleep(time_to_sleep*2)
            continue

        if keyboard.is_pressed('up') and keyboard.is_pressed('left'):
            tp_up()
            tp_left()
            time.sleep(time_to_sleep*2)
            continue

        if keyboard.is_pressed('down') and keyboard.is_pressed('right'):
            tp_down()
            tp_right()
            time.sleep(time_to_sleep*2)
            continue

        if keyboard.is_pressed('down') and keyboard.is_pressed('left'):
            tp_down()
            tp_left()
            time.sleep(time_to_sleep*2)
            continue

        if keyboard.is_pressed('up'):
            tp_up()
            time.sleep(time_to_sleep)
            continue

        if keyboard.is_pressed('down'):
            tp_down()
            time.sleep(time_to_sleep)
            continue

        if keyboard.is_pressed('right'):
            tp_right()
            time.sleep(time_to_sleep)
            continue

        if keyboard.is_pressed('left'):
            tp_left()
            time.sleep(time_to_sleep)
            continue
    

aob = rb"\x78\x04\x6C\x01\x00\x00\x00\x00\x00\x00\x40\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x40\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x3F\x00\x00\x80\x3F\x68\x01\x00\x00\xFF\x00\x00\x00\xFF\x00\x00\x00\xFF\x00\x00\x00..\x00\x00..\x00\x00..\x00\x00..\x00\x00..\x00\x00..\x00\x00..\x00\x00..\x00\x00..\x00\x00"

aob_injection("WonderKing.exe", aob)