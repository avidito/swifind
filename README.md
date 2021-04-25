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

How it works? --

### Swimming
`Catfish` execute all function that assigned to `Strategy`. Each `Plan` in `Strategy` will be execute from `Strategy` origin. For data collection activity, each scraped information will be stored in `Bag`.

### Unpacking
`Catfish` return all collected items inside its `Bag`. `Bag` also contains activity or journey logs that can be retrieved with `Catfish` unpack method.

# Swipl Activity
Currently, there are two activity that available in `swipl`:
- ORIGIN
- ACTIVITY

For more info about `swipl`, read this doc.

# Example
-- HTML example
-- Swipl script example
-- Python script example
-- Return value example
