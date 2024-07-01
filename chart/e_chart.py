import streamlit as st

import pandas as pd
import altair as alt

from collections import Counter



class Life_chart:

    def get_key_words(k_data: dict):
        key_list = []
        for title in k_data.values():
            title_list = title.split('/')
            for t in title_list:
                key_list.append(t)
        return key_list

    def get_keys_num(k_list: list):
        counter = Counter(k_list)
        # keys_num = [(element, count) for element, count in counter.items() if count > 1]
        keys_num = [(element, count) for element, count in counter.items()]
        return keys_num
    
    def extract_relate_data(all_data, aim_range):
        relate_date = []
        for date in aim_range:
            date_str = date.strftime('%Y-%m-%d')
            # 检查日期是否在字典中
            if date_str in all_data:
                relate_date.append(all_data[date_str])
            else:
                relate_date.append(None)
        return relate_date

    @classmethod
    def range_date_data(cls, datas:dict, aim_range):
        relate_date = cls.extract_relate_data(datas, aim_range)
        relate_date_data = {}
        for i in range(len(aim_range)):
            if relate_date[i]:
                relate_date_data[aim_range[i]] = relate_date[i]
        return relate_date_data

    @classmethod
    def life_weight(cls, w_data: dict, d_range):
        weights = cls.extract_relate_data(w_data, d_range)
        data = {'date': d_range, 'weight': weights}
        w_df = pd.DataFrame(data)
        # 将日期列设置为索引
        # w_df.set_index('date', inplace=True)
        weight_chart1 = (
            alt.Chart(w_df)
            .mark_line(color='#9095AB')
            .encode(
                alt.X("monthdate(date):T", title=None),
                alt.Y(
                    "weight:Q",
                    title="Weight (KG)",
                    scale=alt.Scale(domain=[55, 68]),
                ),
                tooltip=['date:T', 'weight:Q']
            )
            .properties(height=300)
            .interactive()
        )
        weight_chart2 = (
            alt.Chart(w_df)
            .mark_area(color='#C3CEF7', clip=True, opacity=0.3)
            .encode(
                alt.X("monthdate(date):T", title=None),
                alt.Y(
                    "weight:Q",
                    title="Weight (KG)",
                    scale=alt.Scale(domain=[55, 68]),
                ),
                tooltip=['date:T', 'weight:Q']
            )
            .properties(height=300)
            .interactive()
        )
        weight_chart = alt.layer(weight_chart1, weight_chart2).properties(height=300)
        return weight_chart
    
    @classmethod
    def life_mood(cls, m_data: dict, d_range):
        relate_moods = cls.range_date_data(m_data, d_range)
        # st.write(relate_moods)
        rows = []
        for date, moods in relate_moods.items():
            for mood in moods:
                rows.append({'date': date, 'mood': mood})
        if len(rows) == 0:
            return None
        else:
            mood_source = pd.DataFrame(rows)
            mood_source['date'] = pd.to_datetime(mood_source['date'])
            mood_collection = ["💗激情满满", "❤开心！", "🧡还不错", "💙平静如水", "💛略微不开心", "😥难过", "💚焦虑", "💢愤怒"]
            mood_y_values = {
                mood_collection[0]: 5,
                mood_collection[1]: 4,
                mood_collection[2]: 3,
                mood_collection[3]: 2,
                mood_collection[4]: 1,
                mood_collection[5]: 0,
                mood_collection[6]: -1,
                mood_collection[7]: -2,
            }
            mood_size_values = {
                mood_collection[0]: 800,
                mood_collection[1]: 650,
                mood_collection[2]: 450,
                mood_collection[3]: 350,
                mood_collection[4]: 200,
                mood_collection[5]: 400,
                mood_collection[6]: 600,
                mood_collection[7]: 800,
            }
            mood_source['y'] = mood_source['mood'].map(mood_y_values)
            mood_source['size'] = mood_source['mood'].map(mood_size_values)

            color_scale = alt.Scale(
                domain=mood_collection,
                range=["#FB573D", "#FA6620", "#F29D35", "#6A9FFA", "#FFD870", "#D5EDF2", "#B2BF9F", "#D9674E"],
            )
            color = alt.Color("mood:N", scale=color_scale, legend=None)

            brush = alt.selection_interval(encodings=["x"])
            click = alt.selection_multi(encodings=["color"])

            points = (
                alt.Chart()
                .mark_circle()
                .encode(
                    alt.X("monthdate(date):T", title=None),
                    alt.Y(
                        "y:Q",
                        title="Mood Index",
                        scale=alt.Scale(domain=[-2, 6]),
                    ),
                    color=alt.condition(brush, color, alt.value("lightgray")),
                    size=alt.Size("size:Q", legend=None),
                    tooltip=['date:T', 'mood:N']
                )
                .properties(height=180)
                .add_selection(brush)
                .transform_filter(click)
            )

            bars = (
                alt.Chart()
                .mark_bar()
                .encode(
                    x=alt.X('count()', title=None),
                    y=alt.Y("mood:N", sort=mood_collection, title=None),
                    color=alt.condition(click, color, alt.value("lightgray")),
                    # order=alt.Order('count()', sort='ascending'),
                    opacity=alt.value(0.6)
                )
                .transform_filter(brush)
                .properties(
                    height=180,
                )
                .add_selection(click)
            )

            mood_chart = alt.vconcat(points, bars, data=mood_source)
            return mood_chart

    @classmethod
    def life_keywords(cls, k_data: dict, d_range):
        k_datas = cls.range_date_data(k_data, d_range)
        keys = cls.get_key_words(k_datas)
        keys_num = cls.get_keys_num(keys)
        if len(keys_num) > 0:
            data = [
                {"name": name, "value": value}
                for name, value in keys_num
            ]
            key_cloud = {
                "series": [{
                    "type": "wordCloud", 
                    "data": data,
                    "shape": 'circle',
                }]}
            key_cloud = {
                "series": [
                    {
                        "type": "wordCloud",
                        "data": data,
                        "shape": "circle",  # 词云图的形状，可以是'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star'
                        "width": "80%",  # 图的宽度
                        "height": "80%",  # 图的高度
                        "gridSize": 20,
                        "rotationRange": [0, 0],
                    }
                ]
            }
            return key_cloud
        else:
            return None