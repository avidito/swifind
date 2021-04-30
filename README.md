# Swifind
[![Build Status](https://www.travis-ci.com/avidito/swifind.svg?branch=main)](https://www.travis-ci.com/avidito/swifind)
[![codecov](https://codecov.io/gh/avidito/swifind/branch/main/graph/badge.svg?token=E2S225BSG4)](https://codecov.io/gh/avidito/swifind)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/avidito/swifind/blob/main/LICENSE)

## Overview
**Swifind** is web scraping function builder. It is a toolset to increase web scraping function simplicity and modularity. It came with its scripting language (`swipl`) to plan web scraping and crawling strategies. `swipl` script will be interpreted to Python sequence of function, makes it easier to recreate, reuse or modify web scraping script. It can be run as a standalone script or even attached to existing project.

Please check these amazing libraries that I used to develop this project:
1. [**BeautifullSoup**](https://github.com/waylan/beautifulsoup) to parse HTML page.
2. [**Request**](https://github.com/pallets/click) to retrieve website page.
3. [**lxml**](https://github.com/lxml/lxml) to enable lxml parsing with BeautifulSoup.

## Requirements
- Python >= 3.6

## Workflow
**Swifind** work in three simple phase:

### Initiation
`Catfish` initiated with `swipl` script path as an argument. `Catfish` will interpret, validate and extract information from `swipl` script. It will store the information into sequence of function that stored in `Strategy` in form of `Plan`. `Catfish` uses `Bag` as a container for extracted or scraped data.

<details close>
<summary><b>How it works?</b></summary>
<br>
<img src="https://github.com/avidito/swifind/blob/doc/doc/interpretation_flow.PNG" alt="interpretation_flow" width="600"/>
<br>

1. `swipl` script will be validated by `Validator`. `Validator` will check syntax validity of each line or block of component. If there is an error, exception will raised. All of validated component will be parsed into *validated components*.
2. *Validated components* will be used to generated *plan blueprint* with `Extractor`. `Extractor` will return function and initiated `Plan`.
3. `Plan` will be assembled to linked list of `Plan`. This sequence of `Plan` is assigned to `Strategy` that attached to existing `Catfish`.
4. `Catfish` will utilize its `Strategy` to do scraping and crawling activity.
</details>

### Swimming
`Catfish` execute all function that assigned to `Strategy`. Each `Plan` in `Strategy` will be execute from `Strategy` origin. For data collection activity, each scraped information will be stored in `Bag`.

<details close>
<summary><b>Swipl Activity</b></summary>
<br>
Currently, there are two activity that available in `swipl`:

- **ORIGIN**: define starting point of `Catfish` (first page).
- **PICK**: define information extraction activity.

For more info about `swipl` activity definition and usage, [read this doc](https://github.com/avidito/swifind/blob/doc/doc/swipl_doc.md).
</details>

### Unpacking
`Catfish` return all collected items inside its `Bag`. `Bag` also contains activity or journey logs that can be retrieved with `Catfish` unpack method.

## Example
For example, imagine there is a website (http://example.com) with following HTML structure:
```html
<body>
  <div class="container">
    <h1>Title Example</h1>
    <a href="/link">Example Link</a>        
    <ul>
      <li>First Item</li>
      <li>Second Item</li>
      <li>Third Item</li>
    </ul>
  </div>
</body>
```

We then plan to extract several things:
- Title of page, we named it **title**.
- Link of example link, we named it **link**
- Second element of unordered-list, we named it **second_elm**

Below are the `swipl` script to extracted those things, we named it `example.swipl`:
```sh
ORIGIN http://example.com
PICK title 'h1*'
PICK link 'div a' href
PICK second_elm 'ul* li[1]'
```

To use this script, we define Python script as follow:
```python
from swifind.catfish import Catfish

cf = Catfish('example.swipl')
cf.swim()
result = cf.unpack()
```
*above example assume `swipl` and Python in the same directory

Result will contain extracted information as follow:
```python
{
  "items":{
    "title": "Title Example",
    "link": "/link",
    "second_elm": "Second Item"
  }
}
```

## Resources
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Packaging Python Project](https://packaging.python.org/tutorials/packaging-projects/)
