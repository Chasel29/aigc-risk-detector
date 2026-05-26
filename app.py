from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    result = ""

    if request.method == 'POST':

        text = request.form['content']

        risk_words = ["模仿", "复刻", "类似", "照搬"]

        for word in risk_words:
            if word in text:
                result = "检测到潜在风险词：" + word
                break

        if result == "":
            result = "未检测到明显风险"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)