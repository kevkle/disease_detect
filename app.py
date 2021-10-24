from flask import Flask, request
from disease_detection import matching_codes

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def diagnosis_page():
    if request.method == "POST":
        string1 = request.form["string1"]
        if string1 is not None:
            result = matching_codes(string1)
            return '''
                <html>
                    <body>
                        <p>The result is {result}</p>
                        <p><a href="/">Click here to make a new diagnosis </a>
                    </body>
                </html>
            '''.format(result=result)

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