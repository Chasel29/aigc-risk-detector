from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    result = ""
    copyright_score = 0
    copyright_level = ""
    analysis_dimensions = {}
    matched_cases = []
    governance_suggestions = []

    # 平台演示数据（用于研究展示与可视化）
    platform_stats = {
        "cases": 52,
        "surveys": 632,
        "interviews": 26,
        "update_time": datetime.now().strftime("%Y-%m-%d")
    }

    # 典型案例展示
    case_library = [
        {
            "title": "AI绘画著作权争议案例",
            "type": "AI图像生成",
            "risk": "中风险",
            "issue": "作品独创性认定",
            "view": "需结合人工修改程度综合判断"
        },
        {
            "title": "AI辅助文案创作案例",
            "type": "文本生成",
            "risk": "低风险",
            "issue": "AI辅助创作边界",
            "view": "人类创作主导性较明显"
        },
        {
            "title": "仿风格AI生成内容案例",
            "type": "风格模仿生成",
            "risk": "高风险",
            "issue": "潜在侵权与商业传播风险",
            "view": "需加强平台审核与版权提示"
        }
    ]

    # 风险场景展示
    risk_scenarios = [
        {
            "level": "低风险",
            "scene": "AI辅助润色与资料整理",
            "description": "人工创作占主导，AI主要用于辅助优化"
        },
        {
            "level": "中风险",
            "scene": "AI生成海报与自媒体内容",
            "description": "存在一定原创表达，但训练数据来源可能存在争议"
        },
        {
            "level": "高风险",
            "scene": "AI批量生成商业化内容",
            "description": "自动生成程度较高，商业传播风险较明显"
        }
    ]

    # 可视化演示数据
    chart_data = {
        "groups": ["普通用户", "内容创作者", "法学相关群体", "AIGC高频使用者"],
        "copyright_support": [48, 67, 72, 61],
        "governance_labels": ["平台审核", "AI标识", "法律规制", "行业标准"],
        "governance_values": [32, 24, 28, 16]
    }

    if request.method == 'POST':

        text = request.form['content']

        # AIGC认知研究辅助分析模块

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

        # 研究性司法倾向模拟（仅用于案例研究展示）
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

        # 研究参考等级判断
        if copyright_score >= 70:
            copyright_level = "低版权争议倾向"
            icon = "🟢"
            legal_opinion = "该内容体现出较明显的人类创造性投入，具备较强的人类主导创作特征。"

        elif copyright_score >= 40:
            copyright_level = "中版权争议倾向"
            icon = "🟠"
            legal_opinion = "该内容存在一定原创表达，但AI参与程度较高，相关权利归属仍存在一定争议。"

        else:
            copyright_level = "高版权争议倾向"
            icon = "🔴"
            legal_opinion = "该内容主要依赖AIGC生成，人类独创性表达相对有限。"

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

        analysis_dimensions = {
            "human": min(human_score, 100),
            "originality": min(originality_score, 100),
            "ai_dependency": min(ai_score, 100),
            "complexity": min(complexity_score, 100)
        }

        if detected_dimensions:
            detected_text = ", ".join(detected_dimensions)
        else:
            detected_text = "未检测到明显创作特征"

        # 相似案例推荐
        if "Midjourney" in text or "AI绘画" in text:
            matched_cases.append("AI绘画著作权争议案例")

        if "文案" in text or "ChatGPT" in text:
            matched_cases.append("AI辅助文案创作案例")

        if "风格" in text or "模仿" in text:
            matched_cases.append("仿风格AI生成内容案例")

        if not matched_cases:
            matched_cases = [
                "AIGC内容版权认知案例",
                "平台治理与风险识别案例"
            ]

        # 治理建议
        governance_suggestions = [
            "建议明确标注AI参与程度",
            "建议保留创作过程记录与修改痕迹",
            "商业传播前建议增加版权风险审核"
        ]

        result = f"""
{icon} AIGC知识产权研究辅助分析结果

━━━━━━━━━━━━━━━
研究参考等级
━━━━━━━━━━━━━━━

{copyright_level}
综合分析指数：{copyright_score}/100

━━━━━━━━━━━━━━━
四维研究分析框架
━━━━━━━━━━━━━━━

人类参与度：{human_level}
独创性表达：{originality_level}
AI依赖程度：{ai_level}
表达复杂度：{complexity_level}

━━━━━━━━━━━━━━━
创作行为分析
━━━━━━━━━━━━━━━

创作模式：{creation_mode}
Prompt创造性：{prompt_creativity}
司法认知倾向：{judicial_tendency}

━━━━━━━━━━━━━━━
关键创作特征
━━━━━━━━━━━━━━━

{detected_text}

━━━━━━━━━━━━━━━
相似案例参考
━━━━━━━━━━━━━━━

- {matched_cases[0]}
- {matched_cases[-1]}

━━━━━━━━━━━━━━━
治理建议参考
━━━━━━━━━━━━━━━

- {governance_suggestions[0]}
- {governance_suggestions[1]}
- {governance_suggestions[2]}

━━━━━━━━━━━━━━━
研究参考意见
━━━━━━━━━━━━━━━

{legal_opinion}

━━━━━━━━━━━━━━━
国际治理趋势参考
━━━━━━━━━━━━━━━

中国：强调“人类智力投入”与独创性表达
美国：倾向不保护纯AI自动生成内容
欧盟：强调创作者控制力与人机协同过程
日本：逐步探索AIGC时代的新型版权规则

━━━━━━━━━━━━━━━
平台说明
━━━━━━━━━━━━━━━

本平台为“AIGC知识产权研究与辅助分析平台”演示模块，
主要用于案例研究、认知分析与可视化展示。
平台结果仅作为研究参考，不构成正式法律认定意见。
        """

    return render_template(
        'index.html',
        result=result,
        score=copyright_score,
        risk_level=copyright_level,
        dimensions=analysis_dimensions,
        matched_cases=matched_cases,
        governance_suggestions=governance_suggestions,
        stats=platform_stats,
        cases=case_library,
        risks=risk_scenarios,
        charts=chart_data
    )

if __name__ == '__main__':
    app.run(debug=True)