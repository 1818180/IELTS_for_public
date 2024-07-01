
class W_Criteria:

    criteria = '''
雅思（IELTS）大作文，即写作任务2（Writing Task 2），要求考生在40分钟内完成一篇250字以上的议论文。雅思大作文的评分标准主要包括以下四个方面：
1. Task Response（任务回应）
内容完整：文章必须充分回应题目要求，涵盖所有的任务点。
观点明确：明确陈述自己的立场或观点，并确保全篇文章观点一致。
论据支持：使用具体的例子和论据来支持观点，解释理由并提供相关的细节。
--------------
2. Coherence and Cohesion（连贯与衔接）
结构清晰：文章结构合理，有清晰的段落分隔，每段有明确的主题句。
逻辑连贯：各段落和句子之间逻辑关系清晰，过渡自然。
使用衔接词：适当使用衔接词和短语使文章流畅，如however, furthermore, on the other hand, in addition等。
------------------
3. Lexical Resource（词汇资源）
词汇丰富：使用广泛的词汇表达思想，避免重复使用简单词汇。
准确使用：词汇使用准确，能恰当地表达复杂的概念和观点。
拼写和词形正确：注意拼写正确，词形变化正确，避免基本词汇错误。
------------------
. Grammatical Range and Accuracy（语法多样性与准确性）
句型多样：使用多种句型结构，包括简单句、复合句和复杂句。
语法准确：尽量减少语法错误，如动词时态、主谓一致、冠词使用、代词指代等。
标点正确：正确使用标点符号，确保句子结构清晰。
----------------
评分细则
每个方面的评分范围是0到9分，四个评分标准的平均分即为大作文的最终得分。
------------------
'''

    score_format = '''
{
"Task Response":[9, "文章充分回应了题目要求，涵盖了双方的观点。观点明确，始终围绕“homework is important”这一观点展开。使用了具体的例子（mathematics exercises）来支持论点。"],
"Coherence and Cohesion":[8.5, "文章结构清晰，有清晰的段落分隔和主题句。段落之间的逻辑关系清晰，过渡自然。使用了适当的衔接词，如“However”、“Furthermore”、“In conclusion”。"],
"Lexical Resource":[9, "使用了丰富的词汇来表达想法，避免重复使用简单词汇。词汇使用准确，能恰当地表达复杂的概念和观点。拼写和词形正确。"],
"Grammatical Range and Accuracy":[9, "使用了多种句型结构，包括简单句、复合句和复杂句。语法准确，几乎没有语法错误。标点正确，句子结构清晰。"]
}
'''

    breif_criteria = '''
请根据以下评分标准对雅思作文进行评分，并以JSON格式输出结果：

评分标准
Task Response（任务回应）
Coherence and Cohesion（连贯与衔接）
Lexical Resource（词汇资源）
Grammatical Range and Accuracy（语法多样性与准确性）
每个方面的评分范围是0到9分，请在JSON格式中提供每个方面的评分和简要分析。

JSON格式示例
json
Copy code
{
"Task Response":[7, "中文简要分析"],
"Coherence and Cohesion":[7, "中文简要分析"],
"Lexical Resource":[7, "中文简要分析"],
"Grammatical Range and Accuracy":[6.5, "中文简要分析"]
}
待评分作文
'''

    sentence_analysis = '''
{
    "1": { 
        'sentence': '这里写分析的英文原句'
        'grammar': '详细指出存在的语法错误、表达错误，并总结一下错误的知识点；点评一下表达是否自然', # 用中文写
        'expression': '写下更自然专业准确的英文表达；如果原句表达没问题，就写下该句子意思的另一种表达形式',
    },
    "2": {...},
    ...
}
'''

class W_Examples:

    part2_9_01 = '''
People's opinions differ as to whether or not school children should be given homework. While there are some strong arguments against the setting of homework, I still believe that it is a necessary aspect of education.
There are several reasons why people might argue that homework is an unnecessary burden on children. Firstly, there is evidence to support the idea that homework does nothing to improve educational outcomes. Countries such as Finland, where school children are not given homework, regularly top international educational league tables and outperform nations where setting homework is the norm. Secondly, many parents would agree that the school day is already long enough, and leaves their children too tired to do further study when they return home. Finally, it is recognised that play time is just as beneficial as study time from the perspective of brain development.
In spite of the above arguments, I support the view that homework has an important role to play in the schooling of children. The main benefit of homework is that itencourages independent learning and problem solving, as children are challenged to work through tasks alone and at their own pace. In doing so, students must apply the knowledge that they have learnt in the classroom. For example, by doing mathematics exercises at home, students consolidate their understanding of the concepts taught by their teacher at school. In my view, it is important for children to develop an independent study habit because this prepares them to work alone as adults.
In conclusion, homework certainly has its drawbacks, but I believe that the benefits outweigh them in the long term.
'''

    part2_7_01 = '''
It cannot be denied that as international travel is becoming easier and more affordable, certain issues and inconvenience have been brought to both the travelers and locals. As a result, some impressionable people might form the bias that the development of international travel is more of a negative development. Nevertheless, as far as culture and globalization, international economy, and environmental protection are concerned, such a development is for sure a positive one.
First and foremost, the increasing easiness and affordability of international travel promotes both the spread of domestic culture and learning of foreign culture, contributing to a deeper international mutual understanding. Due to difference in ideology and value, nations around the world usually hold stereotype opinions on others, causing difficulties in personal, business, and political communication and cooperation. Easier international travel not only enables travelers to show the world what their true life is, but showcase the world right in front of the travelers. 
Second, the fact that easier international travel promotes the growth of international economy indicates that it is definitely a positive development. Take Thailand, a country that benefits greatly from tourism, for example. Thanks to the easiness of international travel in modern days, the reasonable cost of living, fantastic sightseeing spots, and charming culture in Thailand can be enjoyed by people around the world. As a result, about 25% of Thailand’s economy is closely associated with tourism, which has provided tons of jobs for locals. Had it not been for the easiness and affordability in international travel, Thailand would not have been able to attract international travels or create jobs for citizens.
A voice arises that international travel could bring devastating effects to the local environment due to pollution. Ironically, it is usually not the travelers who bring damage but lack of funding or poor management. Particularly in developing regions, without the income from travelers, the locals would have no choice but to exploit natural resources and damage the environment; on the other hand, effective tourism management can not only generate funding for the environmental protection but keep the sightseeing spots from being affected.
Therefore, in terms of culture and globalization, international economy, and environmental protection, I strongly hold the opinion that easier international travel is a positive development. While one sees a circle and another sees a zero, I believe my opponents will compromise upon being shown to my article.
'''

    part2_6_01 = '''
Some people say job satisfaction is more important than job security, while others believe that having a permanent job is better than enjoying the job. Discuss both views and give your own opinion.

Everybody has to work. The question is: which is more important in work, the job security or the job satisfaction? Some people think the job security is more important than job satisfaction, but others believe the opposite. In my view, both job security and satisfaction are important.
We all need a secure job. If we have a stable job, we can make a lot of money. Then we can buy big houses and expensive cars, and can travel all around the world. This will make our life more wonderful. If we have a stable job, we will not have to worry about losing our job. So we do not have to spend time looking for jobs. This means we can have more time to stay together with our family.
However, it is also important to have an interesting job. If we have an interesting job, we can do our job well. Then we can get happiness from our job. If we are not interested in what we do, we can never succeed no matter how stable our job is. My uncle James is a good example. He is a middle school teacher, which is a very stable job. However, he is not really interested in teaching. As a result, he is not very successful even at his fifties.
In conclusion, I think it is the best that we have a secure and satisfying job, because this kind of job helps us to make our living and have time to stay together with our family, and at the same time succeed in our career. I wish everybody could get such a job.
'''


class W_Test:
    part2_test_topic = "Some people think that children should start learning a foreign language from primary school, while others think it should be secondary school. Discuss both views and give your own opinion."
    part2_test_essay = '''
Learning a foreign language is becoming increasingly important in today's globalized world. While some argue that children should begin learning a foreign language in primary school, others advocate for introduction in secondary school. In this essay, we will explore both views before providing our own perspective.
Some believe that teaching a foreign language from primary school would be more effective than secondary school. The brain is more susceptible to learning languages before the age of 12, and starting early would provide children with greater exposure to the language. A study conducted in London shows that children who start learning a new language before the age of 10 are more likely to achieve a higher level of proficiency compared to those who start later in life.
On the other hand, others believe that schools should start teaching foreign languages in secondary school. Children might not have developed enough cognitive and linguistic skills to learn a new language in primary school. In some cases, it might even lead to language fatigue or loss of interest in learning new things. In fact, many European countries such as Finland and Sweden don't start teaching foreign languages until secondary school.
Considering both perspectives, I believe that introducing a foreign language in primary school would be more beneficial. As stated earlier, the younger the brain, the easier it is to learn new languages, and starting early would provide children with a head start in language proficiency. Moreover, in today's globalized world, knowledge of a second language is a key asset for future career prospects, and learning a new language would open up new opportunities for children. However, it's important to ensure that the language learning curriculum is age-appropriate and engaging for children, so as to maintain their interest.
To conclude, both perspectives on the debate about foreign language learning have their own merits, but I support the view that children should learn a second language from primary school itself. By starting early, children would have a greater opportunity to gain proficiency in a foreign language, giving them a competitive edge in their future careers. Nonetheless, it is vital for language learning curriculum to be implemented in a way that effectively captures the children's interest.
'''
    part2_test = [
        part2_test_topic,
        part2_test_essay
    ]

    part2_my_topic = "Some people believe that school children should not be given homework by their teachers, whereas others argue that homework plays an important role in the education of children. Discuss both of these views and give your own opinion."
    part2_my_essay = '''Whether homework should be given by school teachers to children, some argue that there is no need, and others think it's an essential approach of education. In my opinion, homework is needed, especially in an effective and suitable way.
School assignments are important, because without enough practises, it's impossibale to truly comprehend the knowledge you learned. Studying at school is just reciving input, the first stage of learing that understanding the superfical side of concepts or notions. Due to the easily forgetful mechanic of our brains, only repeatedly revising and processing the knowledge can turn the input into our ouput. After all, knowledge we can’t apply is deemed to be useless.
However, for some people, homework assigned by teachers are not good for learning. It’s true that some school tasks are tedious and not appealing to kids, but the most concerning problem is lacking of effectivenes and efficiency, not homework itself. To make things worse, these inefficient tasks, such as overly reapeating, can be conterproductive to students’ insterest in learing. Moreover, one task can’t suit all, every student should get their own assignment.
I think that homework is still needed and its shortcomes can be fixed by artifical intelligence. In the era of MLLs(mass language model) like ChatGPT,  after breaking the information barrier, knowledge itself is no longer as much valuable as before. Instead, the ability of quickly applying knownledge to problem-soving is vital, which needs to be cultivated in school days by doing related homework. On the other hand, school assignments can be customlized to everyone by using AI to appraise personal studying condition. 
In a nutshell, homework is basicly a measure to internalize the knowledge for future use. And it should be tailored to every student and make the learning process more effective.
'''
    part2_my = [
        part2_my_topic,
        part2_my_essay
    ]