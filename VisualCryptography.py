import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def text_to_binary(text):
    binary_string = ""
    for char in text:
        binary_char = format(ord(char), '08b')
        binary_string += binary_char
    return binary_string

def binary_to_text(binary_string):
    text = ""
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        text += chr(int(byte, 2))
    return text