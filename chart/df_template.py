# import streamlit as st
import pandas as pd

class DFtemplates:

    def df_misspelled_words():
        df = pd.DataFrame(
            [
                {"✔ right word": None, "❌ wrong word": None}
            ]
        )
        return df
