# import streamlit as st
# import datetime
# import pandas as pd
# import numpy as np



# class DateSorter:

#     def __init__(self, tip, state) -> None:
#         self.tip = tip
#         self.state = state
#         # self.state.key = 'date_range'
#         # self.state['today_month'] = self.get_current_month()
#         self.state['select_month'] = self.get_current_month
#         # self.state['date_range'] = self.get_1month_days(self.get_current_month)
#         # self.state['today_year_month'] = datetime.date.today()

#     def get_1month_days(self, your_month):
#         print("🧡select_month", self.state['select_month'])
#         year, month = map(int, your_month.split('-'))
#         first_day = datetime.date(year, month, 1)
#         if month == 12:
#             last_day = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
#         else:
#             last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
#         date_range = pd.date_range(start=first_day, end=last_day)
#         return date_range


#     def get_previous_month(self):
#         year, month = map(int, self.state['select_month'].split('-'))
#         first_day_of_current_month = datetime.date(year, month, 1)
    
#         last_day_of_previous_month = first_day_of_current_month - datetime.timedelta(days=1)
#         previous_month = last_day_of_previous_month.strftime("%Y-%m")
#         self.state['select_month'] = previous_month
#         self.state['date_range'] = self.get_1month_days(previous_month)
#         print("💙", previous_month)
#         # self.get_1month_days()
#         return previous_month

#     def get_next_month(self):
#         year, month = map(int, self.state['select_month'].split('-'))
#         if month == 12:
#             next_month_date = datetime.date(year + 1, 1, 1)
#         else:
#             next_month_date = datetime.date(year, month + 1, 1)
        
#         next_month = next_month_date.strftime("%Y-%m")
#         self.state['select_month'] = next_month
#         print("💙", next_month)
#         self.state['date_range'] = self.get_1month_days(next_month)
#         # self.get_1month_days()
#         return next_month

#     def get_current_month(self):
#         # 获取当前日期
#         today = datetime.date.today()
#         # 格式化为 "YYYY-MM"
#         current_month = today.strftime("%Y-%m")
#         self.state['select_month'] = current_month
#         print("💛", current_month)
#         self.state['date_range'] = self.get_1month_days(current_month)
#         # self.get_1month_days()
#         return current_month

#     def get_d(self):
#         date_selector = st.container(border=True)
#         self.state
#         with date_selector:
#             col1, col2, col3, buff, col4 = st.columns([0.3,0.3,1,0.3,1.5])
#             with col4:
#                 with st.container():
#                     custome_date = st.popover("Select Custom Date", use_container_width=True)
#                     with custome_date:
#                         st.radio(
#                             "Set 👇",
#                             ["2 week", "3 month", "6 months", "1 year"],
#                         )
#                         st.date_input(
#                             "Select Specific time period",
#                             (datetime.date(today.year, today.month, 1), datetime.date(today.year, today.month, today.day)),
#                             format="MM.DD.YYYY",
#                             key="date_input"
#                             )
#                         st.button("submit")
#             with col1:
#                 with st.container():
#                     st.button("◀", use_container_width=True, on_click=lambda: self.get_previous_month())
#             with col2:
#                 with st.container():
#                     st.button("▶", use_container_width=True, on_click=lambda: self.get_next_month())
#             with col3:
#                 st.button('date', disabled=False, use_container_width=True, on_click=lambda: self.get_current_month())
                
#         return date_selector


# if __name__ == "__main__":

#     states = st.session_state

#     today = datetime.date.today()
#     formatted_date = today.strftime("%Y-%m-%d")

#     st.session_state['date'] = formatted_date
#     select_date = DateSorter(tip="Select Specific time period", state=states)
#     d_selector = select_date.get_d()

#     select_date.get_current_month()
#     date_range = select_date.state['date_range']
#     st.write(date_range)
#     # st.write(date_range)
#     st.write(date_range.size)

#     data = {
#         'number': np.random.normal(loc=5, scale=1, size=date_range.size)
#     }
#     df = pd.DataFrame(data=data, index=date_range)
#     st.line_chart(df)



# import streamlit as st
# import datetime
# import pandas as pd
# import numpy as np

# class DateSorter:

#     def __init__(self, tip, state) -> None:
#         self.tip = tip
#         self.state = state
#         if 'select_month' not in self.state:
#             self.state['select_month'] = self.get_current_month()
#         if 'date_range' not in self.state:
#             self.state['date_range'] = self.get_1month_days(self.state['select_month'])

#     def get_1month_days(self, your_month):
#         year, month = map(int, your_month.split('-'))
#         first_day = datetime.date(year, month, 1)
#         if month == 12:
#             last_day = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
#         else:
#             last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
#         date_range = pd.date_range(start=first_day, end=last_day)
#         return date_range

#     def get_previous_month(self):
#         year, month = map(int, self.state['select_month'].split('-'))
#         first_day_of_current_month = datetime.date(year, month, 1)
#         last_day_of_previous_month = first_day_of_current_month - datetime.timedelta(days=1)
#         previous_month = last_day_of_previous_month.strftime("%Y-%m")
#         self.state['select_month'] = previous_month
#         self.state['date_range'] = self.get_1month_days(previous_month)
#         st.experimental_rerun()  # Refresh the page

#     def get_next_month(self):
#         year, month = map(int, self.state['select_month'].split('-'))
#         if month == 12:
#             next_month_date = datetime.date(year + 1, 1, 1)
#         else:
#             next_month_date = datetime.date(year, month + 1, 1)
#         next_month = next_month_date.strftime("%Y-%m")
#         self.state['select_month'] = next_month
#         self.state['date_range'] = self.get_1month_days(next_month)
#         st.experimental_rerun()  # Refresh the page

#     def get_current_month(self):
#         today = datetime.date.today()
#         current_month = today.strftime("%Y-%m")
#         self.state['select_month'] = current_month
#         self.state['date_range'] = self.get_1month_days(current_month)
#         st.experimental_rerun()  # Refresh the page

#     def get_d(self):
#         date_selector = st.container()
#         with date_selector:
#             col1, col2, col3, buff, col4 = st.columns([0.3, 0.3, 1, 0.3, 1.5])
#             with col4:
#                 with st.container():
#                     custome_date = st.expander("Select Custom Date")
#                     with custome_date:
#                         st.radio(
#                             "Set 👇",
#                             ["2 week", "3 month", "6 months", "1 year"],
#                         )
#                         st.date_input(
#                             "Select Specific time period",
#                             (datetime.date.today(), datetime.date.today()),
#                             format="MM.DD.YYYY",
#                             key="date_input"
#                         )
#                         st.button("submit")
#             with col1:
#                 with st.container():
#                     st.button("◀", use_container_width=True, on_click=lambda: self.get_previous_month())
#             with col2:
#                 with st.container():
#                     st.button("▶", use_container_width=True, on_click=lambda: self.get_next_month())
#             with col3:
#                 st.button('date', use_container_width=True, on_click=lambda: self.get_current_month())

#         return date_selector

# if __name__ == "__main__":
#     states = st.session_state
#     today = datetime.date.today()
#     formatted_date = today.strftime("%Y-%m-%d")
#     st.session_state['date'] = formatted_date
#     select_date = DateSorter(tip="Select Specific time period", state=states)
#     d_selector = select_date.get_d()
    
#     date_range = select_date.state['date_range']
#     st.write(date_range.size)

#     data = {
#         'number': np.random.normal(loc=5, scale=1, size=date_range.size)
#     }
#     df = pd.DataFrame(data=data, index=date_range)
#     st.line_chart(df)



import streamlit as st
import datetime
import pandas as pd
import numpy as np

class DateSorter:

    def __init__(self, tip, state) -> None:
        self.tip = tip
        self.state = state
        if 'select_month' not in self.state:
            self.state['select_month'] = self.get_current_month()
        if 'date_range' not in self.state:
            self.state['date_range'] = self.get_1month_days(self.state['select_month'])

    def get_1month_days(self, your_month):
        year, month = map(int, your_month.split('-'))
        first_day = datetime.date(year, month, 1)
        if month == 12:
            last_day = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
        else:
            last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
        date_range = pd.date_range(start=first_day, end=last_day)
        return date_range

    def get_previous_month(self):
        year, month = map(int, self.state['select_month'].split('-'))
        first_day_of_current_month = datetime.date(year, month, 1)
        last_day_of_previous_month = first_day_of_current_month - datetime.timedelta(days=1)
        previous_month = last_day_of_previous_month.strftime("%Y-%m")
        self.state['select_month'] = previous_month
        self.state['date_range'] = self.get_1month_days(previous_month)
        return True  # 这将确保回调函数返回一个布尔值

    def get_next_month(self):
        year, month = map(int, self.state['select_month'].split('-'))
        if month == 12:
            next_month_date = datetime.date(year + 1, 1, 1)
        else:
            next_month_date = datetime.date(year, month + 1, 1)
        next_month = next_month_date.strftime("%Y-%m")
        self.state['select_month'] = next_month
        self.state['date_range'] = self.get_1month_days(next_month)
        return True  # 这将确保回调函数返回一个布尔值

    def get_current_month(self):
        today = datetime.date.today()
        current_month = today.strftime("%Y-%m")
        self.state['select_month'] = current_month
        self.state['date_range'] = self.get_1month_days(current_month)
        return True  # 这将确保回调函数返回一个布尔值

    def get_time_period(self, days):
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=days)
        date_range = pd.date_range(start=start_date, end=end_date)
        # st.write(date_range)
        self.state['date_range'] = date_range
        return True
        # pass

    def selcet_period(self):
        if self.state.select_period == '2 week':
            self.get_time_period(14)
        elif self.state.select_period == '3 month':
            self.get_time_period(90)
        elif self.state.select_period == '6 months':
            self.get_time_period(180)
        elif self.state.select_period == '1 year':
            self.get_time_period(365)
        return True
        # pass

    def get_d(self):
        date_selector = st.container(border=False)
        with date_selector:
            col1, col2, col3, buff, col4 = st.columns([0.3, 0.3, 0.8, 0.3, 1.5])
            with col4:
                with st.container():
                    custome_date = st.popover("Select Custom Date", use_container_width=True)
                    with custome_date:
                        st.radio(
                            "Set 👇",
                            ["2 week", "3 month", "6 months", "1 year"],
                            index=None,
                            key='select_period',
                            on_change=lambda: self.selcet_period() or st.experimental_rerun()
                        )
                        st.divider()
                        st.date_input(
                            "Select Specific time period",
                            (datetime.date.today(), datetime.date.today()),
                            format="MM.DD.YYYY",
                            key="date_input"
                        )
                        st.button("submit")
            with col1:
                with st.container():
                    st.button("◀ ", use_container_width=True, on_click=lambda: self.get_previous_month() or st.experimental_rerun())
            with col2:
                with st.container():
                    st.button(" ▶", use_container_width=True, on_click=lambda: self.get_next_month() or st.experimental_rerun())
            with col3:
                today = datetime.date.today()
                current_month = '📍 Back to ' + today.strftime("%Y-%m")
                st.button(current_month, use_container_width=True, on_click=lambda: self.get_current_month() or st.experimental_rerun())

        return date_selector

if __name__ == "__main__":
    states = st.session_state
    today = datetime.date.today()
    formatted_date = today.strftime("%Y-%m-%d")
    if 'date' not in st.session_state:
        st.session_state['date'] = formatted_date

    select_date = DateSorter(tip="Select Specific time period", state=states)
    d_selector = select_date.get_d()
    # select_date.get_current_month()
    date_range = select_date.state['date_range']
    st.write(date_range[0].date(), "~", date_range[-1].date())
    # st.write(select_date.state)
    data = {
        'number': np.random.normal(loc=5, scale=1, size=date_range.size)
    }
    df = pd.DataFrame(data=data, index=date_range)
    st.line_chart(df)
