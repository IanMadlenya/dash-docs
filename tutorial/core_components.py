# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event
from pandas_datareader import data as web
from datetime import datetime as dt
import plotly.graph_objs as go
import json
import styles

from server import app

layout = html.Div(children=[
    html.H1('Dash Core Components'),

    dcc.Markdown('''
        Dash ships with supercharged components for interactive user interfaces.
        A core set of components, written and maintained by the Dash team,
        is available in the `dash-core-components` library.

        The source is on GitHub at [plotly/dash-core-components](https://github.com/plotly/dash-core-components).
    '''.replace('    ', '')),

    html.Hr(),
    html.H3('Dropdown'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
)''', language='python', customStyle=styles.code_container),
    dcc.Dropdown(options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ], value="MTL", id='section2-dropdown-1'),

    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    multi=True,
    value="MTL"
)''', language='python', customStyle=styles.code_container),
    dcc.Dropdown(options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ], multi=True, value="MTL", id='section2-dropdown-2'),

    html.Hr(),
    html.H3('Date Picker'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    id='date-picker-single',
    date=dt(1997, 5, 10)
)
''', language='python', customStyle=styles.code_container),

    dcc.DatePickerSingle(
        id='section2-datepickersingle-1',
        date=dt(1997, 5, 10)
    ),

    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    id='date-picker-range',
    start_date=dt(1997, 5, 3),
    end_date_placeholder_text='Select a date!'
)
''', language='python', customStyle=styles.code_container),

    dcc.DatePickerRange(
        id='section2-datepickerrange-1',
        start_date=dt(1997, 5, 3),
        end_date_placeholder_text='Select a date!'
    ),

    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerSingle(
    id='date-picker-single',
    initial_visible_month=dt(1997, 5, 5),
    min_date_allowed=dt(1997, 4, 29),
    max_date_allowed=dt(1997, 6, 3),
    show_outside_days=True,
    with_portal=True,
    number_of_months_shown=1,
    placeholder='Try it out!'
)''', language='python', customStyle=styles.code_container),
    dcc.DatePickerSingle(
        id='section2-datepickersingle-2',
        initial_visible_month=dt(1997, 5, 5),
        min_date_allowed=dt(1997, 4, 29),
        max_date_allowed=dt(1997, 6, 3),
        show_outside_days=True,
        with_portal=True,
        number_of_months_shown=1,
        placeholder='Try it out!'
    ),

    dcc.SyntaxHighlighter('''import dash_core_components as dcc
from datetime import datetime as dt

dcc.DatePickerRange(
    id='date-picker-range',
    start_date=dt(1997, 5, 10),
    end_date_placeholder_text="Clear the date!",
    first_day_of_week=3,
    minimum_nights=2,
    min_date_allowed=dt(1997, 4, 29),
    max_date_allowed=dt(1997, 6, 3),
    show_outside_days=True,
    calendar_orientation='vertical',
    number_of_months_shown=2,
    clearable=True,
    day_size=45,
    stay_open_on_select=True,
    reopen_calendar_on_clear=True,
    month_format='MM YY',
    display_format='MMMM D, Y'
)''', language='python', customStyle=styles.code_container),

    dcc.DatePickerRange(
        id='section2-datepickerrange-2',
        start_date=dt(1997, 5, 10),
        end_date_placeholder_text="Clear the date!",
        first_day_of_week=3,
        minimum_nights=2,
        min_date_allowed=dt(1997, 4, 29),
        max_date_allowed=dt(1997, 6, 3),
        show_outside_days=True,
        day_size=45,
        number_of_months_shown=2,
        calendar_orientation='vertical',
        clearable=True,
        stay_open_on_select=True,
        reopen_calendar_on_clear=True,
        month_format='MM YY',
        display_format='MMMM D, Y'
    ),

    html.Hr(),
    html.H3('Slider'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Slider(
    min=-5,
    max=10,
    step=0.5,
    value=-3,
)''', language='python', customStyle=styles.code_container),
    dcc.Slider(
        min=-5,
        max=10,
        step=0.5,
        value=-3,
        id='section2-slider-1'
    ),

    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Slider(
    min=0,
    max=9,
    marks={i: 'Label {}'.format(i) for i in range(10)},
    value=5,
)''', language='python', customStyle=styles.code_container),
    html.Div(dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) for i in range(10)},
        value=5,
        id='section2-slider-2'
    )),
    html.Hr(),
    html.H3('RangeSlider'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.RangeSlider(
    count=1,
    min=-5,
    max=10,
    step=0.5,
    value=[-3, 7]
)''', language='python', customStyle=styles.code_container),
    dcc.RangeSlider(
        count=1,
        min=-5,
        max=10,
        step=0.5,
        value=[-3, 7],
        id='section2-rangeslider-1'
    ),

    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.RangeSlider(
    marks={i: 'Label {}'.format(i) for i in range(-5, 7)},
    min=-5,
    max=6,
    value=[-3, 4]
)''', language='python', customStyle=styles.code_container),
    html.Div(dcc.RangeSlider(
        marks={i: 'Label {}'.format(i) for i in range(-5, 7)},
        min=-5,
        max=6,
        value=[-3, 4],
        id='section2-rangeslider-2'
    )),

    html.Hr(),
    html.H3('Input'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Input(
    placeholder='Enter a value...',
    type='text',
    value=''
)''', language='python', customStyle=styles.code_container),
    dcc.Input(
        placeholder="Enter a value...",
        value="",
        type='text',
        id='section2-input'
    ),

    html.Hr(),
    html.H3('Checkboxes'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    values=['MTL', 'SF']
)''', language='python', customStyle=styles.code_container),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        values=['MTL', 'SF'],
        id='section2-checklist-1'
    ),

    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    values=['MTL', 'SF'],
    labelStyle={'display': 'inline-block'}
)''', language='python', customStyle=styles.code_container),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        values=['MTL', 'SF'],
        labelStyle={'display': 'inline-block'},
        id='section2-checklist-2'
    ),


    html.Hr(),
    html.H3('Radio Items'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
)''', language='python', customStyle=styles.code_container),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL',
        id='section2-radioitems-1'
    ),

    dcc.SyntaxHighlighter('''import dash_core_components as dcc

dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL',
    labelStyle={'display': 'inline-block'}
)''', language='python', customStyle=styles.code_container),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'},
        id='section2-radioitems-2'
    ),

    html.Hr(),
    html.H3('Markdown'),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc

    dcc.Markdown(\'\'\'
    #### Dash and Markdown

    Dash supports [Markdown](http://commonmark.org/help).

    Markdown is a simple way to write and format text.
    It includes a syntax for things like **bold text** and *italics*,
    [links](http://commonmark.org/help), inline `code` snippets, lists,
    quotes, and more.
    \'\'\')
    '''.replace('  ', ''),
        customStyle=styles.code_container,
        language='python'
    ),

    dcc.Markdown('''
    #### Markdown

    Dash supports [Markdown](http://commonmark.org/help).

    Markdown is a simple way to write and format text.
    It includes a syntax for things like **bold text** and *italics*,
    [links](http://commonmark.org/help), inline `code` snippets, lists,
    quotes, and more.'''.replace('  ', ''),
    containerProps={'className': 'example-container'}),

    html.Hr(),
    html.H3('Graphs'),
    dcc.Markdown('''
    The `Graph` component shares the same syntax as the open-source
    `plotly.py` library. View the [plotly.py docs](https://plot.ly/python)
    to learn more.
    '''.replace('    ', '')),
    dcc.SyntaxHighlighter('''import dash_core_components as dcc
import plotly.graph_objs as go

dcc.Graph(
    figure=go.Figure(
        data=[
            go.Scatter(x=[1, 2, 3], y=[3, 2, 4], mode='lines'),
            go.Scatter(x=[1, 2, 3], y=[4, 1, 5], mode='lines')
        ],
        layout=go.Layout(
            title='Quarterly Results',
            showlegend=False,
            margin=go.Margin(l=20, r=0, t=40, b=20)
        )
    ),
    style={'height': 300},
    id='my-graph'
)''', language='python', customStyle=styles.code_container),
    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Scatter(x=[1, 2, 3], y=[3, 2, 4], mode='lines'),
                go.Scatter(x=[1, 2, 3], y=[4, 1, 5], mode='lines')
            ],
            layout=go.Layout(
                title='Quarterly Results',
                showlegend=False,
                margin=go.Margin(
                    l=20, r=0, t=40, b=20
                )
            )
        ),
        style={'height': 300},
        id="my-graph"
    ),

    html.Div(style={'marginBottom': 50}),

    html.Div(id='hidden', style={'display': 'none'})
])


for k in layout.keys():
    if k == 'hidden':
        continue

    if k in ['section2-rangeslider-2', 'section2-slider-2']:
        layout[k] = html.Div(layout[k],
            className="example-container",
            style=dict({'padding': '40px'})
        )
    elif(k in ['section2-dropdown-1', 'section2-dropdown-2']):
        layout[k] = html.Div(layout[k])
    elif(k in ['section2-datepickersingle-1', 'section2-datepickersingle-2',
               'section2-datepickerrange-1', 'section2-datepickerrange-2']):
        layout[k] = html.Div(layout[k], style={'display': 'inline-block'})
    else:
        layout[k] = html.Div(layout[k], className="example-container")

# add dependencies to all of section2's elements so that they become controlled
@app.callback(
    Output('hidden', 'children'),
    [Input(k, 'value' if 'checklist' not in k else 'values')
     for k in layout.keys() if k != 'hidden'])
def update_hidden_div(*args):
    return ''
