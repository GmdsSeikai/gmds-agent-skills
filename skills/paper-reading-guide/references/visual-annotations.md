# Code-Native Visual Annotation Helper

Use after inspecting the full PDF page and a context-complete clean crop under the [evidence rules](evidence-rules.md#teaching-annotations-on-original-visuals). This helper composes those original pixels with vector text and leaders in memory, then exports a separate PNG. It does not locate evidence, validate a scientific interpretation, or open/write the original PDF. `render_page.py` keeps its existing interface.

## Invocation and Version-1 Input

Read the skill's optional `local-runtime.md` before using Python. The only dependency is the existing PyMuPDF. Save the UTF-8 JSON and outputs in the task's artifact directory:

```text
python <skill-dir>/scripts/annotate_visual.py <checked-crop.png> <callouts.json> --out <task-output-dir> --padding 200 --font-size 18
```

Example for a **synthetic** 600 × 400 pixel crop; replace every target and label placement after inspecting the actual source:

```json
{
  "version": 1,
  "title": "教学标注 · 合成示例",
  "callouts": [
    {"text": "1 输入节点", "target": [50, 60], "label": [-170, 20]},
    {"text": "2 输出节点", "target": [550, 300], "label": [610, 280], "via": [[605, 300]]}
  ]
}
```

- The input is a checked opaque RGB PNG, such as `render_page.py` output. The JSON object requires exactly `version` (integer `1`), `title`, and a nonempty `callouts` list. Each callout requires `text`, `target`, `label`; optional `via` is a list of leader bend points. Unknown fields/versions fail rather than being silently reinterpreted.
- Coordinates are **source PNG pixels**, measured from its top-left, y downward; they are not PDF points or normalized fractions. `target` must be within the image. `label` is the text box's top-left, wholly outside the source rectangle in the added margin. Negative coordinates address top/left margins. `via` uses the same coordinate space and must stay within the canvas. The output places the unchanged-size source at `(padding, padding)` and adds `padding` pixels on all four sides; no DPI conversion or source rescaling occurs. For a PDF crop rendered at a chosen DPI, inspect its actual PNG dimensions before selecting pixel coordinates.
- `--padding` and `--font-size` are positive integers, defaulting to 200 and 18 pixels. The title goes near the canvas's top-left. Labels must fit without intersecting the source, title or another label. Shorten/reposition text or increase padding when rejected; labels do not wrap or shrink automatically. Leaders run from a label's nearest edge through optional `via` points to the target. Adjust `via` and inspect the result to avoid crossing source content or other labels; the helper does not detect scientific symbols or line collisions.
- Write labels and title in the explanation language and include matching numbers/terms in prose. Keep source notation in the original image; do not replace mathematical glyphs with translated approximations. The default is PyMuPDF's bundled `cjk` font, without font download. `--font <font-file>` accepts a caller-supplied font. Every title/label character is checked for a real glyph without fallback; unsupported characters or unavailable fonts fail before output creation. This check cannot prove visual readability: actually view the output. A missing font/tool means use the clean original and prose, not blank labels claimed as success.

## Outputs and Failure Boundaries

The CLI prints absolute paths for `<input-stem>.original.png` (byte-identical copy) and `<input-stem>.annotated.png`. Existing filenames receive exclusive `_2`, `_3`, etc. suffixes, independently for each output, including concurrent collisions and same-basename inputs. It never overwrites the input, existing output, or PDF. Consumers use printed paths rather than predicting a suffix. There is no automatic cleanup.

Invalid source/spec/geometry/font arguments fail before creating the output directory. Filesystem failure during export can leave a clean copy or incomplete file; the pair is not atomic. Keep earlier exports, report the failure, and inspect any retry's printed paths. No annotation output establishes crop completeness, source correctness, readable user display, or user comprehension. Send the teaching annotation with its source location, matching short explanation and clean-original link under the evidence rules.
