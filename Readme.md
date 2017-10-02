# Wayback
This is a simple tool to scrape every version
of a url stored in the [Wayback Machine](https://archive.org/web/).

## Example Usage
```
python -m wayback.scrape --urls google.com facebook.com --start-date 2017-09-01 \
  --end-date 2017-09-02 --output-dir scrape
```
