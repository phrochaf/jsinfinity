from flask import Flask, render_template, redirect, url_for, request, session, g
import secrets
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Altere para uma chave secreta forte

# Configurações do MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'wayne_security'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)



@app.before_request
def before_request():
    g.nonce = secrets.token_urlsafe(16)  # Gera um nonce seguro para cada requisição

@app.after_request
def apply_csp(response):
    response.headers['Content-Security-Policy'] = (
        f"default-src 'self'; "
        f"style-src 'self' 'nonce-{g.nonce}' https://fonts.googleapis.com; "
        f"font-src 'self' https://fonts.gstatic.com; "
        f"script-src 'self' 'nonce-{g.nonce}' https://cdn.jsdelivr.net;"
        "default-src 'self'; "
        "style-src 'self' https://fonts.googleapis.com; "  # Permite CSS do Google Fonts
        "font-src 'self' https://fonts.gstatic.com; "  # Permite fontes do Google Fonts
        "script-src 'self' https://cdn.jsdelivr.net; "  # Permite scripts de fontes confiáveis
    )
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index_html():
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verifica no banco de dados
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()

        # Verifica se o usuário existe e a senha está correta
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            session['role'] = user['role']  # Armazena o papel do usuário na sessão

            # Redireciona para o dashboard correto baseado no papel do usuário
            if user['role'] == 'employee':
                return redirect(url_for('employee_dashboard'))
            elif user['role'] == 'manager':
                return redirect(url_for('manager_dashboard'))
            elif user['role'] == 'security_admin':
                return redirect(url_for('security_admin_dashboard'))
        else:
            return "Usuário ou senha inválidos", 401

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')  # Novo campo

        if not username or not password or not role:
            return "Todos os campos são obrigatórios.", 400

        hashed_password = generate_password_hash(password)

        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (username, hashed_password, role))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('login'))
        except Exception as e:
            print(f"Erro ao registrar usuário: {e}")
            return "Erro ao registrar usuário. O nome de usuário pode já estar em uso.", 400

    return render_template('register.html')

@app.route('/employee_dashboard')
def employee_dashboard():
    if 'username' in session and session['role'] == 'employee':
        return render_template('employee_dashboard.html', username=session['username'])
    return redirect(url_for('login'))

# Página para gerentes
@app.route('/manager_dashboard')
def manager_dashboard():
    if 'username' in session and session['role'] == 'manager':
        return render_template('manager_dashboard.html', username=session['username'])
    return redirect(url_for('login'))

# Página para administradores de segurança
@app.route('/security_admin_dashboard')
def security_admin_dashboard():
    if 'username' in session and session['role'] == 'security_admin':
        # Exemplo de dados para o gráfico
        cur = mysql.connection.cursor()
        cur.execute("SELECT description, COUNT(*) as count FROM resources GROUP BY description")
        data = cur.fetchall()
        cur.close()

        labels = [item['description'] for item in data]
        counts = [item['count'] for item in data]

        chart_data = {
            'labels': labels,
            'datasets': [{
                'label': 'Recursos por Tipo',
                'data': counts,
                'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1
            }]
        }

        return render_template('security_admin_dashboard.html', username=session['username'], chart_data=chart_data)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/resources')
def resources():
    if 'username' in session and session['role'] == 'security_admin':
        # Obter lista de recursos do banco de dados
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM resources")
        resources = cur.fetchall()
        cur.close()
        return render_template('resources.html', resources=resources)
    return redirect(url_for('login'))

@app.route('/view_resources')
def view_resources():
    alert = request.args.get('alert')  # Captura o alerta, se existir

    if 'username' in session:
        cur = mysql.connection.cursor()
        
        # Obter todos os recursos para a tabela
        cur.execute("SELECT * FROM resources")
        resources = cur.fetchall()
        
        # Obter soma de quantidades por descrição para o gráfico
        cur.execute("""
            SELECT description, SUM(quantity) as total_quantity
            FROM resources
            GROUP BY description
        """)
        resource_counts = cur.fetchall()
        
        cur.close()

        # Preparar os dados para o gráfico
        labels = [resource['description'] for resource in resource_counts]
        counts = [resource['total_quantity'] for resource in resource_counts]  # Usar a soma das quantidades

        role = session.get('role')
        return render_template('view_resources.html', resources=resources, role=role, labels=labels, counts=counts, alert=alert)

    return redirect(url_for('login'))

@app.route('/register_resource', methods=['GET', 'POST'])
def register_resource():
    if 'username' not in session or session['role'] not in ['manager', 'security_admin']:
        return redirect(url_for('view_resources', alert="Você não tem permissão para registrar recursos."))
    
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        quantity = request.form['quantity']
        description = request.form['description']
        status = request.form['status']

        # Inserir recurso no banco de dados
        cur = mysql.connection.cursor()
        try:
            cur.execute(
                "INSERT INTO resources (name, location, quantity, description, status) VALUES (%s, %s, %s, %s, %s)",
                (name, location, quantity, description, status)
            )
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('view_resources'))
        except Exception as e:
            return f"Erro ao registrar recurso: {str(e)}", 400

    return render_template('register_resource.html')

@app.route('/edit_resource/<int:resource_id>', methods=['GET', 'POST'])
def edit_resource(resource_id):
    cur = mysql.connection.cursor()
    
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        quantity = request.form['quantity']
        description = request.form['description']
        status = request.form['status']

        # Atualiza o recurso no banco de dados
        cur.execute("""
            UPDATE resources
            SET name = %s, location = %s, quantity = %s, description = %s, status = %s
            WHERE id = %s
        """, (name, location, quantity, description, status, resource_id))

        mysql.connection.commit()
        cur.close()
        return redirect(url_for('view_resources'))

    # Busca o recurso a ser editado
    cur.execute("SELECT * FROM resources WHERE id = %s", (resource_id,))
    resource = cur.fetchone()
    cur.close()
    
    return render_template('edit_resource.html', resource=resource)


@app.route('/delete_resource/<int:resource_id>', methods=['POST'])
def delete_resource(resource_id):
    if 'username' in session:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM resources WHERE id = %s", (resource_id,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('view_resources'))
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)
