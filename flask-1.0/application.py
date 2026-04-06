from flask import Flask

application = Flask(__name__)

@application.route('/')
def home():
    return "Hello from Flask on AWS Elastic Beanstalk 4.7.0!"

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)

