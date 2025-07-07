import dash
from dash import dcc, html

from pages.components import guide

dash.register_page(__name__, path="/", name="Home")


def layout() -> html.Div:
    doc = """
    #### Online
    * home
    """

    return html.Div(
        [
            dcc.Markdown(
                """
                ## 소개
                  * 기능 우선 (UI 를 위한 코드는 최소화)
                  * Simple and easy dev 
                  
                ## Developed using
                  * [plotly dash](https://dash.plotly.com/): Low-code framework for rapidly building data apps in Python
                """
            ),
            guide.ui(doc),
        ]
    )
