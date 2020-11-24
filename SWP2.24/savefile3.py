from PIL import Image, ImageTk
import tkinter as tk
import os
cnt = len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/'))-2
window = tk.Tk()
canvas = tk.Canvas(window, width= 1000, height = 1000)
canvas.pack()
image_list = []
k = 1
h = 1
for i in range(1,cnt):
    img = Image.open('/home/user/PycharmProjects/FirstUnittest/SWP2.24/savedimage{}.jpg'.format(i))
    imResize = img.resize((200,200))
    img_a = ImageTk.PhotoImage(imResize)
    image_list.append(img_a)
    if 200 * k == 1000:
        k = 1
        h += 1
    canvas.create_image(200 * k, 200 * h, image=image_list[i - 1])
    k += 1




window.mainloop()

print(image_list)

