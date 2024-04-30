from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# 用于保存笔记文件的目录
NOTES_FOLDER = 'notes'
app.config['NOTES_FOLDER'] = NOTES_FOLDER

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/notes', methods=['GET', 'POST'])  # 添加了对 POST 请求的支持
def save_or_get_note():
    if request.method == 'POST':
        note = request.json.get('note')

        # 检查笔记是否为空
        if not note:
            return jsonify({'error': '笔记内容为空'})

        # 创建一个名为 note.txt 的文件，并保存笔记内容
        note_file_path = os.path.join(app.config['NOTES_FOLDER'], 'note.txt')
        with open(note_file_path, 'w') as f:
            f.write(note)

        # 返回已保存的消息
        return jsonify({'message': '笔记已保存'})
    else:
        # 获取笔记内容
        note_file_path = os.path.join(app.config['NOTES_FOLDER'], 'note.txt')
        if not os.path.exists(note_file_path):
            return jsonify({'error': '笔记不存在'})

        with open(note_file_path, 'r') as f:
            note = f.read()

        # 返回笔记内容
        return jsonify({'note': note})

if __name__ == '__main__':
    app.run(debug=True)

