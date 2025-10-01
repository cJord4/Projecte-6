import tkinter as tk
import time
import threading

def explotar(root, label):
    # Esperar 2 segundos antes de "explotar"
    time.sleep(2)
    
    # Simular parpadeo tipo explosión
    for i in range(6):
        color = "red" if i % 2 == 0 else "yellow"
        label.config(bg=color, fg="black")
        root.update()
        time.sleep(0.2)
    
    # Cerrar ventana
    root.destroy()

def main():
    root = tk.Tk()
    root.title("Explosión")
    root.geometry("300x200")

    label = tk.Label(root, text="Niggers", font=("Arial", 30))
    label.pack(expand=True)

    # Lanzamos la explosión en un hilo aparte
    threading.Thread(target=explotar, args=(root, label), daemon=True).start()

    root.mainloop()

if __name__ == "__main__":
    main()
