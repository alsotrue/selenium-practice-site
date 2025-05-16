from flask import Flask, render_template_string, request

app = Flask(__name__)

main_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Selenium Practice Page</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .container {
            width: 90%;
            margin: auto;
        }
        .section {
            padding: 20px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        iframe {
            border: 1px solid #999;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        nav a {
            margin-right: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <nav>
            <a href="/">Home</a>
            <a href="/form-page">Form Page</a>
            <a href="/iframe-page" target="_blank">Iframe Page</a>
            <a href="/popup-page" target="_blank">Popup Page</a>
        </nav>

        <h1>Welcome to Selenium Practice Site</h1>

        <div class="section">
            <h2>Form Inputs</h2>
            <form action="/form-page" method="post">
                <label for="text1">Name:</label>
                <input type="text" id="text1" name="text1"><br><br>

                <h3>Skills (Checkbox):</h3>
                <input type="checkbox" id="skill1" name="skills" value="Python">
                <label for="skill1">Python</label>
                <input type="checkbox" id="skill2" name="skills" value="Selenium">
                <label for="skill2">Selenium</label><br><br>

                <h3>Gender (Radio):</h3>
                <input type="radio" id="male" name="gender" value="Male">
                <label for="male">Male</label>
                <input type="radio" id="female" name="gender" value="Female">
                <label for="female">Female</label><br><br>

                <h3>Country:</h3>
                <select id="country" name="country">
                    <option value="">--Choose--</option>
                    <option value="Taiwan">Taiwan</option>
                    <option value="Japan">Japan</option>
                    <option value="USA">USA</option>
                </select><br><br>

                <button type="submit">Submit</button>
            </form>
        </div>

        <div class="section">
            <h2>Element State and Navigation</h2>
            <button id="hiddenBtn" style="display:none">You can't see me</button><br><br>
            <button id="disabledBtn" disabled>This is disabled</button><br><br>

            <h3>Iframe Example:</h3>
            <iframe src="/iframe-page" title="iframe test" width="100%" height="100"></iframe><br><br>

            <h3>Links:</h3>
            <a href="/popup-page" target="_blank">Open Custom Popup Page</a><br>
            <a href="https://www.google.com" target="_blank">Open Google</a>
        </div>

        <div class="section">
            <h2>JavaScript Dialogs & Table</h2>
            <button onclick="alert('This is an alert!')">Trigger Alert</button>
            <button onclick="confirm('Do you confirm?')">Trigger Confirm</button>
            <button onclick="prompt('Please enter your input:')">Trigger Prompt</button><br><br>

            <h3>Sample Table:</h3>
            <table>
                <tr><th>ID</th><th>Name</th><th>Country</th></tr>
                <tr><td>1</td><td>Alice</td><td>Taiwan</td></tr>
                <tr><td>2</td><td>Bob</td><td>Japan</td></tr>
                <tr><td>3</td><td>Charlie</td><td>USA</td></tr>
            </table>
        </div>
    </div>
</body>
</html>
'''

form_result_html = '''
<!DOCTYPE html>
<html>
<head><title>Form Submitted</title></head>
<body>
    <h2>Form Submission Result</h2>
    <p>You entered: <strong>{{ name }}</strong></p>
    <a href="/">Back to Home</a>
</body>
</html>
'''

iframe_html = '''
<!DOCTYPE html>
<html>
<head><title>Iframe Content</title></head>
<body>
    <p>This is content inside the iframe.</p>
    <input type="text" id="iframeInput" placeholder="Input in iframe">
</body>
</html>
'''

popup_html = '''
<!DOCTYPE html>
<html>
<head><title>Popup Page</title></head>
<body>
    <h2>This is a new popup page.</h2>
    <p>You can use this page to test window switching.</p>
    <button onclick="window.close()">Close Window</button>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(main_html)

@app.route('/form-page', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        name = request.form.get('text1', '')
        return render_template_string(form_result_html, name=name)
    return "<p>Access this page via the form on the home page.</p><a href='/'>Back</a>"

@app.route('/iframe-page')
def iframe():
    return render_template_string(iframe_html)

@app.route('/popup-page')
def popup():
    return render_template_string(popup_html)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
