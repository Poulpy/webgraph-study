# Webgraph study

The goal is to calculate parameters for certain graphs :

- barabasi-albert graphs
- edgar-gilbert graphs
- graphs from the stanford database (from the web)

Graph from stanford database are under resources/.

```
# To create a barabasi-albert graph and write its parameters in a file
python3 __main__.py ba
# To create an edgar-gilbert graph and write its parameters in a file
python3 __main__.py eg
# To read a file containing edges and write its parameters in a file
python3 __main__.py read resources/twitchDE.csv
```

The parameters are written in a CSV file under data/.

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
