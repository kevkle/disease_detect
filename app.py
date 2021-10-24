from flask import Flask, request
from disease_detection import matching_codes

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    return '''
        <html>
            <body>
                <p>Enter your diagnosis:</p>
                <form method="post" action=".">
                    <p><input name="string1" /></p>
                    <p><input type="submit" value="Return the ICD code" /></p>
                </form>
            </body>
        </html>
    '''


if __name__ == "__main__":
    app.run(debug=True)