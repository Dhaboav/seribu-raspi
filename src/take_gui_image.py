import customtkinter as ctk
import cv2
from picamera2 import Picamera2
from PIL import Image, ImageTk
import os
import time

# Setup folder penyimpanan
save_dir = "images"
os.makedirs(save_dir, exist_ok=True)

# Inisialisasi Picamera2
picam2 = Picamera2()
preview_config = picam2.create_preview_configuration(main={"format": "XRGB8888", "size": (640, 480)})
picam2.configure(preview_config)
picam2.start()

# Setup customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PiCamera GUI")
        self.geometry("720x640")
        self.counter = 0

        # Preview Frame
        self.preview_label = ctk.CTkLabel(self, text="")
        self.preview_label.pack(pady=10)

        # Counter
        self.counter_label = ctk.CTkLabel(self, text=f"Captured: {self.counter}", font=ctk.CTkFont(size=16))
        self.counter_label.pack(pady=5)

        # Tombol-tombol dalam satu frame (horizontal)
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=20)

        # Tombol Capture (kiri)
        self.capture_btn = ctk.CTkButton(self.button_frame, text="Capture", command=self.capture_image)
        self.capture_btn.pack(side="left", padx=10)

        # Tombol Exit (kanan, merah)
        self.exit_btn = ctk.CTkButton(self.button_frame, text="Exit", command=self.quit_app, fg_color="red", hover_color="#aa0000")
        self.exit_btn.pack(side="left", padx=10)

        self.update_frame()  # Start preview loop

    def update_frame(self):
        frame = picam2.capture_array()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(rgb)
        image = image.resize((640, 480))
        imgtk = ImageTk.PhotoImage(image=image)
        self.preview_label.imgtk = imgtk
        self.preview_label.configure(image=imgtk)
        self.after(10, self.update_frame)  # Refresh setiap 10ms

    def capture_image(self):
        filename = os.path.join(save_dir, f"capture_{self.counter}.jpg")
        frame = picam2.capture_array()
        cv2.imwrite(filename, frame)
        self.counter += 1
        self.counter_label.configure(text=f"Captured: {self.counter}")
        print(f"[INFO] Gambar disimpan: {filename}")

    def quit_app(self):
        picam2.stop()
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
  
