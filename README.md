# Visual Cryptography Project

## Overview

The Visual Cryptography project is a Python application designed to encrypt and decrypt messages using images as a medium. It comprises two main files: `VisualCryptography.py` and `functions.py`. The former handles the graphical user interface (GUI) using the tkinter library, while the latter contains the core functions for message encryption and decryption using the Python Imaging Library (PIL).

### Features
- Encryption of textual messages into images
- Decryption of messages from encrypted images

## Installation

### Requirements
- Python 3.x
- Pillow (Python Imaging Library)
- tkinter library

### Steps
1. Clone or download the project repository from [GitHub](https://github.com/luKiszef/VisualCryptoGraphy).
2. Ensure you have Python 3.x installed on your system.
3. Install the required dependencies:
    ```bash
    pip install Pillow tkinter
    ```
4. Navigate to the project directory.
5. Run the `VisualCryptography.py` script:
    ```bash
    python VisualCryptography.py
    ```

## File Structure

- **VisualCryptography.py**: Main script containing the GUI and application logic.
- **functions.py**: Module containing functions for message encryption and decryption.

## functions.py

This file contains functions for message encryption and decryption using the Python Imaging Library (PIL).

### Functions

#### `text_to_binary(text: str) -> str`
Converts a textual message into a binary string.

- **Parameters:**
    - `text` (str): The message to be converted.

- **Returns:**
    - `binary_string` (str): Binary representation of the input text.

- **Description:**
    This function takes a textual message as input and converts it into a binary string. Each character in the input text is converted to its ASCII representation and then to an 8-bit binary string.

#### `binary_to_text(binary_string: str) -> str`
Converts a binary string back into its textual representation.

- **Parameters:**
    - `binary_string` (str): The binary string to be converted.

- **Returns:**
    - `text` (str): Textual representation of the input binary string.

- **Description:**
    This function reverses the process of `text_to_binary`. It takes a binary string as input and converts it back into its textual representation. The binary string is split into 8-bit chunks, each representing a character's ASCII code, which is then converted to its corresponding character.

#### `encrypt_image(image_path: str, binary_message: str) -> str`
Encrypts a binary message into an image.

- **Parameters:**
    - `image_path` (str): The file path to the input image.
    - `binary_message` (str): The binary message to be encrypted.

- **Returns:**
    - `encrypted_image_path` (str): File path to the encrypted image.

- **Description:**
    This function encrypts a binary message into an image using a least significant bit (LSB) substitution technique. It reads each pixel of the input image and modifies the least significant bit of its RGB components to encode the binary message. The resulting image is saved with the filename "encrypted_image.png" in the project directory.

#### `decrypt_image(image_path: str, message_length: int) -> str`
Decrypts a binary message from an encrypted image.

- **Parameters:**
    - `image_path` (str): The file path to the encrypted image.
    - `message_length` (int): The length of the original message (in characters).

- **Returns:**
    - `binary_message` (str): The decrypted binary message.

- **Description:**
    This function decrypts a binary message from an encrypted image. It reads each pixel of the encrypted image and extracts the least significant bit of its RGB components to reconstruct the binary message. The length of the original message is required to determine the number of bits to extract. The decrypted binary message is returned.

## VisualCryptography.py

This file contains the graphical user interface (GUI) for the Visual Cryptography application. It utilizes the tkinter library to create a user-friendly interface for encrypting and decrypting messages.

### Functions

#### `animate_button(button: tk.Button) -> None`
Animates a button by changing its relief style temporarily.

- **Parameters:**
    - `button` (tk.Button): The button to be animated.

- **Description:**
    This function modifies the relief style of the button to create a visual animation effect when clicked.

#### `show_options() -> None`
Displays encryption and decryption options after clicking the "Start" button.

- **Description:**
    This function hides the "Start" button and displays options for encryption and decryption, including mode labels, encrypt and decrypt buttons, and message entry field.

#### `encrypt() -> None`
Encrypts a message into an image file.

- **Description:**
    This function retrieves the message entered by the user, converts it to binary, prompts the user to select an image file, encrypts the binary message into the selected image using functions from `functions.py`, and displays a success message with the path to the encrypted image.

#### `decrypt() -> None`
Decrypts a message from an encrypted image file.

- **Description:**
    This function prompts the user to select an encrypted image file, decrypts the binary message from the image using functions from `functions.py`, converts the binary message to text, and displays the decrypted message in a messagebox.
