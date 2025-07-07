import os

import dash
import dash_auth
import dash_bootstrap_components as dbc
from dash import html
from dash_extensions.enrich import Dash
from loguru import logger

DASH_USERNAME = os.getenv("DASH_USERNAME", "admin")
DASH_PASSWORD = os.getenv("DASH_PASSWORD", "admin")
VALID_USERNAME_PASSWORD_PAIRS = {DASH_USERNAME: DASH_PASSWORD}

APP_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
app: Dash = Dash(
    __name__,
    use_pages=True,
    pages_folder="pages",  # pages 폴더 경로 수정
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
    assets_folder="assets",  # assets 폴더 경로 수정
    # suppress_callback_exceptions=True,
)

# Flask secret key 설정 (세션 관리용)
app.server.secret_key = os.getenv(
    "FLASK_SECRET_KEY", "your-secret-key-change-in-production-12345"
)

# Basic Authentication 적용
auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)

app.title = "분석 대시보드"

sidebar = html.Div(
    [
        html.Div(
            [
                # width: 3rem ensures the logo is the exact width of the
                # collapsed sidebar (accounting for padding)
                html.Img(src=APP_LOGO, style={"width": "3rem"}),
                html.H2("Sidebar"),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className="fas fa-home me-2"),
                        html.Span("홈"),
                    ],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-wrench me-2"),
                        html.Span("툴"),
                    ],
                    href="/tool",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)

content = html.Div(
    dbc.Spinner(dash.page_container, color="success", size="md"), className="content"
)
app.layout = html.Div([sidebar, content])

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)  # logs 디렉토리 생성
    logger.add(
        "logs/app.log",
        encoding="utf-8",
        rotation="00:00",
        format="{time:YYYY-MM-DD HH:mm:ss.SSS}\t{level}\t{message}",
        level="INFO",
        retention="40 days",
        compression="zip",
        watch=True,
    )

    logger.info("Starts server ...")
    app.run(debug=True, host="0.0.0.0", port=8000)
