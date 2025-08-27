import dash
from dash import html, dcc, Input, Output, State, callback

import dash_bootstrap_components as dbc

from pages.components import guide

dash.register_page(__name__, path="/tool", name="Tool")


def layout(age: int = 0, region: str = "전체") -> html.Div:
    doc = """
    #### Tool
    * sub
    """

    region_options = [
        {"label": "전체", "value": "전체"},
        {"label": "서울", "value": "서울"},
        {"label": "경기", "value": "경기"},
        {"label": "인천", "value": "인천"},
    ]

    return html.Div(
        [
            dbc.Form(
                [
                    # Div 를 사용해야 Label 과 Input 이 한 줄에 나옴 (Row, Col 사용 안함)
                    html.Div(
                        [
                            dbc.Label(
                                "나이 입력",
                                className="fw-bold",
                            ),
                            dbc.Input(
                                type="number",
                                name="age",
                                value=age,
                                placeholder="Enter age",
                                debounce=True,  # 사용자가 Enter 키를 누르거나, 입력 후 focus를 잃을 때(blur) 만 callback이 실행
                                className="mx-2",
                                style={"display": "inline-block", "width": "300px"},
                            ),
                        ],
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.Label(
                                        "지역 선택",
                                        className="fw-bold",
                                    ),
                                    # Dropdown 선택 값은 Form 으로 전달 되지 않아서, 숨겨진 input 으로 저장해 
                                    # submit 시 전달되도록 함. 
                                    dcc.Dropdown(
                                        id="region-input",
                                        options=region_options,
                                        value=region,
                                        placeholder="종목명 또는 코드를 입력하세요...",
                                        searchable=True,
                                        clearable=True,
                                        optionHeight=35,
                                        maxHeight=300,
                                        style={
                                            "width": "100%",
                                            "fontSize": "14px",
                                        },
                                        className="mb-2",
                                    ),
                                    # 숨겨진 input으로 dropdown 값 저장
                                    dcc.Input(
                                        id="region-hidden",
                                        name="region",
                                        type="hidden",
                                        value=region,
                                    ),
                                ]
                            )
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    "보기", type="submit", color="primary", n_clicks=0
                                ),
                                width=3,
                            )
                        ],
                        className="mt-2",
                    ),
                ],
                action="/tool",
                method="GET",
                prevent_default_on_submit=False,
            ),
            html.Hr(),
            html.Div(f"나이: {age}"),
            html.Div(f"지역: {region}"),
            html.Br(),
            html.Br(),
            guide.ui(doc),
        ]
    )


@callback(
    Output("region-hidden", "value"),
    Input("region-input", "value"),
    prevent_initial_call=True,
)
def update_hidden_region_value(selected_value):
    """Dropdown 값이 변경될 때 hidden input 업데이트"""
    return selected_value if selected_value else "전체"
