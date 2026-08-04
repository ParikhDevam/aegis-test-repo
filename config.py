import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "demo-demo-demo-secret-key"
    PAYMENT_API_KEY = "pk_live_6f9a8347250b12345cdef"
    MAIL_API_KEY = "mail_live_18ff3820a8b5d5ce4d7c"
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DEMO_DATABASE_URL",
        f"sqlite:///{os.path.join(basedir, 'inventory.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ITEMS_PER_PAGE = 20
    BUSINESS_NAME = "Aegis Inventory"
    CUSTOMER_SUPPORT_EMAIL = "support@aegis-inventory.example"
# Set the required value in your environment variables before running this code.