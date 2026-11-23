from flask import Flask, render_template

app = Flask(__name__)

tickets = [
    {
        "id": 1251,
        "customer": "Example Company",
        "issue": "Unable to access email",
        "priority": "High",
        "status": "In Progress"
    },
    {
        "id": 3551,
        "customer": "Northwood Ltd",
        "issue": "Printer not responding",
        "priority": "Medium",
        "status": "New"
    },
    {
        "id": 3681,
        "customer": "Westfield Office",
        "issue": "Computer running slow",
        "priority": "Low",
        "status": "Resolved"
    },
    {
        "id": 4921,
        "customer": "Apex Corporation",
        "issue": "VPN Disconnect",
        "priority": "High",
        "status": "In Progress"
    },
]


@app.route("/")
def dashboard():
    return render_template("dashboard.html", tickets=tickets)


@app.route("/tickets")
def ticket_list():
    return render_template("tickets.html", tickets=tickets)


if __name__ == "__main__":
    from livereload import Server

    server = Server(app)

    server.watch("templates/")
    server.watch("static/")

    server.serve(port=5000, host="127.0.0.1")