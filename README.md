# pandas-stubs
(Work-in-progress, contributions are welcome) Stubs for common pandas classes for static type checking (e.g. with mypy).

Files in this repo are initially generated by `stubgen` (part of `mypy`) running on `pandas` source code. Manual edits are made on top of that to make type-checking work. This is work in progress.

### How to use this:
Instructions for using with `mypy`:
1. Clone the repo to some folder, e.g. `~/pandas-stubs`
2. Add the above folder path into either `MYPYPATH` environment variable, or as part of the `mypy_path` variable in a config file. See https://mypy.readthedocs.io/en/latest/config_file.html#import-discovery for details about the mypy config file.
3. Run `mypy` to typecheck.

### Code examples:

```
# mypy should have no problem checking this annotated function:
def filter_col(df: pd.DataFrame, col: str, val: str) -> pd.Series:
    s = df[col]
    s = s.loc[s == val]
    return s


# reveal_type should know the types of all these:
df = pd.read_csv(csv_file_path)  # --> pandas.DataFrame
s = df['col1'] * 100  # --> pandas.Series

ts = pd.Timestamp('2020-01-01')  # --> pandas.Timestamp
delta = pd.Timestamp.now() - ts  # --> pandas.Timedelta
ts2 = ts + pd.Timedelta(10, unit='D')  # --> pandas.Timestamp

dates = pd.date_range('2020-01-01', '2022-01-01', freq='D')  # --> pandas.DatetimeIndex
dates[0]  # --> pandas.Timestamp
```


# TODO
- make into a pip package
...
