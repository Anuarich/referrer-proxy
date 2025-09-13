from flask import Flask, render_template_string

app = Flask(__name__)

fake_referer = "https://www.google.com/search?q=Beach+Road+Pattaya.+Incredible+walk.+Thailand.+September+2025.+Pattaya+Through+My+Eyes.+4K"
target_url = "https://www.youtube.com/watch?v=G1g3KJByCyc"

@app.route('/')
def redirect_with_fake_referer():
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Redirecting...</title>
    <meta name="referrer" content="origin">
    <script>
        history.replaceState(null, '', '{fake_referer}');
        window.location.href = "{target_url}";
    </script>
    </head>
    <body>
    <p>Redirecting to video...</p>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
