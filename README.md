# Swifind

## Overview
**Swifind** is web scraping function builder. It is toolset to increase web
scraping function simplicity and modularity. It came with its scripting
language (`swipl`) to plan web scraping and crawling strategies. `swipl` script
will be interpreted to Python sequence of action, makes it easier to recreate,
reuse or modify web scraping script. It can be run as a standalone script or
even attached to existing project.

## Workflow
**Swifind** work in three simple step:

### Initiation
`Catfish` initiated with `swipl` script path as an argument. `Catfish` will interpret, validate and extract information from `swipl` script. It will store the information into sequence of function that stored in `Strategy` in form of `Plan`. `Catfish` uses `Bag` as a container for extracted or scraped data.

<details open>
<summary>How it works?</summary>
-- image --
<br>

1. `swipl` script will be validated by `Validator`. `Validator` will check syntax validity of each line or block of component. If there is an error, exception will raised. All of validated component will be parsed into *validated components*.
2. *Validated components* will be used to generated *plan blueprint* with `Extractor`. `Extractor` will return function and initiated `Plan`.
3. `Plan` will be assembled to linked list of `Plan`. This sequence of `Plan` is assigned to `Strategy` that attached to existing `Catfish`.
4. `Catfish` will utilize its `Strategy` to do scraping and crawling activity.
</details>

### Swimming
`Catfish` execute all function that assigned to `Strategy`. Each `Plan` in `Strategy` will be execute from `Strategy` origin. For data collection activity, each scraped information will be stored in `Bag`.

### Unpacking
`Catfish` return all collected items inside its `Bag`. `Bag` also contains activity or journey logs that can be retrieved with `Catfish` unpack method.

# Swipl Activity
Currently, there are two activity that available in `swipl`:
- **ORIGIN**: define starting point of `Catfish` (first page).
- **PICK**: define information extraction activity.

For more info about `swipl` activity definition and usage, read this doc.

# Example
-- HTML example
-- Swipl script example
-- Python script example
-- Return value example
