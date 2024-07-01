import re
import ast
import json
import pandas as pd
from nltk.tokenize import sent_tokenize
from snownlp import SnowNLP
from spellchecker import SpellChecker
from textblob import TextBlob

# 便于筛取AI回答中的有用信息
class SortingTXT:

    @staticmethod
    def check_spelling(text):
        spell = SpellChecker()
        # 使用正则表达式拆分文本，仅保留单词部分
        words = re.findall(r'\b\w+\b', text)
        misspelled = spell.unknown(words)
        for word in misspelled:
            print(f"'{word}' is misspelled. Suggestions: {spell.candidates(word)}")
        # misspelled_words = list(misspelled)
        # suggestions = [spell.correction(word) for word in misspelled]
        
        # return misspelled_words, suggestions

    @staticmethod
    def txt_2words_list(text:str):
        pattern = r"[^\w\s'-]"
        cleaned_paragraph = re.sub(pattern, '', text)
        word_list = cleaned_paragraph.split()
        return word_list      

    @staticmethod
    def find_different_words(words_r: list, words_w:list):
        if len(words_r) == len(words_w):
            find_words = []
            for i in range(len(words_r)):
                if words_r[i] != words_w[i]:
                    find_words.append({"✔ right word": words_r[i], "❌ wrong word": words_w[i]})
            words_df = pd.DataFrame(find_words)
            return words_df
        else:
            return "text isn't match"

    @staticmethod
    def find_s_in_txt(tt: str):
        sentences = sent_tokenize(tt)
        return sentences
        # sentences = [ s1, s2 ]

    @staticmethod
    def find_lists_in_txt(txt: str):
        list_pattern = re.compile(r'\[[^\[\]]*\]')
        matches = list_pattern.findall(txt)
        lists = [ast.literal_eval(match) for match in matches] 
        return lists

    @staticmethod
    def dict_2_list(dict):
        result = []
        for key, value in dict.items():
            value.insert(0, key)
            result.append(value)
        return result


    def extract_outermost_json(string):
        # 找到第一个出现的 '{'
        start = string.find('{')
        # 找到最后一个出现的 '}'
        end = string.rfind('}')
        
        if start != -1 and end != -1 and start < end:
            dict_str = string[start:end+1]
            # 返回字典字符串
            return dict_str
        else:
            print("未找到完整的字典部分")
            return None

    @classmethod
    def extract_dict(cls, raw_txt):
        pattern = r'\{.*?\}'
        match = re.search(pattern, raw_txt, re.DOTALL)
        if match:
            dict_str = match.group()
            # 将字符串转换为Python字典
            extracted_dict = ast.literal_eval(dict_str)
            extracted_list = cls.dict_2_list(extracted_dict)
            return extracted_list
        else:
            print("未找到符合条件的字典")
            return None

    def convert_to_dict(dict_str):
        # 替换单引号为双引号
        # dict_str = re.sub(r"'", '"', dict_str)
        # 去除注释（以 # 开头的内容）
        dict_str = re.sub(r"#.*", "", dict_str)
        # 替换逗号和大括号之间的换行符
        dict_str = re.sub(r",\s*}", "}", dict_str)
        dict_str = re.sub(r",\s*]", "]", dict_str)
        # 去除字典内部属性之间缺少的逗号（针对示例输入）
        dict_str = re.sub(r'(?<=[}\w"])("\s*")(?=[{\w])', r'\1,', dict_str)
        
        try:
            # 使用 ast.literal_eval 将字符串转换为字典
            dictionary = ast.literal_eval(dict_str)
            return dictionary
        except (SyntaxError, ValueError) as e:
            print(f"字典转换错误: {e}")
            return None

class StyleTXT:
    def markdown_period(txt:str):
        sentences = txt.split('。')
        md_list = []
        for s in sentences:
            # s = "###### " + s
            md_list.append(s)
        md = "\n\n".join(md_list)
        return md


if __name__ == "__main__":
    test = '''
请你在我作文基础上, 用英文进行改进重写, 使其能至少达到雅思8分水平，或者比刚刚打分更好的水平。
并将改进后的作文前一行加上“改进后的作文：”，作文后不再添加任何内容

{
"Task Response": [8, "文章充分回应了题目要求，涵盖了双方的观点。观点明确，始终围绕“obesity is a complex problem”这一观点展开。使用了具体的例子（distribution of healthy food）来支持论点。"],
"Coherence and Cohesion": [7.5, "文章结构清晰，有清晰的段落分隔和主题句。段落之间的逻辑关系清晰，过渡自然。使用了适当的衔接词，如“Moreover”、“In addition”。但个别段落之间衔接稍显生硬。"],
"Lexical Resource": [8, "使用了丰富的词汇来表达想法，避免重复使用简单词汇。词汇使用准确，能恰当地表达复杂的概念和观点。个别单词拼写或词形错误。"],
"Grammatical Range and Accuracy": [8, "使用了多种句型结构，包括简单句、复合句和复杂句。语法准确，有少量语法错误。标点正确，句子结构清晰，但个别句子结构过于复杂。"]
}

改进后的作文：
'''
    # SortingTXT.extract_dict(test)

    test_txt = '''It's widely debated that whether the young people should be educated by the ex-criminal about the harms of crimes. Somes think the first-hand experience are more convincing for education. And I hold the same belief with them, due to the effiencency and the social stability.
For the safety of children, some parents will feel dangerous when the details of crimes are exposed to their kids. It is truly understandable, because human at the early stage tend to imitate others' behaviors. And there are some horrible incidents happened when kids got badly injured after mimicking the high-risk movements from cartoons. However, in the case of teenagers, they already have basic moral norms and safety rules in mind and are mentally prepared for identifying which actions are acceptable. As long as we carefully scrutnize the content of first-hand experiences lecture, only leaving the essence of the main idea, such speeches about the journey of finding the right direction are significant and powerful for teenagers to stablish a health and solid value system.
In my opioion, these speeches from real criminals are not only capable for educational propose but the best suit ones. To prevent teenagers from breaking the rules, only refering the damages and negative social impact are not enough. We have to remove the criminal motivaition in the first place, and no one could understand better than those used-be prisoners. And the causes of committing crimes vary from desire, hate these personal issues to the helpless, hopeless those life situations. By sharing these motivations, it could be clear that crimes cannot be the solution of the difficulties in life but exacerbating the situation even worse. On the other hand, teenagers could learn to deal with their negative feelings and even help others to get by the difficulties, which can widely eliminish(reduce) the crime rate.
In conclusion, those who once been in the prison are capable and suitable for speaking of damages of crimes in school. Teens can be  related to the crime motivation and prevent it in the first place.
'''
    # SortingTXT.check_spelling(test_txt)

    # w_list = SortingTXT.txt_2words_list(test_txt)
    # print(w_list)

    input_string = """
    {
        "1": {
            'sentence': '这里写分析的英文原句',
            'grammer': '指出语法的错误或单词短语的表达错误', # 用中文写
            'expression': '写下更自然专业的英文表达；如果原句表达没问题，就写下该句子意思的另一种表达形式',
        },
        "2": {
            'sentence': '另一句英文原句',
            'grammer': '另一处语法错误',
            'expression': '另一种表达方式',
        }
    }
    """

    json_data = SortingTXT.extract_outermost_json(input_string)
    print(json_data)
