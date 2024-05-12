# app.py
from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS

app = Flask(__name__) # 创建flask应用
CORS(app) # 支持跨域访问

# 默认为get请求
@app.route('/hello')
def hello():
    return 'hello world' # 返回text/html类型响应，是一个html文件，<body>hello world</body>

# 上传文件
@app.route('/upload', methods=['POST'])
def upload():
    # request.json解析post的json数据
    print(request.json)
    # request.files解析上传的文件
    f = request.files['filename']
    f.save(f'your_path/{f.filename}')
    # jsonify()返回application/json类型的响应
    return jsonify({'message': 'upload success'}) 

# 文件服务器
@app.route('/download/<path:name>')
def download(name):
    return send_from_directory("your_path", name, as_attachment=True)

# 错误处理
@app.errorhandler(Exception)
def error_handler(e):
    return jsonify({'error': repr(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
