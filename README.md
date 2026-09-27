# editdist

Levenshtein distance: the number of single-character inserts, deletes, and replacements that turn one string into another.

The implementation keeps one row of the matrix, so it is meant for short strings such as names and identifiers.

```python
from editdist import distance

distance("kitten", "sitting")  # 3
```

```bash
python -m unittest test_editdist.py
```

MIT
