from flask import Flask
from flask import send_file
from io import BytesIO
from flask import request
from clippy.clippy import get_img
from forms import TextForm
from flask import render_template
from flask_wtf.csrf import CSRFProtect
try:
    from keys import SECRET_KEY
except Exception as exc:
    print("You need to supply a secret key for the app")
    import sys
    sys.exit(1)

app = Flask(__name__)
app.secret_key = SECRET_KEY
csrf = CSRFProtect(app)


def serve_pil(img):
    img_io = BytesIO()
    img.save(img_io, "PNG", quality=100)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


@app.route('/', methods=['GET'])
def hello_world():
    form = TextForm(request.args, csrf_enabled=False)
    if not form.validate():
        return render_template("text_form.html", form=form)
    else:
        return generate(form.text.data)


@app.route('/', methods=['POST'])
def generate(text="You need to supply a text!!!"):
    img = get_img(text)
    return serve_pil(img)


if __name__ == '__main__':
    app.run()
