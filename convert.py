import yaml

def process_fonts(fonts):
    strfonts = []
    for font in fonts:
        strfonts.append("xft:{face}:size={size}".format(**font))
    return "font", strfonts

def process_color(color):
    return color["kind"], "[{opacity}]{color}".format(**color)

filters = {
    "fonts": process_fonts,
    "color": process_color
}

with open("Xdefaults.yaml") as f:
    xdefaults = yaml.load(f)

output = []

def process_kvpl(kvpl, keys=[]):
    output = []
    for key, value in kvpl:
        if key in filters:
            key, value = filters[key](value)

        if isinstance(value, list):
            value = ",".join(value)

        elif isinstance(value, dict):
            output += process_kvpl(value.items(), keys + [key])
            continue

        output.append("{}: {}".format(".".join(keys + [key]), value))

    return output

output = process_kvpl(xdefaults["config"].items())

if "include" in xdefaults:
    for fname in xdefaults["include"]:
        output.append("\n")
        output.append("# {}".format(fname))
        with open(fname) as f:
            output.append(f.read())

print("\n".join(output))
