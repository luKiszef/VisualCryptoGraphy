import tkinter as tk
from tkinter import filedialog, messagebox
from functions import encrypt_image, decrypt_image, text_to_binary, binary_to_text

def animate_button(button):
    button.config(relief=tk.SUNKEN)
    button.after(100, lambda: button.config(relief=tk.RAISED))

def show_options():
    start_button.destroy()
    visual_cryptography_label.destroy()
    mode_label.pack()
    encrypt_button.pack(pady=5)
    decrypt_button.pack(pady=5)
    message_label.pack()
    message_entry.pack(pady=5)

def encrypt():
    message = message_entry.get()
    if not message:
        messagebox.showerror("Error", "Please enter a message.")
        return
    binary_message = text_to_binary(message)
    image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if not image_path:
        messagebox.showerror("Error", "Please select an image.")
        return
    encrypted_image_path = encrypt_image(image_path, binary_message)
    messagebox.showinfo("Success", f"Image encrypted successfully. Saved as {encrypted_image_path}.")

def decrypt():
    image_path = filedialog.askopenfilename(title="Select Encrypted Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if not image_path:
        messagebox.showerror("Error", "Please select an encrypted image.")
        return
    binary_message = decrypt_image(image_path, len(message_entry.get()) * 8)
    decrypted_message = binary_to_text(binary_message)
    messagebox.showinfo("Decrypted Message", f"The decrypted message is: {decrypted_message}")


root = tk.Tk()
root.title("Image Encryption")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

visual_cryptography_label = tk.Label(root, text="Visual Cryptography", bg="#f0f0f0", font=("Helvetica", 24, "bold"))
visual_cryptography_label.pack(pady=50)

start_button = tk.Button(root, text="Start", command=show_options, bg="#008CBA", fg="white", font=("Helvetica", 16))
start_button.pack()

mode_label = tk.Label(root, text="Choose Mode:", bg="#f0f0f0", font=("Helvetica", 14))
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt, bg="#4CAF50", fg="white", font=("Helvetica", 12))
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt, bg="#FF5733", fg="white", font=("Helvetica", 12))
message_label = tk.Label(root, text="Enter Message:", bg="#f0f0f0", font=("Helvetica", 14))
message_entry = tk.Entry(root, width=30)

root.mainloop()
