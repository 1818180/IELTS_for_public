import sys
import re

sys.path.append('.')

from assets.sort_tool import SortingTXT, StyleTXT
from assets.w_examples import W_Examples, W_Criteria, W_Test
from ai_response.deepseek_response import get_ds_1answer
from ai_response.gemini_responce import get_gm_1answer

class AImodel:
    ds = "deepseek"
    gm_pro = "gemini-pro"
    gm_flash = "gemini-1.5-flash"
    gm_pro_new = "gemini-1.5-pro"
    models = [ds, gm_pro, gm_flash, gm_pro_new]

class AIprompt:
    def submit_question_to_AI(question: str, ai_model: str):
        if ai_model == "deepseek":
            answer_part2 = get_ds_1answer(question)
            return answer_part2
        else:
            answer_part2 = get_gm_1answer(question, ai_model)
            return answer_part2

class AIforWriting(AIprompt):
    # prompt draft ================================================
    modify_slight = '''请你对我的文章用英文进行修改重写，文章大意和句式不变，只改变用词错误、用词不当和语法错误即可
'''
    modify_medium = '''请你对我的文章用英文进行重写, 文章大意不变，可以改变句式，务必使得文章用词正确且专业，语法正确且句式丰富，整体符合雅思写作高分水准，字数控制在原文水平
'''
    modify_high = '''请你根据我提供的文章题目要求，用英文重写一篇文章，不参考我的原文主旨，重新立意，写一篇符合雅思写作高分水准的文章，字数控制在450字以内
'''
    modify_requests = {"slight": modify_slight, "medium": modify_medium, "high": modify_high}
    
    # essay
    @classmethod
    def part2_only_essay(cls, topic, writing, request:str):
        que_2 = f'''
作文主题:
{topic}
\n
我的作文文本：
{writing}
\n
修改要求：
{cls.modify_requests[request]}
=====
直接给出英文即可，不要提供文章外的任何内容
'''
        return que_2
    
    # score & essay
    def part2_question_all(topic, writing):
        ques_2 = f'''
雅思part2评判要求如下:
{W_Criteria.criteria}
\n
这是一篇雅思part2 9分例文:
{W_Examples.part2_9_01}
\n
这是一篇雅思part2 7分例文:
{W_Examples.part2_7_01}
\n
这是一篇雅思part2 7分例文:
{W_Examples.part2_6_01}
\n
=======
这是我的雅思part2作文题目:
{topic}
\n
我的作文文本：
{writing}
\n
请你根据雅思作文评判标准对我的作文进行打分。
打分格式请以JSON格式书写
其中包含“Task Response”,"Coherence and Cohesion","Lexical Resource","Grammatical Range and Accuracy"4个key，是评分的4个标准;
每个key后面跟随的value是一个List，该list第一个值是对应key标准下的分值，作为float;List第二个数据是str类型，写出对应key标准下的简要分析。
JSON例子如下，仅用参考格式，分析内容需要根据作文和文本重新分析:
{W_Criteria.score_format}
---
请你在我作文基础上，不改变大意和思路，用英文进行改进重写，使其能至少更好的水平。
重新文章的字数控制在450字以内。
重新文章的字数控制在450字以内。
重新文章的字数控制在450字以内。
并将改进后的作文前一行加上“改进后的作文：”，作文后不再添加任何内容
---
回答简洁意赅，请不要出现赘述
'''
        return ques_2

    @classmethod
    def part2_question_bri(cls, topic, writing, request):
        question = f'''
{W_Criteria.breif_criteria}
作文题目：
{topic}
-------------------
正文：
{writing}
-------------------
1.按照json格式打分
-------------------
2.{cls.modify_requests[request]}
-------------------
注意：除JSON格式的打分和重写的文章外，不要加入任何内容
-------------------
重写文章前加上“改进后的作文：”

'''
        return question

    # sentences
    def sentences_anaylsis(sentences: list):
        question = f'''
这是我的英文句子列表：
{sentences}
====
请你针对列表里的句子逐个进行分析，分析的角度如下：
1. 有无语法错误
2. 表达是否自然
====
将你的分析结果写成以下json格式：
{W_Criteria.sentence_analysis}
====

只回答该json格式即可
'''
        return question
    
    # misspelled
    def misspelled_words(text: str):
        question = f'''帮我找出这篇文章中所有的拼写错误的单词
注意：
1.是拼写错误，不是时态、者单复数、词性使用错误；英式美式拼写差异不算做拼写错误
例如：forgetful和forgetfulness是词性使用错误，但是forgetful本身没有拼写错误
2. 带连字符的单词要保留连字符
例如：problem-soving这个错误要保留连字符“-”
====
把错误拼写的单词汇总到一个python列表[]
把它们的正确形式汇总到另一个python列表[]
注意：同一个列表不出现相同元素
====
这是我的文章：
{text}
====
一定要仔细仔细找拼写错误
只需要回答2个python列表即可
'''
        return question

    # answer process ================================================
    def sort_essay(ai_raw):
        header = ['改进后的作文：', 'Improved Essay:']
        pattern = r"^.*?(?=\b\w+\b)"
        new_writing = None
        for h in header:
            if h in ai_raw:
                new_writing = ai_raw.split(h)[-1]
                new_writing = re.sub(pattern, "", new_writing, flags=re.DOTALL)
        if new_writing:
            return new_writing
        else:
            return ai_raw

    @classmethod
    def sort_score_essay(cls, ai_raw):
        score = SortingTXT.extract_dict(ai_raw)
        new_writing = cls.sort_essay(ai_raw)
        return score, new_writing
        # return new_writing


if __name__ == "__main__":

    test = "改进后的作文：\n\n-------------------\n\nIt is a contentious is"
    result = AIforWriting.sort_score_essay(test)
    print(result)