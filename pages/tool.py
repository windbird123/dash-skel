import dash
from dash import html

import dash_bootstrap_components as dbc

from pages.components import guide

dash.register_page(__name__, path="/tool", name="Tool")


def layout(param: str = "") -> html.Div:
    doc = """
    #### Tool
    * sub
    """

    return html.Div(
        [
            dbc.Form(
                [
                    dbc.Input(
                        type="text",
                        name="param",
                        value=param,
                        placeholder="Enter tool name",
                        debounce=True, # 사용자가 Enter 키를 누르거나, 입력 후 focus를 잃을 때(blur) 만 callback이 실행
                        style={"display": "inline-block", "width": "30%"},
                    ),
                    dbc.Button("보기", type="submit", color="primary", n_clicks=0),
                ],
                action="/tool",
                method="GET",
                prevent_default_on_submit=False,
            ),
            html.Div(f"Server side rendering: {param}"),
            guide.ui(doc),
        ]
    )
