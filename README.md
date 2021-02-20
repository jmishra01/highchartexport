# highchartexport
Convert highchart configuration into image file

**Install**

pip install highchartexport

**Example**

You can use it as a terminal command
```terminal
highchartexport --json "{\"chart\":{\"type\":\"area\"},\"series\":[{\"data\":[1,2,3,4,5,6],\"name\":\"areaplot\"}]}" --out area_chart.png
```

```terminal
highchartexport --json "{\"chart\":{\"type\":\"area\"},\"series\":[{\"data\":[1,2,3,4,5,6],\"name\":\"areaplot\"}]}" --out area_chart.png --width 2000 --scale 2
```

Pass highchart configuration json file

```terminal
highchartexport --in hc_config.json --out area_chart.svg --width 2000 --scale 2 --type svg
```

```terminal
highchartexport --in hc_config.json --out area_chart.svg --chart StockChart --width 2000 --scale 2 --type svg
```

You can also use it in your code
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

hc_export.save_as_pdf(config=config, filename="bubble.pdf")

```
