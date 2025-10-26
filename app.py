from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample tickets
tickets = [
    {"id": 1, "event": "Concert A", "available": 5},
    {"id": 2, "event": "Movie B", "available": 10},
    {"id": 3, "event": "Theater C", "available": 3}
]

@app.route("/")
def home():
    return render_template("home.html", tickets=tickets)

@app.route("/book/<int:ticket_id>", methods=["POST"])
def book(ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id and ticket["available"] > 0:
            ticket["available"] -= 1
            return f"Successfully booked 1 ticket for {ticket['event']}! Remaining: {ticket['available']}"
    return "Ticket not available!", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
