import streamlit as st
import pandas as pd
from assets.prompt import AIforWriting, AImodel
from assets.sort_tool import SortingTXT, StyleTXT
from chart.df_template import DFtemplates

st.set_page_config(
    page_title="IELTS Writing Helper",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",                                                                                                      
    menu_items={
        'Get Help': 'https://github.com/1818180/IELTS_writing_helper',
        'Report a bug': "https://github.com/1818180/IELTS_writing_helper",
        'About': "# This is my *first* Web APP! Hope it's helpful to you!"
    }
)

def state_initialize(key, value):
    if key not in st.session_state:
        st.session_state[key] = value
    else:
        pass

def state_update(key, value):
    st.session_state[key] = value


state_initialize('word_lengths', 0)
state_initialize('score', None)
state_initialize('new_writing', {})
state_initialize('misspelled', DFtemplates.df_misspelled_words())
state_initialize('corrected_writing', None)
state_initialize('grammer_anaylsis', None)
state_initialize('practice_sentence', None)
state_initialize('sentences_practice_notebooks', {})

new_writing_dict = st.session_state.new_writing
grammer_anaylsis = st.session_state.grammer_anaylsis

@st.experimental_dialog("Hold on!")
def warning(word):
    st.warning(word)

@st.experimental_dialog("Export")
def export_content():
    all1, my_essay2, analyse3, notebook4 = st.tabs(['all content', 'my essay','essay analysis', 'notebooks'])
    with all1:
        with st.container(height=500,border=False):
            st.session_state
    with my_essay2:
        with st.container(height=500,border=False):
            if st.session_state.topic:
                st.session_state.topic
                st.divider()
            else:
                st.warning('no topic')
            if st.session_state.writing:
                st.session_state.writing
                st.divider()
            else:
                st.warning('no writing')
            st.dataframe(st.session_state.misspelled, hide_index=True, use_container_width=True)
    with analyse3:
        with st.container(height=500,border=False):
            if st.session_state.grammer_anaylsis:
                st.session_state.grammer_anaylsis
                st.divider()
            else:
                st.warning('no sentences analysis yet')
            if st.session_state.new_writing:
                st.session_state.new_writing
            else:
                st.warning('no improved essays yet')
            
    with notebook4:
        with st.container(height=500,border=False):
            if st.session_state.sentences_practice_notebooks:
                st.session_state.sentences_practice_notebooks
            else:
                st.warning('no notebooks yet')

with st.sidebar:
    st.image("./assets/images/logo.png")
    st.header("Topic")
    topic = st.text_area(
        label="💡 IELTS writing topic:",
        height=150,
        placeholder="What's the topic of your writing?",
        key="topic"
    )
    draft = st.text_area(
        label="💡 Simple draft:",
        height=150,
        key="draft",
        placeholder="Have any ideas?",
    )
    # st.divider()
    st.caption("After completing the study, all relevant content can be exported in JSON format ")
    bu_save_essay = st.button("📍 Export all content ", type='primary',use_container_width=True,on_click=lambda :export_content())
    st.divider()
    st.page_link("https://github.com/1818180/IELTS_writing_helper", label="My Github", icon="👩")

def word_lengths():
    text = st.session_state['writing']
    words = text.split()
    lengths = len(words)
    st.session_state['word_lengths']=lengths
    return lengths


def update_essay(model, essay_new):
    if model not in list(new_writing_dict.keys()):
        new_writing_dict[model] = [essay_new]
    else:
        new_writing_dict[model].append(essay_new)
    st.toast("💖 New essay added already!")

def only_essay(model, request):
    topic = st.session_state.topic
    writing = st.session_state.writing
    question = AIforWriting.part2_only_essay(topic, writing, request)
    answer = AIforWriting.submit_question_to_AI(question, model)
    update_essay(model=model, essay_new=answer)

def score_essay(model, request):
    if model:
        topic = st.session_state.topic
        writing = st.session_state.writing
        question = AIforWriting.part2_question_bri(topic, writing, request)
        answer = AIforWriting.submit_question_to_AI(question, model)
        st.toast(f"Sending request to {model}")
        if answer:
            score, new_writing = AIforWriting.sort_score_essay(answer)
            state_update('score',score)
            st.toast("💌 Score has been successfully fetched!")
            update_essay(model,new_writing)
            st.toast("💌 New improved essay has been successfully fetched! Check out in Tab ***'anaylse center'***")
    else:
        warning("Please select one AI model")


@st.experimental_dialog("Choose your prompt")
def submit_ai():
    models = [model for model in AImodel.models]
    submit_t1, prompt_tab2 = st.tabs(['Submit essay','Copy prompt'])
    with submit_t1:
        with st.container(border=True):
            ai_model = st.radio(
                "choose an AI model",
                models,
                index=0,
                horizontal=True,
                help="具体模型选择"
            )
        with st.container(border=True):
            essay_request = st.select_slider(
                "choose AI improvement scale",
                [key for key in AIforWriting.modify_requests.keys()]
            )
        st.write("使用", ai_model, "模型")
        st.write(AIforWriting.modify_requests[essay_request])
        st.button("Submit to AI", type='primary', on_click=lambda :score_essay(ai_model, essay_request))
    with prompt_tab2:
        st.caption("if you want to use outside AI, copy the prompt below")
        with st.container(height=300, border=False):
            question = AIforWriting.part2_question_bri(st.session_state.topic, st.session_state.writing, essay_request)
            st.code(question)


# overall layout==========================================================================

writing_space, analyse_space, practice_space = st.tabs(["***:blue-background[◾ WRITE ◾]***", "***:blue-background[◾ ANALYSE ◾]***", '***:blue-background[◾ PRACTICE ◾]***'])

with writing_space:
    show_topic, buff, output_col, buff, writing_helper = st.columns([1, 0.1, 1.5,0.1, 1])

# writing ==========================================================================

with output_col:
    st.text_area(
        label='writing',
        label_visibility="collapsed",
        height=680,
        placeholder='start writing ~',
        key="writing",
        on_change=lambda :word_lengths()
    )
    if st.session_state['word_lengths'] > 250:
        submit_essay = st.button("Submit Essay", type='primary')
        if submit_essay:
            submit_ai()
    else:
        st.caption("You can only submit if you've written enough words, keep writing, please ~")


with show_topic:
    if st.session_state.topic:
        st.subheader("Topic")
        st.markdown(st.session_state.topic)
        st.markdown('---')
    if st.session_state.draft:
        st.subheader("Draft")
        st.markdown(f'''{st.session_state.draft}''')
        st.markdown('---')
    st.write("You have writen ", st.session_state['word_lengths']," characters.")

if st.session_state.score:
    st_score = st.session_state.score
    with writing_helper:
        with st.expander("AI Score"):
            s1,s2,s3,s4 = st.columns(4)
            ss = [s1,s2,s3,s4]
            for i in range(len(ss)):
                with ss[i]:
                    with st.container(height=80, border=False):
                        tit_md = "###### ***" + st_score[i][0] + "***"
                        st.markdown(tit_md)
                    st.markdown(st_score[i][1])
                    anaylsis_markdown = StyleTXT.markdown_period(st_score[i][2])
                    with st.popover(f"**⭐{i+1}**",use_container_width=True):
                        st.markdown(anaylsis_markdown)

# analyse ==========================================================================

with analyse_space:
    misspelled_w, grammer_error, fulltext, sen_improve = st.tabs(["🌼 **Misspelled words**", "🌱 **Grammer error**", "🍀 **Improved essay**", "🌻 **Improved sentences**"])

# analyse ==========================================================================

def find_misspedlled():
    state_update('corrected_writing', st.session_state.corrected_writing)
    words_w = SortingTXT.txt_2words_list(st.session_state.writing)
    words_r = SortingTXT.txt_2words_list(st.session_state.corrected_writing)
    misspelled_words = SortingTXT.find_different_words(words_r, words_w)
    if isinstance(misspelled_words, str):
        warning(misspelled_words)
    else:
        df1 = st.session_state.misspelled
        df2 = misspelled_words
        merged_df = pd.concat([df1, df2])
        merged_df = merged_df.drop_duplicates()
        st.session_state.misspelled = merged_df.dropna()

with misspelled_w:
    m1, buff, m2 = st.columns([3,0.1,1])
    with m1:
        st.info("TIPS: 可以利用浏览器自带的拼写工具改正错误单词，改完记得保存哦~ （edge浏览器很好用）",icon="🔵")
        st.button("🌼 Get esssay", on_click=lambda :state_update('corrected_writing', st.session_state.writing))
        st.text_area(
            "please using mirosoft tool check misspelled words",
            label_visibility='collapsed',
            height=450,
            key="corrected_writing",
        )
        st.button("🌼 Save changes", on_click=lambda :find_misspedlled(), type='primary')
    with m2:
        st.subheader("Misspelled Words")
        st.dataframe(st.session_state.misspelled, hide_index=True, use_container_width=True)


# analyse sentences ==========================================================================

def chose_add_type(new_dict):
    def process_anay():
        type = st.session_state.adding_type
        if type == "replace all":
            st.toast("正在添加至分析字典中") 
            state_update('grammer_anaylsis', new_dict)
        elif type == "add in":
            st.toast("正在添加至分析字典中")
            for num in list(new_dict.keys()):
                if new_dict[num]['sentence'] == st.session_state.grammer_anaylsis[num]['sentence']:
                    st.session_state.grammer_anaylsis[num]['grammar'] += "\n" + new_dict[num]['grammar']
                    st.session_state.grammer_anaylsis[num]['expression'] += "\n" + new_dict[num]['expression']
        else:
            warning("Please choose one adding type")

    with sentence_analysis_setting:
        with st.form("type"):
            st.table(new_dict)
            st.selectbox(
                "choose the add type",
                options=("replace all", "add in"),
                index=None,
                key="adding_type",
                label_visibility='collapsed',
            )
            st.form_submit_button("🌱submit type", on_click=lambda :process_anay())

def get_ai_sentence_anay(sentence: list, model: str):
    question = AIforWriting.sentences_anaylsis(sentence)
    answer = AIforWriting.submit_question_to_AI(question, model)
    anaylsis_str = SortingTXT.extract_outermost_json(answer)
    anaylsis_dict = SortingTXT.convert_to_dict(anaylsis_str)
    sentence_anaylsis_depart(anaylsis_dict)

def sentence_anaylsis_depart(ana_dict):
    if st.session_state.grammer_anaylsis == None:
        st.session_state.grammer_anaylsis = ana_dict
    else:
        if ana_dict:
            chose_add_type(ana_dict)
        else:
            warning("Wrong format ☹")

with grammer_error:
    set_c , buff, ana_c= st.columns([0.5,0.1,2.1])
    with ana_c:
        st.subheader("Analysis Display")
        if st.session_state.grammer_anaylsis is not None:
            for key, value in st.session_state.grammer_anaylsis.items():
                with st.container(border=False):
                    sen = f'''##### :blue-background[{key}.] {value['sentence']}'''
                    st.markdown(sen)
                    if '\n' in value['grammar']:
                        grammars = value['grammar'].split('\n')
                        for grammar in grammars:
                            if grammar:
                                st.markdown(f"- :red-background[{grammar}]")
                    else:
                        st.markdown(f"- :red-background[{value['grammar']}]")

                    if '\n' in value['expression']:
                        expressions = value['expression'].split('\n')
                        for expression in expressions:
                            if expression:
                                sen_impr = "**:blue[" + expression + "]**"
                                st.markdown(sen_impr)
                    else:
                        sen_impr = "**:blue[" + value['expression'] + "]**"
                        st.markdown(sen_impr)
                    st.divider()
    with set_c:
        st.info("改正完拼写错误，来这里一键生成原文的逐句分析👇",icon="🔵")
        if st.session_state.writing:
            essay_for_anaylse = st.session_state.writing
            if st.session_state.corrected_writing:
                essay_for_anaylse = st.session_state.corrected_writing
            sentence_analysis_setting = st.popover("🌱 Get sentences analysis",use_container_width=True)
            st.image("https://i.pinimg.com/564x/0d/ae/8f/0dae8f4113af470174b8323c9d6182e2.jpg")
            with sentence_analysis_setting:
                ana1,ana2 = st.tabs(["Use built-in AI", "Input DIY answer"])
                with ana2:
                    st.caption("🔵 COPY the sentences anaylsis prompt below.")
                    sentences = SortingTXT.find_s_in_txt(essay_for_anaylse)
                    question = AIforWriting.sentences_anaylsis(sentences)
                    with st.container(height=130,border=False):
                        st.code(question)
                    diy_anay = st.text_area(label="diy_anay", label_visibility='collapsed', placeholder="copy the answer here with correct format",height=130)
                    submit_diy_anay = st.button("🌱Submit DIY", on_click=lambda :sentence_anaylsis_depart(SortingTXT.convert_to_dict(diy_anay)),type='primary')
                with ana1:
                    ai_model = st.radio(
                        "choose an AI model",
                        options=[model for model in AImodel.models],
                        index=None,
                        horizontal=True,
                        help="具体模型选择"
                    )
                    submit_sentence_anaylse = st.button(label="🌱submit", on_click=lambda :get_ai_sentence_anay(sentence=SortingTXT.find_s_in_txt(essay_for_anaylse), model=ai_model),type='primary')
        # else:
            # st.warning("You need to correct the misspelled words first 👻",icon="🔴")


# analyse new essays ==========================================================================

with fulltext:
    setcol, buff, aicol, buff , mecol = st.columns([0.5,0.1,1,0.1,1])
    with setcol:
        st.info("获取更多范文，可以内置AI生成或自己导入~",icon="🔵")
        with st.popover("🍀 Get improved essay", use_container_width=True):
            ai1, ai2 = st.tabs(["Use built-in AI", "Use DIY answer"])
            with ai1:
                with st.container(border=True):
                    ai_model_essay = st.radio(
                            "select ai model",
                            options=[model for model in AImodel.models],
                            index=None,
                            horizontal=True,
                            help="具体模型选择"
                        )
                    st.divider()
                    new_essay_request = st.select_slider(
                        "select AI improvement scale",
                        [key for key in AIforWriting.modify_requests.keys()],
                    )
                st.caption(f"使用{ai_model_essay}模型")
                st.caption(AIforWriting.modify_requests[new_essay_request])
                get_new_essay = st.button(label="🍀 submit to AI",type='primary',on_click=lambda :only_essay(ai_model_essay,new_essay_request))
            with ai2:
                st.caption("Copy the prompt below")
                question = AIforWriting.part2_only_essay(st.session_state.topic, st.session_state.writing, new_essay_request)
                with st.container(height=200,border=False):
                    st.code(question)
                st.caption("Copy your DIY essay below")
                copied_essay = st.text_area(
                    "copied_essay",
                    label_visibility='collapsed',
                    height=200
                )
                st.button(label='🍀 Submit DIY', on_click=lambda :update_essay("DIY", copied_essay),type='primary')
        st.image("./assets/images/cat.png")
    with mecol:
        st.subheader("My essay")
        if st.session_state.corrected_writing:
            st.markdown(st.session_state.corrected_writing)
        else:
            st.markdown(st.session_state.writing)
    with aicol:
        st.subheader("Improved essay")
    if  len(list(model for model in list(st.session_state.new_writing.keys()))) > 0 :
        with setcol:
            st.selectbox(
                "Select source model",
                (model for model in list(st.session_state.new_writing.keys())),
                index=0,
                key="model_select"
            )
            st.selectbox(
                "Select different version",
                (i+1 for i in range(len(st.session_state.new_writing[st.session_state.model_select]))),
                key="essay_num",
                index=0
            )
        with aicol:
            st.markdown(st.session_state.new_writing[st.session_state.model_select][st.session_state.essay_num-1])


# analyse ==========================================================================
def make_sen_practice_notebook(name: str):
    if st.session_state.practice_translate and st.session_state.practice_translate and name:
        new_notebook = {}
        en_sen = SortingTXT.find_s_in_txt(st.session_state.practice_content)
        zh_sen = st.session_state.practice_translate.split('\n\n')
        if len(en_sen) == len(zh_sen):
            for con, tran in zip(en_sen, zh_sen):
                new_notebook[con] = {}
                new_notebook[con]['translation'] = tran
            st.session_state['sentences_practice_notebooks'][name] = new_notebook
            state_update('practice_content', None)
            state_update('practice_translate', None)
        else:
            warning("英文句子和中文句子个数不匹配😢，注意中文翻译的句子之间要多空一行👀")
    else:
        warning("***英文文章***，***对应翻译***和***笔记本名称***缺一不可那👻")


def add_notebook(notebook:dict):
    first_level_values = list(notebook.values())[0]
    if 'translation' in list(first_level_values.values())[0].keys():
        st.session_state['sentences_practice_notebooks'].update(notebook)
    else:
        warning("notebook format isn't right")

def save_keyword():
    name = st.session_state.selected_notebook
    sentence = notebook_sentences[st.session_state.select_index]
    st.session_state.sentences_practice_notebooks[name][sentence]['keyword'] = st.session_state.keyword

with sen_improve:
    note1,buff, note2,buff = st.columns([1,0.2,3,1.2])
    with note1:
        st.info("创建你的学习笔记吧！记录每一句的keywords，在练习板块[PRACTICE]还可以造句巩固",icon="🔵")
        with st.popover("🌻 Crate Notebook",use_container_width=True):
            diytab, copytab = st.tabs(['Create','Copy'])
        with diytab:
            st.caption('🔵 Improved essay')
            if st.session_state.new_writing:
                st.button("🌻 Use selected improved essay",use_container_width=True, on_click=lambda :state_update("practice_content",st.session_state.new_writing[st.session_state.model_select][st.session_state.essay_num-1]))
            st.text_area('improved essay',key="practice_content", height=150,label_visibility='collapsed',placeholder="Copy or select the improved essay")
            st.caption('🔵 Translation Console: Split essay into sentences')
            if st.session_state.practice_content:
                with st.container(height=150, border=True):
                    for con in SortingTXT.find_s_in_txt(st.session_state.practice_content):
                        st.markdown(con)
            st.caption('🔵 Translation: ')
            st.text_area('Translation',key='practice_translate', height=150, label_visibility='collapsed',placeholder="Copy Chinese translation sentence by sentence")
            st.caption('🔵 Name: ')
            notebook_name = st.text_input('notebook name',placeholder="notebook name",label_visibility='collapsed')
            st.button('🌻 Create', on_click=lambda :make_sen_practice_notebook(notebook_name),type='primary')
        with copytab:
            copied_notebook = st.text_area('copy your notebook with right format',height=400)
            st.button('🌻 Add',type='primary',on_click=lambda :add_notebook(SortingTXT.convert_to_dict(copied_notebook)))
        st.image('https://i.pinimg.com/564x/37/85/0a/37850a199fd1b4be73f02ff6c6f8619c.jpg')
        if tuple(st.session_state.sentences_practice_notebooks.keys()):
            st.selectbox(
                label='choose one notebook',
                options=(tuple(st.session_state.sentences_practice_notebooks.keys())),
                key='selected_notebook',
                label_visibility='hidden',
                on_change=lambda :state_update('select_index', 0)
            )
            notebook_sentences = list(st.session_state.sentences_practice_notebooks[st.session_state.selected_notebook].keys())
            state_initialize('select_index', 0)
            select_sen = notebook_sentences[st.session_state.select_index]
            num,se1,se2 = st.columns(3)
            with num:
                st.write(st.session_state.select_index,'/',len(notebook_sentences)-1)
            with se1:
                st.button('◀',use_container_width=True, 
                          on_click=lambda: st.session_state.update(select_index=max(0, st.session_state.select_index - 1)))
            with se2:
                st.button('▶',use_container_width=True,
                          on_click=lambda: st.session_state.update(select_index=min(len(notebook_sentences) - 1, st.session_state.select_index + 1)))
    with note2:
        if 'selected_notebook' in st.session_state:
            st.markdown(f'''#### :blue[{notebook_sentences[st.session_state.select_index]}]''')
            if 'keyword' in st.session_state.sentences_practice_notebooks[st.session_state.selected_notebook][select_sen]:
                keyword_list = st.session_state.sentences_practice_notebooks[st.session_state.selected_notebook][select_sen]['keyword'].split('\n')
                filtered_keys = [key for key in keyword_list if key != '']
                for key in filtered_keys:
                    if '=' not in key:
                        st.markdown(f''':red-background[{key}]''')
                    else:
                        key1, key2 = key.split('=', 1)
                        st.markdown(f''':red-background[{key1}]''')
                        if '//' not in key:
                            st.markdown(f'''* {key2}''')
                        else:
                            for k in key2.split('//'):
                                st.markdown(f'''* {k}''')
            keyword = st.session_state.sentences_practice_notebooks[st.session_state.selected_notebook].get(select_sen, {}).get('keyword', '')
            st.text_area(
                '**keywords**',
                value=keyword, 
                key='keyword',
                on_change=lambda :save_keyword(),
                height=200,
                help="笔记格式：1. 一行只写一条笔记。2. keyword和补充内容用“=”分隔。3. 补充内容可以用“//”来分隔"
            )

# analyse ==========================================================================
with practice_space:
    re1,buff,re2,buff,re3 = st.columns([1,0.1,3,0.1,1])
    if st.session_state.sentences_practice_notebooks:
        with re1:
            st.info("选择笔记本开始造句学习吧！主动记忆效果最好💪",icon="🔵")
            st.image("https://i.pinimg.com/564x/29/51/fa/2951fafff227a1bfae56029170525802.jpg")
            st.selectbox(
                'select notebook',
                (tuple(st.session_state.sentences_practice_notebooks.keys())),
                key='select_practice_book',
                label_visibility='collapsed'
            )
            book_content = st.session_state.sentences_practice_notebooks[st.session_state.select_practice_book]
            all_notes = list(book_content.values())
                    
        with re2:
            with st.container(height=850, border=False):
                for content in book_content.keys():
                    st.markdown(f'''##### :green[{book_content[content]['translation']}]''')
                    st.text_area(label='⭐',help=content, height=25)
                    st.divider()
        with re3:
            st.subheader("All the notes")
            with st.container(height=800, border=False):
                for note in all_notes:
                    # st.write(note)
                    if 'keyword' in list(note.keys()):
                        keys = note['keyword'].split('\n')
                        for k in keys:
                            if '=' in k:
                                no1, no2 = k.split('=', 1)
                                st.markdown(f''':red-background[{no1}]''')
                                if '//' not in k:
                                    st.markdown(f'''* {no2}''')
                                else:
                                    for n in no2.split('//'):
                                        st.markdown(f'''* {n}''')
                            else:
                                st.markdown(f''':red-background[{k}]''')
    else:
        with re2:
            st.info("还没有笔记本哦，返回分析板块[ANALYSE]创建吧",icon="🔵")
            st.image('./assets/images/back.png')


