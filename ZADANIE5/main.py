import tkinter as tk

# Napisz funkcję create_app(), która:
# Tworzy główne okno Tkinter,
# Dodaje etykietę (label) z jakimś wstępnym tekstem (np. "Wpisz coś:"),
# Dodaje pole tekstowe (Entry), w którym użytkownik może coś wpisać,
# Dodaje przycisk (Button), po którego kliknięciu tekst z pola Entry zostanie wyświetlony w drugiej etykiecie (np. "Wpisałeś: <tekst>").


def create_app():
    """
    Tworzy i zwraca główne okno Tkinter z prostym interfejsem.
    1) Etykieta: "Wpisz coś:"
    2) Pole Entry
    3) Przycisk "Pokaż", który wyświetli wpisany tekst w innej etykiecie
    """
    # title - "Prosta aplikacja Tkinter"
    app = tk.Tk()
    app.geometry("300x200")
    app.title("Prosta aplikacja Tkinter")

    # label_instruct = umocuj przez pack
    label_instruct = tk.Label(app, text="Wpisz coś:")
    label_instruct.pack()

    entry_text = tk.Entry(app)
    entry_text.pack()

    label_result = tk.Label(app, text="Tu pojawi się Twój tekst")
    label_result.pack()

    # zdefiniuj funkcję show_text() pobierającą wpisany tekst i wyświetlającą w label_result
    def show_text():
        entered_text = entry_text.get()
        label_result.config(text=f"Wpisałeś: {entered_text}")

    button_show = tk.Button(app, text="Pokaż", command=show_text)
    button_show.pack()

    return app


if __name__ == '__main__':
    app = create_app()
    app.mainloop()
