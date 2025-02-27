from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/carousel')
def return_sample_page():
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet">
    <title>Слайдшоу</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  </head>
  <body class="p-3 m-0 border-0 bd-example m-0 border-0">




    <div id="carouselExampleIndicators" class="carousel slide">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Слайд 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Слайд 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Слайд 3"></button>
      </div>
      <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="{url_for('static', filename='img/1.jpg')}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='img/2.jpg')}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='img/3.jpg')}" class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden"><ya-tr-span data-index="129-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Previous" data-translation="Предыдущая страница" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Предыдущая страница</ya-tr-span></span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden"><ya-tr-span data-index="129-1" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Next" data-translation="Далее" data-ch="0" data-type="trSpan" style="visibility: inherit !important;">Далее</ya-tr-span></span>
      </button>
    </div>



  </body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
