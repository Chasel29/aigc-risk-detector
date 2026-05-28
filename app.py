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
        "cases": 58,
        "surveys": 632,
        "interviews": 26,
        "frameworks": 4,
        "update_time": datetime.now().strftime("%Y-%m-%d")
    }

    # 典型案例展示
    case_library = [
        {
            "title": "Midjourney版权争议案例",
            "type": "AI图像生成",
            "risk": "中风险",
            "issue": "作品独创性认定",
            "view": "需结合人工修改程度综合判断"
        },
        {
            "title": "ChatGPT辅助写作案例",
            "type": "文本生成",
            "risk": "低风险",
            "issue": "人类创作主导性",
            "view": "AI主要承担辅助生成功能"
        },
        {
            "title": "AI仿风格生成案例",
            "type": "风格模仿生成",
            "risk": "高风险",
            "issue": "潜在侵权与商业传播风险",
            "view": "需加强平台审核与版权风险提示"
        },
        {
            "title": "AI音乐生成案例",
            "type": "AIGC音频生成",
            "risk": "中风险",
            "issue": "训练数据合规性",
            "view": "需进一步明确平台责任边界"
        }
    ]

    # 风险场景展示
    risk_scenarios = [
        {
            "level": "低风险",
            "scene": "AI辅助润色与资料整理",
            "description": "人工创作占主导，AI主要承担辅助优化功能"
        },
        {
            "level": "中风险",
            "scene": "AI生成海报与自媒体内容",
            "description": "存在一定原创表达，但训练数据来源可能存在争议"
        },
        {
            "level": "高风险",
            "scene": "AI批量商业化内容生成",
            "description": "自动生成程度较高，存在较明显版权风险"
        }
    ]

    # 可视化演示数据
    chart_data = {
        "groups": ["普通用户", "内容创作者", "法学相关群体", "AIGC高频使用者"],
        "copyright_support": [48, 67, 72, 61],
        "governance_labels": ["平台审核", "AI标识", "法律规制", "行业标准"],
        "governance_values": [32, 24, 28, 16],
        "dimension_labels": [
            "Human Participation",
            "Originality",
            "AI Dependency",
            "Expression Complexity"
        ],
        "dimension_values": [82, 74, 61, 69]
    }

    if request.method == 'POST':

        text = request.form['content']

        # AIGC认知研究辅助分析模块

        creation_mode = "Human–AI Collaborative Creation"
        prompt_creativity = "中等"
        judicial_tendency = "存在争议"

        # 四维版权认定模型

        # 初始化匹配变量（避免未赋值报错）
        human_match = 0
        originality_match = 0
        ai_match = 0
        complexity_match = 0

        human_keywords = [
            "修改", "设计", "原创", "优化",
            "多轮", "调整", "重构", "人工",
            "反复修改", "草图", "构思", "策划",
            "导演", "拍摄", "后期", "编排",
            "创作", "打磨", "润色", "训练",
            "photoshop", "editing", "manual",
            "post-edit", "post-editing",
            "multi-round", "prompt engineering",
            "human creator", "redraw",
            "creative direction"
        ]

        originality_keywords = [
            "独特", "创新", "个性化",
            "创意", "原创表达", "世界观",
            "角色设定", "叙事", "镜头语言",
            "情绪表达", "视觉风格", "美学",
            "故事结构", "艺术表达",
            "original", "cinematic",
            "architecture composition",
            "worldbuilding", "visual storytelling",
            "concept art", "creative"
        ]

        ai_keywords = [
            "ChatGPT", "Midjourney", "AI生成",
            "AIGC", "自动生成", "Stable Diffusion",
            "Claude", "Gemini", "文心一言",
            "一键生成", "直接生成", "AI完成",
            "无需修改", "自动创作",
            "fully generated", "automatic",
            "one click", "without editing"
        ]

        complexity_keywords = [
            "结构", "故事", "视觉设计",
            "交互", "世界观", "品牌体系",
            "角色设定", "叙事", "镜头语言",
            "多层", "复杂", "系统化",
            "人物关系", "时间线", "空间设计",
            "architecture", "cinematic lighting",
            "visual storytelling", "scene design",
            "composition", "conceptual"
        ]

        # 基础分（避免大部分案例出现极低分）
        base_score = 55

        # 创作特征缓存
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

        human_score = min(100, 25 + human_match * 10)
        originality_score = min(100, 20 + originality_match * 10)
        ai_score = min(100, ai_match * 12)
        complexity_score = min(100, 15 + complexity_match * 8)

        detected_dimensions.extend(human_detected)
        detected_dimensions.extend(originality_detected)
        detected_dimensions.extend(ai_detected)
        detected_dimensions.extend(complexity_detected)

        # Prompt创造性分析
        high_prompt_keywords = [
            "赛博朋克", "水墨", "未来", "电影感",
            "蒸汽朋克", "废土", "东方幻想",
            "赛博神话", "意识流", "超现实",
            "cyberpunk", "cinematic", "original architecture",
            "multi-round", "prompt engineering",
            "post-editing", "photoshop",
            "worldbuilding", "visual storytelling"
        ]

        high_prompt_match, _ = semantic_match(high_prompt_keywords, text)

        if high_prompt_match >= 2:
            prompt_creativity = "较高"
        elif high_prompt_match >= 1:
            prompt_creativity = "中等偏高"
        else:
            prompt_creativity = "基础"

        if "多轮" in text or "人工修改" in text or "重构" in text:
            creation_mode = "Deep Human–AI Collaborative Creation"

        # 研究性司法倾向模拟（仅用于案例研究展示）
        if human_score >= 50 and originality_score >= 40 and complexity_score >= 30:
            judicial_tendency = "倾向认可作品属性"

        elif ai_score >= 60 and human_score <= 20:
            judicial_tendency = "倾向不认可完全版权"

        else:
            judicial_tendency = "存在法律争议"

        # 可版权性综合计算（研究型辅助分析）
        copyright_score = (
            base_score +
            human_score * 0.22 +
            originality_score * 0.22 +
            complexity_score * 0.16 -
            ai_score * 0.08
        )

        # 人工深度参与额外加分
        deep_human_keywords = [
            "photoshop", "multi-round", "人工修改",
            "post-editing", "prompt engineering",
            "原创", "重构"
        ]

        bonus = 0

        for word in deep_human_keywords:
            if word.lower() in text.lower():
                bonus += 4

        copyright_score += bonus

        copyright_score = int(max(15, min(copyright_score, 95)))

        # 研究参考等级判断
        if copyright_score >= 80:
            copyright_level = "高独创性协同创作"
            icon = "🟢"
            legal_opinion = "该内容体现出较强的人类创造性投入与表达控制能力，具有较明显的人机协同创作特征。"

        elif copyright_score >= 60:
            copyright_level = "中等独创性表达"
            icon = "🟠"
            legal_opinion = "该内容存在一定原创表达与人工参与，但AI生成成分相对较高，相关权利认定仍存在争议。"

        else:
            copyright_level = "高度AI生成倾向"
            icon = "🔴"
            legal_opinion = "该内容对AIGC生成依赖程度较高，人类独创性表达相对有限。"

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
            "human": max(20, min(human_score, 100)),
            "originality": max(20, min(originality_score, 100)),
            "ai_dependency": max(15, min(ai_score, 100)),
            "complexity": max(20, min(complexity_score, 100))
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
{icon} AIGC Copyrightability Research Analysis

━━━━━━━━━━━━━━━
Research Risk Level
━━━━━━━━━━━━━━━

{copyright_level}
综合分析指数：{copyright_score}/100

━━━━━━━━━━━━━━━
TRG Four-Dimensional Framework
━━━━━━━━━━━━━━━

Human Participation Index：{human_level}
Original Expression Index：{originality_level}
AI Dependency Index：{ai_level}
Expression Complexity：{complexity_level}

Human Participation Score：{analysis_dimensions['human']}/100
Originality Score：{analysis_dimensions['originality']}/100
AI Dependency Score：{analysis_dimensions['ai_dependency']}/100
Complexity Score：{analysis_dimensions['complexity']}/100

━━━━━━━━━━━━━━━
Creative Process Analysis
━━━━━━━━━━━━━━━
Research Confidence Level：Experimental Research Reference

创作模式：{creation_mode}
Prompt创造性：{prompt_creativity}
司法认知倾向：{judicial_tendency}

━━━━━━━━━━━━━━━
Detected Creative Features
━━━━━━━━━━━━━━━

{detected_text}

━━━━━━━━━━━━━━━
Related Case References
━━━━━━━━━━━━━━━

- {matched_cases[0]}
- {matched_cases[-1]}

━━━━━━━━━━━━━━━
Governance Suggestions
━━━━━━━━━━━━━━━

- {governance_suggestions[0]}
- {governance_suggestions[1]}
- {governance_suggestions[2]}

━━━━━━━━━━━━━━━
Research Observation
━━━━━━━━━━━━━━━

{legal_opinion}

━━━━━━━━━━━━━━━
Global Governance Trends
━━━━━━━━━━━━━━━

China: Emphasizes human intellectual contribution and originality
United States: Tends not to protect fully AI-generated content
European Union: Focuses on creator control and collaborative process
Japan: Exploring emerging copyright rules for the AIGC era

━━━━━━━━━━━━━━━
Platform Statement
━━━━━━━━━━━━━━━

This platform is an experimental research and visualization module
for AIGC copyrightability analysis and governance studies.
All analysis results are for academic research reference only
and do not constitute formal legal opinions.
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