from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    result = ""

    if request.method == 'POST':

        text = request.form['content']

        high_risk_words = ["复刻", "照搬", "完全一致"]

        medium_risk_words = ["模仿", "类似", "参考"]

        result = ""

        for word in high_risk_words:
            if word in text:
                result = f"""
                🔴 风险等级：高风险

                检测到高风险词汇：{word}

                该内容可能涉及直接复制、
                风格侵权或版权风险。
                """
                break

        if result == "":

            for word in medium_risk_words:
                if word in text:
                    result = f"""
                    🟠 风险等级：中风险

                    检测到敏感表达：{word}

                    建议避免直接模仿品牌、
                    作者或商业内容风格。
                    """
                    break

        if result == "":
            result = """
            🟢 风险等级：低风险

            未检测到明显风险内容。
            """

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)