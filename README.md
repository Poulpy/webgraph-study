# Webgraph study

The goal is to calculate parameters for certain graphs :

- barabasi-albert graphs
- edgar-gilbert graphs
- graphs from the stanford database (from the web)

Graph from stanford database are under resources/.

```
# Generate plot from a set of edges
python3 __main__.py file resources/twitchDE.csv
# Plots are under data/plots/
```


## Tests

```
export PYTHONPATH='.'
python3 tests/test_graph.py
```

## Dependencies

Python 3.8.5

Matplotlib 3.3.3

## Notes

To replace all tabs by commas in the file RoadNetwork.txt
```
cat resources/RoadNetwork.txt | sed 's/^\(..*\)\t\(..*\)/\1,\2/g' > RoadNetwork.csv
```

