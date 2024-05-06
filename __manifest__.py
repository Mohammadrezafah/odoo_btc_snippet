{
    'name': 'BTC Snippet',
    'version': '1.0',
    'author': 'Reza',
    'depends': ['web', "website"],
    'data': [
        "views/snippet_btc_views.xml",
    ],
    'assets': {
       'web.assets_frontend': [
           '/web/static/lib/Chart/Chart.js',
           '/btc_snippet/static/src/js/btc_chart.js',
       ],
    },
}
