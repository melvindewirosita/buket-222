from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get('mongodb+srv://dewiiroosita12:melvindr@cluster0.ek1gznh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
DB_NAME =  os.environ.get('melvindr')

client = MongoClient('mongodb+srv://dewiiroosita12:melvindr@cluster0.ek1gznh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
