
from highchartexport import save_as_png, save_as_svg, save_as_pdf, save_as_jpeg, stockChart, reset_basic_config

HIGHCHART_EXAMPLE = {"xAxis": {"categories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]}, 
        "series": [{"data": [1,3,2,4], "type": "line"}, {"data": [5,3,4,2], "type":"line"}]}



save_as_png(HIGHCHART_EXAMPLE, "example.png")
save_as_png(HIGHCHART_EXAMPLE, "example_scale2_width2000.png", scale=2, width=1000)
save_as_png(HIGHCHART_EXAMPLE, "example_map.png", constr="Map")

reset_basic_config()
stockChart()
save_as_png(HIGHCHART_EXAMPLE, "example_stockchart.png")

save_as_jpeg(HIGHCHART_EXAMPLE, "example.jpeg")
save_as_svg(HIGHCHART_EXAMPLE, "example.svg")
save_as_pdf(HIGHCHART_EXAMPLE, "example.pdf")




