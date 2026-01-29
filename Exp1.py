from flask import Flask, request, render_template_string

app = Flask(__name__)

form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Multiplication Table</title>
</head>
<body>
    <h1>Generate Multiplication Table</h1>
    <form method="POST">
        <label>Enter a number:</label>
        <input type="number" name="number" required>
        <button type="submit">Generate</button>
    </form>

    {% if table %}
    <h2>Table of {{ num }}</h2>
    <table border="1" cellpadding="8">
        {% for i,val in table.items() %}
        <tr>
            <td>{{ num }} × {{ i }}</td>
            <td>{{ val }}</td>
        </tr>
        {% endfor %}
    </table>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    table = None
    num = None

    if request.method == "POST":
        num = int(request.form['number'])
        table = {i: num * i for i in range(1, 11)}

    return render_template_string(form_html, table=table, num=num)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
