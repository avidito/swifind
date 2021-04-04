# Swipy Rule

## Structure
Any plan (`swipy` script) must follow this structure:

## Activity
Activity is `swipy` command or function. It will be validated and translated to Python function sequence. Some activity need arguments. Activity and each arguments seperated with one whitespace. Below are the list of activity in `swipy`:

### `root`
`root` is command to tell `Swimmer` where is the starting point. `root` must be placed
at the first line of each plan.

Rule:
- must be called with one argument: `URL`.
- `URL` argument must be a string, contain website's URL (without any quotation mark).

Example:
```sh
root https://quotes.toscrape.com/
```

### `collect`
`collect` is command to tell `Swimmer` what to collect/scrape from page and save it in its bucket.

Rule:
- must be called two arguments, `ID` and `PATH`.
- `ID` argument must be a string, contain tag or identifier for collected items in bucket (for comparison, it same as key in dictionary).
- `PATH` argument must be a string, contain CSS path of element (with single quotation mark).

Exaple:
```sh
collect title 'body > div > div.row.header-box > div.col-md-8 > h1 > a'
```
