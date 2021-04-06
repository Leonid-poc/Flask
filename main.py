from flask import Flask, url_for, request
import os

app = Flask(__name__)

# http://192.168.100.6:8080/
# http://127.0.0.1:8080/
# https://yandex.ru/dev/maps/staticapi/doc/1.x/dg/concepts/markers.html
# {url_for('static', filename='css/style.css')}
# with open('test.html', mode='r', encoding='utf-8') as txt:
#     e = txt.read()


@app.route('/astronaut_selection')
def astronaut_selection():
  return f"""
  

  """

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
