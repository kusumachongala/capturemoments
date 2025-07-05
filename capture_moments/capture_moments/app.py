from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Dummy data for photographers
photographers = [
    {"id": "p1", "name": "Amit Lensman", "skills": ["Wedding", "Portrait"], "image": "amit.jpg"},
    {"id": "p2", "name": "Sana Clickz", "skills": ["Fashion", "Event"], "image": "sana.jpg"}
]

# Dummy booked/availability dates
availability_data = {
    "p1": ["2025-06-20", "2025-06-23"],
    "p2": ["2025-06-19", "2025-06-22"]
}

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Photographer List Page
@app.route('/show-photographers')
def show_photographers():
    return render_template('photographers.html', photographers=photographers, availability_data=availability_data)

# Booking Page
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        photographer_id = request.form.get('photographer')
        date = request.form.get('date')

        # Optional: Save booking data or perform actions here

        return f"""
        <h2 style='color:green'>
            Booking Confirmed!<br>
            Name: {name}<br>
            Email: {email}<br>
            Photographer: {photographer_id}<br>
            Date: {date}
        </h2>
        """

    return render_template('book.html', photographers=photographers, booked_dates=availability_data)

if __name__ == '__main__':
    app.run(debug=True)
