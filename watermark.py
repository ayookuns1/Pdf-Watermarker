import PyPDF2
import tkinter as tk
from tkinter import filedialog



class PDFWatermarkerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Watermarker")
        self.root.geometry("400x300")

        self.template_path = ""
        self.watermark_path = ""

        self.header_label = tk.Label(root, text="PDF Watermarker", font=("Helvetica", 16, "bold"), fg="#003399")
        self.header_label.pack(pady=20)

        self.template_label = tk.Label(root, text="Select Template PDF:", font=("Helvetica", 12))
        self.template_label.pack()

        self.template_button = tk.Button(root, text="Browse", command=self.load_template, font=("Helvetica", 10))
        self.template_button.pack()

        self.watermark_label = tk.Label(root, text="Select Watermark PDF:", font=("Helvetica", 12))
        self.watermark_label.pack()

        self.watermark_button = tk.Button(root, text="Browse", command=self.load_watermark, font=("Helvetica", 10))
        self.watermark_button.pack()

        self.watermark_button = tk.Button(root, text="Watermark PDF", command=self.watermark_pdf,
                                          font=("Helvetica", 12, "bold"), bg="#66CC00", fg="white")
        self.watermark_button.pack(pady=20)

    def load_template(self):
        self.template_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    def load_watermark(self):
        self.watermark_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf" )])


    def watermark_pdf(self):
        if not self.template_path or not self.watermark_path:
            return

        template = PyPDF2.PdfReader(open(self.template_path, 'rb'))
        watermark = PyPDF2.PdfReader(open(self.watermark_path, 'rb'))

        output = PyPDF2.PdfWriter()

        for i in range(len(template.pages)):
            page = template.pages[i]
            page.merge_page(watermark.pages[0])
            output.add_page(page)

        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        with open(output_path, 'wb') as file:
            output.write(file)

        self.template_path = ""
        self.watermark_path = ""
        self.template_button.config(text="Browse")
        self.watermark_button.config(text="Browse")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFWatermarkerApp(root)
    root.mainloop()