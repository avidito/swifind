# Swipl Rule

## Structure
Any plan (`swipl` script) must follow this structure:

## Activity
Activity is `swipl` command or function. It will be validated and translated to Python function sequence. Some activity need arguments. Activity and each arguments separated with one whitespace. Below are the list of activity in `swipl`:

### `ROOT`
`origin` is command to tell `Catfish` where is the starting point. `origin` must be placed
at the first line of each plan.

Rule:
- must be called with one argument: `URL`.
- `URL` argument must be a string, contain website's URL (without any quotation mark).

Example:
```sh
ROOT https://quotes.toscrape.com/
```

### `PICK`
`PICK` is command to tell `Swimmer` what to collect/scrape from page and save it in its bucket.

Rule:
- must be called two arguments, `ID` and `PATH`.
- `ID` argument must be a string, contain tag or identifier for collected items in bucket (for comparison, it same as key in dictionary).
- `PATH` argument must be a string, contain CSS path of element (with single quotation mark).

Exaple:
```sh
PICK title 'body > div > div.row.header-box > div.col-md-8 > h1 > a'
```
