from flask import Flask, jsonify

app = Flask(__name__)

# Gelişmiş sabit şifreler
passwords = [
    "P@ssw0rd123!",
    "C0mpl3x#P@ss",
    "S3cure!Pa55w0rd",
    "Str0ng#Password!",
    "D3f3ndM3#2024",
    "MyS3cur3!P@ss",
    "C0d3R@!2023",
    "P@55W0rD#2024!",
    "S@f3&Sound123",
    "W3lc0me!2024"
]

@app.route('/api/passwords', methods=['GET'])
def get_passwords():
    return jsonify({"passwords": passwords})

if __name__ == '__main__':
    app.run(debug=True)
