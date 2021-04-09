# Swifind

## Overview
**Swifind** is web scraping function builder. It is toolset to increase web
scraping function simplicity and modularity. It came with its scripting
language (`swipl`) to plan web scraping and crawling strategies. `swipl` script
will be interpreted to Python sequence of action, makes it easier to recreate,
reuse or modify web scraping script. It can be run as a standalone script or
even attach in existing project.

## Workflow
**Swifind** work in three simple step:

### Initiation
This step consist of initiate `Catfish` object. `Catfish` object is interpreter to convert `swipl` script into Python functions. These functions will be stored in `Strategy` object as `Plan` sequences. `Catfish` object also bring `Bag` object to storing information.

### Swimming
This step consist of executing `Plan` in `Strategy`. For data collection activity, each scraped information will be stored in `Bag`. Information inside `Bag` object will be categorized / grouped by `labels`.

### Unpacking
This step consist of unpack `Bag` and load its content to somewhere else. For new journey, `Bag` content will be cleared. `Catfish` object will also create journey log, logs of swimming execution.
