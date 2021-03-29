# highchartexport
Convert highchart configuration into an image file using export server of HighCharts, which is http://export.highcharts.com/


**Installation**

You can use pip command
```terminal
pip install highchartexport
```

**Example**

In terminal
```terminal
highchartexport --json "{\"chart\":{\"type\":\"area\"},\"series\":[{\"data\":[1,2,3,4,5,6],\"name\":\"areaplot\"}]}" --out area_chart.png
```

```terminal
highchartexport --json "{\"chart\":{\"type\":\"area\"},\"series\":[{\"data\":[1,2,3,4,5,6],\"name\":\"areaplot\"}]}" --out area_chart.png --width 2000 --scale 2
```

Pass highchart json file

* For PNG image file
```terminal
highchartexport --in hc_config.json --out area_chart.png --width 2000 --scale 2 --type png
```

* For SVG file
```terminal
highchartexport --in hc_config.json --out area_chart.svg --width 2000 --scale 2 --type svg
```

* For SVG file with StockChart
```terminal
highchartexport --in hc_config.json --out area_chart.svg --chart StockChart --width 2000 --scale 2 --type svg
```

* For PDF file with Map Chart
```terminal
highchartexport --in hc_config.json --out area_chart.svg --chart Map --width 2000 --scale 2 --type pdf
```

Import in your Python program
```python
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

# use default width and scale value
hc_export.save_as_pdf(config=config, filename="bubble.pdf")

# you can pass width and scale value
hc_export.save_as_pdf(config=config, filename="bubble.pdf", width=1000, scale=4)
```
