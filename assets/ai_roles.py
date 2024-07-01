from assets.w_examples import W_Criteria, W_Examples


ielts_w_score_format = '''
打分格式以JSON格式书写
其中包含“Task Response”,"Coherence and Cohesion","Lexical Resource","Grammatical Range and Accuracy"4个key，是评分的4个标准;
每个key后面跟随的value是一个List，该list第一个值是对应key标准下的分值，作为float;List第二个数据是str类型，写出对应key标准下的简要分析。
'''



class AIroles:
    professional_IELTS_teacher = "professional_IELTS_teacher"

    Ielts_teacher = {
        "assistant的身份": "一个专业的雅思老师",
        "雅思作文评判标准": W_Criteria.criteria,
        "雅思part2例文库": {
            "9分": [W_Examples.part2_9_01],
            "7.5分": [W_Examples.part2_7_01],
            "6分": [W_Examples.part2_6_01]
        },
        "雅思作文打分格式": ielts_w_score_format,
        "雅思作文打分格式例子": W_Criteria.score_format
    }

    ai_role = {
        "professional_IELTS_teacher": Ielts_teacher,
    }