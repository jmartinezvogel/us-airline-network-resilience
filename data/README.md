# Data

The raw data is **not** committed to this repo (size and licensing), so you need to place one file here before running the notebook.

## 1. Flight data (manual download, required)

**Source:** U.S. Bureau of Transportation Statistics (BTS), *Air Carrier Statistics (Form 41 Traffic), All Carriers*, table **T-100 Domestic Segment (All Carriers)**. It is U.S. government data in the public domain.

1. Open the BTS database page: <https://www.transtats.bts.gov/DatabaseInfo.asp?QO_VQ=EEE> and follow the *Data Tables* link to **T-100 Domestic Segment (All Carriers)**.
2. Click **Download** and set the filters: **Year = 2025**, **Period = all months (January to December)**.
3. Select (at least) these fields: `ORIGIN`, `DEST`, `CLASS`, `DEPARTURES_PERFORMED`, `PASSENGERS`.
4. Download, unzip, and save the CSV in this folder as:

```
data/T_T100D_SEGMENT_ALL_CARRIER.csv
```

BTS occasionally reorganizes its site, so menu names may differ slightly. What matters is that the CSV has the five columns above with exactly those names. The original analysis used a file with 458,361 rows and 22 columns.

Check that the file is valid:

```bash
python scripts/check_data.py
```

## 2. Airport coordinates (automatic)

The notebook downloads `airports.dat` from [OpenFlights](https://github.com/jpatokal/openflights) on its own. If you are offline, save that file in this folder as `data/airports.dat` and the notebook will use it as a fallback.

OpenFlights data is licensed under the [Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/1-0/).
