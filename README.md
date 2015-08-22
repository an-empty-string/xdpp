# xdpp
## What is this?
It's a way to manage your `.Xdefaults` file without going through fun `cpp`
and `.Xresources` hoops. Just use YAML instead!

## Why?
`cpp` just wasn't for me. I preferred an easier-to-read and easier-to-maintain
X resources configuration. YAML was the obvious configuration language to me,
and I was bored, so I made this!

## How to use it?
Just edit `Xdefaults.yaml` in this directory. You can `include` things without
conversion by putting them in the `include` key. Otherwise, you probably want
the `config` key. See the file in this repository for an example of my
configuration (for `rxvt-unicode`).

Once you're done configuring it, just `python convert.py > ~/.Xdefaults`.

## Other stuff
- YAML lists get converted to comma-separated strings
- YAML dictionaries are recursively converted to `Xresources` format
    - ... *unless* there is a `custom_filter` defined for the key. read the source!  `
