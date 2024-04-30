from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', output=None)

@app.route('/run', methods=['POST'])
def run_program():
    code = request.form['code']
    input_data = request.form['input_data']
    
    # 将代码保存到文件中
    with open('temp/temp.cpp', 'w') as f:
        f.write(code)
    
    # 将输入数据保存到文件中
    with open('temp/input.txt', 'w') as f:
        f.write(input_data)
    
    # 使用 subprocess 执行 g++ 编译代码
    compile_process = subprocess.Popen(['g++', 'temp/temp.cpp', '-o', 'temp/temp'], stderr=subprocess.PIPE)
    compile_output, compile_error = compile_process.communicate()
    
    # 如果编译错误，则返回编译错误信息
    if compile_error:
        return jsonify({'status': 'error', 'error': compile_error.decode('utf-8')})
    
    # 执行编译后的可执行文件，并将输入数据从 input.txt 重定向到标准输入，将输出结果重定向到 output.txt
    with open('temp/input.txt', 'r') as input_file:
        with open('temp/output.txt', 'w') as output_file:
            run_process = subprocess.Popen(['./temp/temp'], stdin=input_file, stdout=output_file)
            run_process.communicate()
    
    # 读取程序输出结果文件内容
    with open('temp/output.txt', 'r') as f:
        output = f.read()
    
    return jsonify({'status': 'success', 'output': output})

if __name__ == '__main__':
    app.run(debug=True)
