import customtkinter as ctk

def calculate():

    try:
        # Get marks of 5 subjects
        subject1 = float(subject1_entry.get())
        subject2 = float(subject2_entry.get())
        subject3 = float(subject3_entry.get())
        subject4 = float(subject4_entry.get())
        subject5 = float(subject5_entry.get())

        # Check whether marks are valid
        if (
            subject1 < 0 or subject1 > 100 or
            subject2 < 0 or subject2 > 100 or
            subject3 < 0 or subject3 > 100 or
            subject4 < 0 or subject4 > 100 or
            subject5 < 0 or subject5 > 100
        ):
            result_label.configure(
                text="Please enter marks between 0 and 100."
            )
            return

        # Calculate total
        total = (
            subject1+subject2+subject3+subject4+subject5
        )

        # Calculate percentage
        percentage = total / 5


        # ----------------------------------------------------
        # Grade calculation
        # ----------------------------------------------------

        if percentage >= 90:
            grade = "A+"

        elif percentage >= 80:
            grade = "A"

        elif percentage >= 70:
            grade = "B"

        elif percentage >= 60:
            grade = "C"

        elif percentage >= 50:
            grade = "D"

        elif percentage >= 40:
            grade = "E"

        else:
            grade = "F"


        # ----------------------------------------------------
        # Pass / Fail
        # ----------------------------------------------------

        # if percentage >= 40:
        #     status = "PASS"

        # else:
        #     status = "FAIL"


        # ----------------------------------------------------
        # Display result
        # ----------------------------------------------------

        result_label.configure(
            text=(
                f"Total Marks: {total:.0f}/500\n"
                f"Percentage: {percentage:.2f}%\n"
                f"Grade: {grade}\n"
                # f"Result: {status}"
            )
        )


    except ValueError:

        result_label.configure(
            text="Please enter valid marks."
        )


# ------------------------------------------------------------
# Function to clear all fields
# ------------------------------------------------------------

def clear_fields():

    subject1_entry.delete(0, "end")
    subject2_entry.delete(0, "end")
    subject3_entry.delete(0, "end")
    subject4_entry.delete(0, "end")
    subject5_entry.delete(0, "end")

    result_label.configure(
        text="Result:"
    )


# ------------------------------------------------------------
# CustomTkinter settings
# ------------------------------------------------------------

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


# ------------------------------------------------------------
# Create application window
# ------------------------------------------------------------

app = ctk.CTk()

app.title("Student Grade Analysis System")
app.geometry("600x750")


# ------------------------------------------------------------
# Heading
# ------------------------------------------------------------

heading = ctk.CTkLabel(
    app,
    text="Student Grade Analysis System",
    font=("Arial", 28, "bold")
)

heading.pack(pady=25)


# ------------------------------------------------------------
# Subject 1
# ------------------------------------------------------------

subject1_label = ctk.CTkLabel(
    app,
    text="Enter Subject 1 Marks:",
    font=("Arial", 16)
)

subject1_label.pack(pady=(5, 2))


subject1_entry = ctk.CTkEntry(
    app,
    width=250,
    placeholder_text="Marks out of 100"
)

subject1_entry.pack(pady=5)


# ------------------------------------------------------------
# Subject 2
# ------------------------------------------------------------

subject2_label = ctk.CTkLabel(
    app,
    text="Enter Subject 2 Marks:",
    font=("Arial", 16)
)

subject2_label.pack(pady=(5, 2))


subject2_entry = ctk.CTkEntry(
    app,
    width=250,
    placeholder_text="Marks out of 100"
)

subject2_entry.pack(pady=5)


# ------------------------------------------------------------
# Subject 3
# ------------------------------------------------------------

subject3_label = ctk.CTkLabel(
    app,
    text="Enter Subject 3 Marks:",
    font=("Arial", 16)
)

subject3_label.pack(pady=(5, 2))


subject3_entry = ctk.CTkEntry(
    app,
    width=250,
    placeholder_text="Marks out of 100"
)

subject3_entry.pack(pady=5)


# ------------------------------------------------------------
# Subject 4
# ------------------------------------------------------------

subject4_label = ctk.CTkLabel(
    app,
    text="Enter Subject 4 Marks:",
    font=("Arial", 16)
)

subject4_label.pack(pady=(5, 2))


subject4_entry = ctk.CTkEntry(
    app,
    width=250,
    placeholder_text="Marks out of 100"
)

subject4_entry.pack(pady=5)


# ------------------------------------------------------------
# Subject 5
# ------------------------------------------------------------

subject5_label = ctk.CTkLabel(
    app,
    text="Enter Subject 5 Marks:",
    font=("Arial", 16)
)

subject5_label.pack(pady=(5, 2))


subject5_entry = ctk.CTkEntry(
    app,
    width=250,
    placeholder_text="Marks out of 100"
)

subject5_entry.pack(pady=5)


# ------------------------------------------------------------
# Calculate button
# ------------------------------------------------------------

calculate_button = ctk.CTkButton(
    app,
    text="Calculate Grade",
    width=200,
    command=calculate
)

calculate_button.pack(pady=15)


# ------------------------------------------------------------
# Clear button
# ------------------------------------------------------------

clear_button = ctk.CTkButton(
    app,
    text="Clear",
    width=200,
    command=clear_fields
)

clear_button.pack(pady=5)


# ------------------------------------------------------------
# Result label
# ------------------------------------------------------------

result_label = ctk.CTkLabel(
    app,
    text="Result:",
    font=("Arial", 20, "bold")
)

result_label.pack(pady=25)


# ------------------------------------------------------------
# Start application
# ------------------------------------------------------------

app.mainloop()