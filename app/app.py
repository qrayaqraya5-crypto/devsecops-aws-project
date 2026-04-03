from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevSecOps AWS Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #0a0e1a;
            color: #ffffff;
            min-height: 100vh;
        }
        .navbar {
            background: #111827;
            padding: 15px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #00d4ff;
        }
        .navbar h1 {
            color: #00d4ff;
            font-size: 22px;
        }
        .status-badge {
            background: #00ff88;
            color: #000;
            padding: 6px 16px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 13px;
        }
        .hero {
            text-align: center;
            padding: 80px 20px 40px;
        }
        .hero h2 {
            font-size: 48px;
            background: linear-gradient(90deg, #00d4ff, #00ff88);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 15px;
        }
        .hero p {
            color: #8892a4;
            font-size: 18px;
        }
        .cards {
            display: flex;
            justify-content: center;
            gap: 25px;
            padding: 40px;
            flex-wrap: wrap;
        }
        .card {
            background: #111827;
            border: 1px solid #1e293b;
            border-radius: 16px;
            padding: 30px;
            width: 220px;
            text-align: center;
            transition: transform 0.3s;
        }
        .card:hover {
            transform: translateY(-8px);
            border-color: #00d4ff;
        }
        .card .icon { font-size: 40px; margin-bottom: 15px; }
        .card h3 { color: #00d4ff; margin-bottom: 8px; font-size: 16px; }
        .card p { color: #8892a4; font-size: 13px; }
        .card .check {
            color: #00ff88;
            font-size: 13px;
            margin-top: 10px;
            font-weight: bold;
        }
        .pipeline {
            background: #111827;
            margin: 0 40px 40px;
            border-radius: 16px;
            padding: 30px;
            border: 1px solid #1e293b;
        }
        .pipeline h3 {
            color: #00d4ff;
            margin-bottom: 20px;
            font-size: 20px;
        }
        .steps {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
        }
        .step {
            background: #1e293b;
            border-radius: 10px;
            padding: 12px 20px;
            text-align: center;
            font-size: 13px;
        }
        .step .label { color: #8892a4; font-size: 11px; }
        .step .name { color: #ffffff; font-weight: bold; }
        .arrow { color: #00d4ff; font-size: 20px; }
        .footer {
            text-align: center;
            padding: 30px;
            color: #8892a4;
            font-size: 13px;
            border-top: 1px solid #1e293b;
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <h1>🔐 DevSecOps Dashboard</h1>
        <span class="status-badge">● RUNNING</span>
    </nav>

    <div class="hero">
        <h2>DevSecOps sur AWS</h2>
        <p>Pipeline CI/CD sécurisé avec GitHub Actions • Docker • Terraform</p>
    </div>

    <div class="cards">
        <div class="card">
            <div class="icon">🐍</div>
            <h3>Python Flask</h3>
            <p>Backend API REST</p>
            <div class="check">✅ Actif</div>
        </div>
        <div class="card">
            <div class="icon">🐳</div>
            <h3>Docker</h3>
            <p>Containerisation</p>
            <div class="check">✅ Actif</div>
        </div>
        <div class="card">
            <div class="icon">🔍</div>
            <h3>Bandit</h3>
            <p>SAST Security Scan</p>
            <div class="check">✅ Configuré</div>
        </div>
        <div class="card">
            <div class="icon">☁️</div>
            <h3>AWS</h3>
            <p>Cloud Deployment</p>
            <div class="check">⏳ En cours</div>
        </div>
        <div class="card">
            <div class="icon">📊</div>
            <h3>Monitoring</h3>
            <p>CloudWatch + SNS</p>
            <div class="check">⏳ En cours</div>
        </div>
    </div>

    <div class="pipeline">
        <h3>🚀 Pipeline CI/CD DevSecOps</h3>
        <div class="steps">
            <div class="step">
                <div class="label">Source</div>
                <div class="name">GitHub</div>
            </div>
            <div class="arrow">→</div>
            <div class="step">
                <div class="label">Scan Code</div>
                <div class="name">Bandit</div>
            </div>
            <div class="arrow">→</div>
            <div class="step">
                <div class="label">Scan Docker</div>
                <div class="name">Trivy</div>
            </div>
            <div class="arrow">→</div>
            <div class="step">
                <div class="label">Scan IaC</div>
                <div class="name">Checkov</div>
            </div>
            <div class="arrow">→</div>
            <div class="step">
                <div class="label">Deploy</div>
                <div class="name">AWS EC2</div>
            </div>
        </div>
    </div>

    <div class="footer">
        Projet DevSecOps — Khalil | AWS • Docker • GitHub Actions • Terraform
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'version': '1.0.0'})

@app.route('/api/status')
def status():
    return jsonify({
        'app': 'running',
        'docker': 'active',
        'security': 'enabled'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
