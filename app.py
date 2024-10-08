# app.py
import logging

from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS

from services.hello.hello import hello_serivce
from config import conf, setup_logging
from utils.response import make_error_response

app = Flask(__name__) # 创建flask应用
CORS(app) # 支持跨域访问

setup_logging()

logging.info("*******************config info:*******************")
logging.info(conf())

app.register_blueprint(hello_serivce, url_prefix='/api/v1/hello')

# 上传文件
@app.route('/v1/upload', methods=['POST'])
def upload():
    # request.json解析post的json数据
    logging.info(request.json)
    # request.files解析上传的文件
    f = request.files['filename']
    f.save(f'your_path/{f.filename}')
    # jsonify()返回application/json类型的响应
    return jsonify({'message': 'upload success'}) 

# 文件服务器
@app.route('/v1/download/<path:name>')
def download(name):
    return send_from_directory("your_path", name, as_attachment=True)

# 错误处理
@app.errorhandler(Exception)
def error_handler(e):
    return make_error_response(repr(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
