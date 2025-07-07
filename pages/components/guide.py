import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, dcc, html


def ui(doc: str) -> html.Div:
    return html.Div(
        [
            dbc.Button(
                "도움말 펼치기/닫기",
                id="button",
                className="mb-2",
                color="primary",
                n_clicks=0,
            ),
            dbc.Collapse(
                dbc.Card(dbc.CardBody(dcc.Markdown(doc))),
                className="mb-4",
                id="description",
                is_open=False,
            ),
        ]
    )


@callback(
    Output("description", "is_open"),
    [Input("button", "n_clicks")],
    [State("description", "is_open")],
)
def toggle_description(n, is_open):
    if n:
        return not is_open
    return is_open
