# robofont-drawing-helpers

A few random drawing helpers I'm working on for RoboFont

**Making extra shortkey combos**

It is always tricky to find simple, new shortcut key combos that aren't yet used. You can make this much easier by converting your `caps lock` key into a "hyper" key – `ctrl+optn+cmmd+shft`, all at once. Use this guide to set it up, if that's appealing to you:

https://brettterpstra.com/2017/06/15/a-hyper-key-with-karabiner-elements-full-instructions/

## `add-sloped-grid-of-guides.py`

Use this to add a grid of guides. If you have set an italic angle in a UFO, the guides will follow it.

You can tweak the code to change the size and basis of the grid sizing:

```
## Set grid size or number of divisions in UPM2
# gridSize = 25                         ### uncomment this to use units for grid size (and comment-out the two lines below)
divisions = 20                          ### uncomment this to use divisions of UPM for grid size (and comment-out the line above)
gridSize = int(round(UPM / divisions))  ### uncomment this to use divisions of UPM for grid size
```

You can also adjust the "magnetism" of guides with the final lines of code:

```
# make guides magnetic
for guide in g.guides:
    # prevent vertical guides from being far more "magnetic"
    if guide.angle == 90:
        guide.magnetic = 10
    else:
        guide.magnetic = 10
```

## `remove-selected-glyphs-from-font.py`

For some reason, it is weirdly hard to _really_ remove glyphs from a UFO, with RoboFont.

This script removes selected glyphs from the `glyphs` folder, from glyphOrder, kerning, and components.

I have it setup to `ctrl+optn+cmmd+shft+delete`

## `duplicate-selected-glyphs-w_new_suffix.py` and `make-selected-alt_glyphs-default.py`

One of the simplest and most effective ways to experiment with different glyphs is to quickly make alternates.

The `duplicate` script prompts your for a new suffix (e.g. `alt` or `italic`), then duplicates all selected glyphs with this suffix.

The `make default` script takes suffixed glyphs, and makes them the non-suffixed versions. The previous non-suffixed glyphs get a suffix `replaced_by_` and then the suffix that replaced them. This is a bit messy, but I couldn't think of anything more clear.

These can then be turned on in the Space Center, for contextual viewing.

Caveat: the `make default` script messes with the glyph order in the UFO a bit. So, save your UFO before using it, in case you don't like what it does.

I have the `duplicate` script setup to `ctrl+optn+cmmd+shft+J` (like the "copy layer" shortcut in Photoshop).
I have the `make default` script setup to `ctrl+optn+cmmd+shft+H` (the key next to `J`).

## `duplicate-sel_glyphs-w_suffix-all_fonts.py`

This duplicates a glyph with a suffix in all open fonts.

If you're working on many masters at once, this can be handy.
