import tkinter as tk

# Create application
app = tk.Tk()
app.title("Discount Calculator")
app.geometry("500x450")

# Application title
title = tk.Label(app, text="DISCOUNT CALCULATOR")
title.pack(pady=10)

# Original Price input
tk.Label(app, text="Original Price (Rp)").pack()

price = tk.Entry(app)
price.pack()

# Discount input
tk.Label(app, text="Discount (%)").pack()

discount = tk.Entry(app)
discount.pack()

# Calculate function
def calculate():
    p = int(price.get())
    d = int(discount.get())

    discount_amount = p * d / 100
    total = p - discount_amount

    result.config(
        text="Final Price: Rp" + str(int(total))
    )

# Calculate button
button = tk.Button(
    app,
    text="CALCULATE",
    command=calculate
)
button.pack(pady=15)

# Result display
result = tk.Label(app, text="Result will appear here")
result.pack()

# Run application
app.mainloop()
