from flask import Flask, render_template, request, send_from_directory
from utils import write_name

# Initalize the app
app = Flask(__name__)


@app.route("/")
def index():
    # Render the index.html page
    return render_template("index.html")


@app.route("/generatecert", methods=["POST"])
def generate_certificate():
    # Get the name from the form
    name = request.form.get("name")
    if not name:
        # If the name is empty, render the index.html page with an error message
        return "<h1>Invalid name</h1><a href='/'>Go back</a>"
    # Generate the certificate
    file_name = write_name(name)
    # Render the generated.html page
    return render_template("generated.html", file_name=file_name)


@app.route("/generated/<path:path>")
def send_image(path):
    return send_from_directory("generated", path)


if __name__ == "__main__":
    # Run the app
    app.run(debug=True)