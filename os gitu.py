import tkinter as tk
from tkinter import messagebox

class TicketBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("ONLINE TICKET BOOKING")
        self.root.configure(bg='white')  # Set the background color to red

        width = root.winfo_screenwidth()  # Get the width of the screen
        height = root.winfo_screenheight()  # Get the height of the screen

        # Set the window size to cover the whole screen
        self.root.geometry(f"{width}x{height}")

        self.first_class_seats = 10
        self.second_class_seats = 15
        self.third_class_seats = 25

        self.movies = ["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5"]

        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg='white')
        main_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Movie and Class selection section
        movie_frame = tk.Frame(main_frame, bg='white')
        movie_frame.pack()

        self.label_movie = tk.Label(movie_frame, text="Select Movie:", bg='white')
        self.label_movie.pack()

        self.movie_var = tk.StringVar()
        self.movie_var.set(self.movies[0])
        self.movie_option_menu = tk.OptionMenu(movie_frame, self.movie_var, *self.movies)
        self.movie_option_menu.pack()

        class_frame = tk.Frame(main_frame, bg='white')
        class_frame.pack()

        self.class_var = tk.IntVar()
        self.class_var.set(1)
        self.class_selection = tk.Label(class_frame, text="Select Class:", bg='white')
        self.class_selection.pack()

        self.first_class = tk.Radiobutton(class_frame, text="First Class", variable=self.class_var, value=1)
        self.first_class.pack()

        self.second_class = tk.Radiobutton(class_frame, text="Second Class", variable=self.class_var, value=2)
        self.second_class.pack()

        self.third_class = tk.Radiobutton(class_frame, text="Third Class", variable=self.class_var, value=3)
        self.third_class.pack()

        self.book_button = tk.Button(main_frame, text="Book Ticket", command=self.select_seat, bg='white')
        self.book_button.pack()

    def select_seat(self):
        selected_movie = self.movie_var.get()
        selected_class = self.class_var.get()

        if selected_movie and selected_class:
            if selected_class == 1:
                seats = self.first_class_seats
            elif selected_class == 2:
                seats = self.second_class_seats
            elif selected_class == 3:
                seats = self.third_class_seats
            else:
                messagebox.showerror("Error", "Selected class is invalid.")
                return

            if seats > 0:
                self.show_seat_selection(selected_movie, selected_class, seats)
            else:
                messagebox.showerror("Error", "Selected class is sold out.")

    def show_seat_selection(self, selected_movie, selected_class, available_seats):
        seat_selection_window = tk.Toplevel()
        seat_selection_window.title("Select Seat")
        seat_selection_window.configure(bg='white')

        seat_selection_window.geometry(f"{self.root.winfo_screenwidth()//2}x{self.root.winfo_screenheight()//2}+{self.root.winfo_screenwidth()//4}+{self.root.winfo_screenheight()//4}")

        seat_var = tk.IntVar()

        tk.Label(seat_selection_window, text=f"Select a seat (1 to {available_seats}):", bg='white').pack()

        for seat in range(1, available_seats + 1):
            tk.Radiobutton(seat_selection_window, text=f"Seat {seat}", variable=seat_var, value=seat, bg='white').pack()

        def book_seat():
            selected_seat = seat_var.get()
            if selected_seat:
                messagebox.showinfo("Success", f"Seat {selected_seat} for {selected_movie} in Class {selected_class} is booked!")
                seat_selection_window.destroy()
            else:
                messagebox.showerror("Error", "Please select a seat.")

        tk.Button(seat_selection_window, text="Book", command=book_seat, bg='white').pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicketBookingSystem(root)
    root.mainloop()
