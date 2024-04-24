from tkinter import messagebox
from reportlab.pdfgen import canvas
import os

def text_to_pdf(input_file, output_file):
    # Sprawdzenie, czy plik PDF docelowy istnieje
    if os.path.exists(output_file):
        choice = messagebox.askquestion("Plik PDF już istnieje", "Plik PDF docelowy już istnieje. Czy chcesz go nadpisać?")

        if choice == "no":
            # Zakończenie bez zapisywania
            return

    c = canvas.Canvas(output_file)

    with open(input_file, "r") as file:
        content = file.read()

    lines = content.split("\n")

    y = 700  # Początkowa pozycja y

    for line in lines:
        c.drawString(50, y, line)  # Rysowanie linii tekstu
        y -= 15  # Przesunięcie do kolejnej linii o 15 jednostek

    c.save()

def export_to_pdf():
    # Ścieżka do pliku tekstowego
    text_file = "Wyniki.txt"

    # Ścieżka do pliku PDF
    pdf_file = "Wyniki.pdf"

    text_to_pdf(text_file, pdf_file)
    messagebox.showinfo("Eksport do PDF", "Plik PDF został zapisany.")

# Reszta kodu GUI...
