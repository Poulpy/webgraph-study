# Webgraph study

## Tests

```
export PYTHONPATH='.'
python tests/test_graph.py
```

## Dependencies

Python 2

## Notes

To replace all tabs by commas in the file RoadNetwork.txt
```
cat resources/RoadNetwork.txt | sed 's/^\(..*\)\t\(..*\)/\1,\2/g' > RoadNetwork.csv
```
