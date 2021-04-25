# Swipl Rule

## Structure
Any plan (`swipl` script) must follow this structure:

## Activity
Activity is `swipl` command or function. It will be validated and translated to Python function sequence. Some activity need arguments. Activity and each arguments separated with one whitespace. Below are the list of activity in `swipl`:

### `ORIGIN`
`origin` is command to tell `Catfish` where is the starting point. `origin` must be placed at the first line of each plan.

Rule:
- must be called with one argument: `URL`.
- `URL` argument must be a string, contain website's URL (without any quotation mark).

Example:
```sh
ROOT https://quotes.toscrape.com/
```

### `PICK`
`PICK` is command to tell `Catfish` what to collect/scrape from page and save it in its bucket.

Rule:
- must be called two arguments, `ID` and `PATH`.
- have one optional argument, `ATTR`.
- `ID` argument must be a string, contain tag or identifier for collected items in bucket (for comparison, it same as key in dictionary).
- `PATH` argument must be a string, contain element path (with single quotation mark).
- `ATTR` argument must be a string, contain desired element attribute (class, id, etc.). By default, `ATTR` will be `None`, and will return component text (recursively).

More about `PATH`:
- To use `PATH` component indexing, specify index inside `[]`. For example, if you want to extract second `div` element, define it with `div[1]` (it's using 0-indexing).
- To use `PATH` component attribute selector, specify attribute-value pair inside `{}`. Value must be enclosed with double-quotation mark. For example, if you want to extract `div` with class "row", define it with `div{class="row"}`.
- To enable `PATH` recursive search, add `*` after component names. For example if you want to find the first `span` recursively, define it with `span*`. Recursive search can also be combined with component indexing and  attribute selector.

Example:
```sh
PICK title 'h1* a'
PICK footer 'footer div p a'
PICK cls 'div div' class
PICK quote 'span*{class="text"}'
PICK author 'small*{class="author"}'
PICK third_quote 'div*{class="row"} div*{class="col-md-8"} div[2] span'
PICK login_url 'div*{class="col-md-4"} a*' href
```
