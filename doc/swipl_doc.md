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

Extra:
- `PATH` argument also accept component indexing. For example, if you want to extract second `div` element, just define it with `div[1]` (it's using 0-indexing).

Example:
```sh
PICK title 'h1 a text'
PICK cls 'div div' class
PICK quote 'div div[1] div div span'
PICK login 'div div div[1] p a' href
```
