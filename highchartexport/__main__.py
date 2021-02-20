from . import save
import argparse
import os
import json


def main():
    parser = argparse.ArgumentParser(description="Create PNG image file from highchart configuration",
            allow_abbrev=False)


    parser.add_argument("--in", action="store", type=str, dest="json_file")
    parser.add_argument("--out", action="store", type=str, dest="image_file", default="imagefile.png")
    parser.add_argument("--json", action="store", type=str, dest="config")
    parser.add_argument("--chart", action="store", type=str, dest="constr", default="Chart", choices=["Chart", "Map", "StockChart"])
    parser.add_argument("--width", action="store", type=str, dest="width", default=False)
    parser.add_argument("--scale", action="store", type=str, dest="scale", default=False)
    parser.add_argument("--type", action="store", type=str, dest="type", default="png", choices=["png", "jpeg", "svg", "pdf"])


    args = parser.parse_args()

    parameter = vars(args)

    if parameter["config"] is None and parameter["json_file"] is not None:
        if not os.path.isfile(parameter["json_file"]):
            raise FileNotFoundError(f'{parameter["json_file"]} not found')

        _file = parameter.pop("json_file")

        with open(_file) as _f:
            config = json.load(_f)
    elif parameter["config"] is not None:
        config = parameter.pop("config")
    else:
        raise Exception("At least provide highchart configuration in argument.\nExample\n --json {\"series\": [{\"data\":[1,2,3,4,5,6]}]}")

    if 'config' in parameter:
        parameter.pop('config')


    filename = parameter.pop("image_file")
    file_type = parameter.pop("type")
    save(config=config, filename=filename, file_type=file_type, **parameter) 
