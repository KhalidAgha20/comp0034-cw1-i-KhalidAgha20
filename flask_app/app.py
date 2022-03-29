from flask_app import create_app, config

app = create_app(config.DevelopmentConfig)


@app.route('/')
def hw():
    return 'jknj'


if __name__ == '__main__':
    app.run()
