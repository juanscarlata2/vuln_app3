from flask import Flask, render_template, request, redirect, url_for, session, render_template_string
from functools import wraps

app = Flask(__name__)
app.secret_key = 'HASHjghg23565!!9787861209jhakskh'
app.run(host='0.0.0.0')

# Decorator function to check if user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            # User is not logged in, redirect to login page
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Dummy function to simulate temperature data retrieval
def get_temperature(server="s3"):

    servers={"s1":34,"s2":56,"s3":57}

    if server not in servers:
        return "N/A","No server"
    else:
        return servers[server], "Server "+server[-1]
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process login form
        username = request.form['username']
        password = request.form['password']
        injections=["'"]
        # Check username and password (you can use a database or a simple check)
        if username == 'admin' and password == 'password':
            # Successful login, store the username in the session
            session['username'] = username
            return redirect(url_for('temperature', server='s1'))
        elif username.find("'") > 0 or password.find("'") > 0:
            error = "You wish these fields were injectable, but they are not."
            return render_template('login.html', error=error)
        else:
            # Invalid credentials, display error message
            error = 'Invalid username or password'
            return render_template('login.html', error=error)
    
    # Render the login form
    return render_template('login.html', error=None)

@app.route('/temperature',methods=['GET', 'POST'])
@login_required
def temperature():
    if request.method == 'POST':
        server = request.form['server']
    else:
        server='s1'
    # Get the temperature data
    temperature_data, server_name = get_temperature(server)
    style='''
    <style>
        body {
            padding: 40px;
        }
        .content-container {
            max-width: 400px;
            margin: 0 auto;
        }
    </style>
    '''

    template=f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Temperature</title>
        <link rel="stylesheet" href="css/bulma.min.css">
        {style}
    </head>
    <body>
        <section class="section">
            <div class="container">
                    <h1 class="title">Temperature</h1>
                    <form action="/temperature" method="POST">
                        <div class="field">
                            <label class="label" for="server">Choose a server:</label>
                            <div class="control">
                                <div class="select">
                                    <select id="server" name="server">
                                        <option value="s1">Server 1</option>
                                        <option value="s2">Server 2</option>
                                        <option value="s3">Server 3</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="field">
                            <div class="control">
                                <button class="button is-primary" type="submit">Get Temperature</button>
                            </div>
                        </div>
                    </form>
                </div>
                <h1 class="title">Temperature on {server_name}</h1>
                <div class="content">
                    <table class="table is-bordered is-fullwidth">
                        <thead>
                            <tr>
                                <th>Server ID</th>
                                <th>Temperature</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td> Col_2345_{server}39_.evilcorp</td>
                                <td>{temperature_data} °C</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <a class="button is-primary" href="/logout">Log out</a>
            </div>
        </section>
    </body>
    </html>

    '''
    # Render the temperature page with the data
    #return render_template('temperature.html', temperature=temperature_data, server=server)
    return render_template_string(template)


@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    
    # Redirect to the login page
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
