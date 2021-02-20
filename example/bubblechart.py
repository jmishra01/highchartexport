import highchartexport as hc_export

config = {
    "chart": {
        "type": 'bubble',
        "plotBorderWidth": 1,
        "zoomType": 'xy'
    },

    "title": {
        "text": 'Highcharts bubbles save in pdf file'
    },

    "series": [{
        "data": [
            [19, 81, 63],
            [98, 5, 89],
            [51, 50, 73],
        ],
        "marker": {
            "fillColor": {
                "radialGradient": { "cx": 0.4, "cy": 0.3, "r": 0.7 },
                "stops": [
                    [0, 'rgba(255,255,255,0.5)'],
                    [1, 'rgba(200, 200, 200, 0.8)']
                ]
            }
        }
    }]
}

hc_export.save_as_pdf(config=config, filename="bubble.pdf")
