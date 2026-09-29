# editdist

Levenshtein distance: the number of single-character inserts, deletes, and replacements that turn one string into another.

The implementation keeps one row of the matrix, so it is meant for short strings such as names and identifiers.

```python
from editdist import distance, closest

distance("kitten", "sitting")  # 3
closest("kitten", ["sitting", "kit"])
```

```bash
python -m unittest test_editdist.py
```

MIT
