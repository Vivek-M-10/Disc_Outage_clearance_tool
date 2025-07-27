from flask import Flask, jsonify
from clearance import remove_old_logs

app = Flask(__name__)

@app.route('/clean', methods=['GET'])
def clean_logs():
    deleted_files = remove_old_logs()
    return jsonify({
        "status": "success",
        "message": f"{len(deleted_files)} files deleted.",
        "files": deleted_files
    })

if __name__ == '__main__':
    app.run()
