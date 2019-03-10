from flask import Flask, render_template


app = Flask(__name__)

films_pic = ['static/test_picture.jpg', 'static/test_picture.jpg', 'static/test_picture.jpg']
for i in range(20):
    films_pic.append('static/test_picture.jpg')

films = []
texts_backgrounds = []
film = ''
top = 0
for i in range(len(films_pic)):
    top += 320
    film += 'background-image: url(' + films_pic[i] + '); '
    film += 'border-radius: 20px; '
    film += 'width: 200px; '
    film += 'height: 300px; '
    film += 'position: absolute; '
    film += 'left: 200px; '
    film += 'top: ' + str(top) + 'px;'
    film += 'border-color: Green'
    films.append(film)
    film = ''
    texts_backgrounds.append('position: absolute; ' + 'top: ' + str(top) +
                             'px; width: 800px; ' + ' height: 300px; ' + 'left: 410px; '
                             + 'border-radius: 20px')


@app.route('/')
@app.route('/hello')
def pics():
    return render_template('test_1.html', films=films, texts_backgrounds=texts_backgrounds)


if __name__ == '__main__':
    app.run(debug=True)
