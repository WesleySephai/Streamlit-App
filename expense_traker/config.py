class Config:
    SECRET_KEY = 'your-secret-key'  # You can replace this with a real secret
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:wesleywes@localhost/expense_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False