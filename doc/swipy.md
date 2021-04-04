# Swipy Rule

## Structure
Any plan (`swipy` script) must follow this structure:

## Activity
Activity is `swipy` command or function. It will be validated and translated to Python function sequence. Some activity need arguments. Activity and each arguments seperated with one whitespace. Below are the list of activity in `swipy`:

#### `root`
`root` is command to tell `Swimmer` where is the starting point. `root` must be placed
at the first line of each plan.

Rule:
- accept one argument, URL.
- URL argument must be a string of website URL (without any quotation mark).

Example:
```sh
root https://quotes.toscrape.com/
```
