from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    result = ""
    copyright_score = 0
    copyright_level = ""

    if request.method == 'POST':

        text = request.form['content']

        # 创新分析模块

        creation_mode = "人机协同创作"
        prompt_creativity = "中等"
        judicial_tendency = "存在争议"

        # 四维版权认定模型

        human_keywords = [
            "修改", "设计", "原创", "优化",
            "多轮", "调整", "重构", "人工",
            "反复修改", "草图", "构思", "策划",
            "导演", "拍摄", "后期", "编排",
            "创作", "打磨", "润色", "训练"
        ]

        originality_keywords = [
            "独特", "创新", "个性化",
            "创意", "原创表达", "世界观",
            "角色设定", "叙事", "镜头语言",
            "情绪表达", "视觉风格", "美学",
            "故事结构", "艺术表达"
        ]

        ai_keywords = [
            "ChatGPT", "Midjourney", "AI生成",
            "AIGC", "自动生成", "Stable Diffusion",
            "Claude", "Gemini", "文心一言",
            "一键生成", "直接生成", "AI完成",
            "无需修改", "自动创作"
        ]

        complexity_keywords = [
            "结构", "故事", "视觉设计",
            "交互", "世界观", "品牌体系",
            "角色设定", "叙事", "镜头语言",
            "多层", "复杂", "系统化",
            "人物关系", "时间线", "空间设计"
        ]

        human_score = 0
        originality_score = 0
        ai_score = 0
        complexity_score = 0

        detected_dimensions = []

        # 智能语义识别函数
        def semantic_match(keyword_group, content):
            score = 0
            matched = []

            for word in keyword_group:
                if word.lower() in content.lower():
                    score += 1
                    matched.append(word)

            return score, matched

        # 智能语义分析

        human_match, human_detected = semantic_match(human_keywords, text)
        originality_match, originality_detected = semantic_match(originality_keywords, text)
        ai_match, ai_detected = semantic_match(ai_keywords, text)
        complexity_match, complexity_detected = semantic_match(complexity_keywords, text)

        human_score = human_match * 12
        originality_score = originality_match * 12
        ai_score = ai_match * 15
        complexity_score = complexity_match * 10

        detected_dimensions.extend(human_detected)
        detected_dimensions.extend(originality_detected)
        detected_dimensions.extend(ai_detected)
        detected_dimensions.extend(complexity_detected)

        # Prompt创造性分析
        high_prompt_keywords = [
            "赛博朋克", "水墨", "未来", "电影感",
            "蒸汽朋克", "废土", "东方幻想",
            "赛博神话", "意识流", "超现实"
        ]

        high_prompt_match, _ = semantic_match(high_prompt_keywords, text)

        if high_prompt_match >= 2:
            prompt_creativity = "较高"
        elif high_prompt_match >= 1:
            prompt_creativity = "中等偏高"
        else:
            prompt_creativity = "基础"

        if "多轮" in text or "人工修改" in text or "重构" in text:
            creation_mode = "深度人机协同创作"

        # 模拟司法认定倾向
        if human_score >= 50 and originality_score >= 40 and complexity_score >= 30:
            judicial_tendency = "倾向认可作品属性"

        elif ai_score >= 60 and human_score <= 20:
            judicial_tendency = "倾向不认可完全版权"

        else:
            judicial_tendency = "存在法律争议"

        # 可版权性综合计算
        copyright_score = (
            human_score * 0.35 +
            originality_score * 0.35 +
            complexity_score * 0.2 -
            ai_score * 0.1
        )

        copyright_score = int(max(0, min(copyright_score, 100)))

        # 版权等级判断
        if copyright_score >= 70:
            copyright_level = "较高可版权性"
            icon = "🟢"
            legal_opinion = "该内容体现出较明显的人类创造性投入，可能具备作品属性。"

        elif copyright_score >= 40:
            copyright_level = "存在争议"
            icon = "🟠"
            legal_opinion = "该内容存在一定原创表达，但AI参与程度较高，权利归属仍存在争议。"

        else:
            copyright_level = "较低可版权性"
            icon = "🔴"
            legal_opinion = "该内容主要依赖AIGC生成，人类独创性表达有限。"

        # 维度等级分析
        def level_text(score):
            if score >= 60:
                return "较高"
            elif score >= 30:
                return "中等"
            else:
                return "较低"

        human_level = level_text(human_score)
        originality_level = level_text(originality_score)
        ai_level = level_text(ai_score)
        complexity_level = level_text(complexity_score)

        if detected_dimensions:
            detected_text = ", ".join(detected_dimensions)
        else:
            detected_text = "未检测到明显创作特征"

        result = f"""
{icon} AIGC作品可版权性分析报告

综合认定结果：{copyright_level}
可版权性评分：{copyright_score}/100

━━━━━━━━━━━━━━━
四维版权认定框架
━━━━━━━━━━━━━━━

人类参与度：{human_level}
独创性：{originality_level}
AI依赖程度：{ai_level}
表达复杂度：{complexity_level}

━━━━━━━━━━━━━━━
创新分析模块
━━━━━━━━━━━━━━━

创作模式：{creation_mode}
Prompt创造性：{prompt_creativity}
司法认定倾向：{judicial_tendency}

━━━━━━━━━━━━━━━
关键创作特征
━━━━━━━━━━━━━━━

{detected_text}

━━━━━━━━━━━━━━━
模拟法律意见
━━━━━━━━━━━━━━━

{legal_opinion}

━━━━━━━━━━━━━━━
国际版权趋势参考
━━━━━━━━━━━━━━━

中国：强调“人类智力投入”与独创性表达
美国：美国版权局倾向不保护纯AI生成作品
欧盟：强调人机协同创作过程与创作者控制力
日本：逐步探索AIGC时代的新型版权规则

━━━━━━━━━━━━━━━
平台声明
━━━━━━━━━━━━━━━

本平台基于AIGC知识产权认定框架进行辅助分析，
用于学术研究、教学演示与AIGC治理探索，
结果不构成正式法律意见。
        """

    return render_template(
        'index.html',
        result=result,
        score=copyright_score,
        risk_level=copyright_level
    )

if __name__ == '__main__':
    app.run(debug=True)