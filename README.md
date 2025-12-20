# Unifying Multi-Source Data for Mixed Martial Arts

Repository housing all supplementary material (source code, data, documentation)


## Directory Structure

```bash
├───data
│   ├───clean
│   │   ├───Best Fight Odds
│   │   ├───Bet MMA
│   │   ├───ESPN
│   │   ├───Fight Matrix
│   │   ├───FightOdds.io
│   │   ├───MMA Decisions
│   │   ├───Sherdog
│   │   ├───Tapology
│   │   ├───UFC Stats
│   │   └───Wikipedia
│   └───raw
│       ├───Best Fight Odds
│       ├───Bet MMA
│       ├───ESPN
│       ├───Fight Matrix
│       ├───FightOdds.io
│       ├───MMA Decisions
│       ├───Sherdog
│       ├───Tapology
│       ├───UFC Stats
│       └───Wikipedia
├───notebooks
│   ├───cleaning
│   └───matching
└───src
    ├───database
    │   └───data_models
    └───scraping
        ├───miscellaneous
        └───scrapy_ufc
            ├───items
            ├───pipelines
            └───spiders
```


## Development Setup

1. Clone this repository. If you would like to clone the database file as well, make sure to have [Git LFS](https://git-lfs.com/) installed. This is optional since the database file can be built programmatically later (see [Database Creation](#database-creation)).
2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
3. Create and activate the virtual environment by running the following from the root of the repository:
```bash
uv venv
source .venv/bin/activate     # macOS/Linux
# OR
.venv\Scripts\activate        # Windows
```
4. Install project dependencies by running:
```bash
uv sync
```


## Usage

### Data Collection

The following information pertains to data files inside the `data/raw/` folder.


For Best Fight Odds data:
1. Download `straight_bets.zip` from https://github.com/iankotliar/UFC_Final/tree/master/data/bestfightodds_data and rename to `straight_over_time.zip`
2. Download `moneyline_data_at_close.zip` from the same repository, extract, and rename the singular file `moneyline_data_at_close.csv` to `closing_with_props.csv`


For all other sources:
1. Navigate into the Scrapy project folder:
```bash
cd src/scraping/scrapy_ufc
```
2. For some given Scrapy spider with name `<spider>`, start crawling by running
```bash
scrapy crawl <spider>
```
3. Specifically for Tapology spiders that scrape bouts, fighters, and gyms, it is necessary to scrape in batches of 1000 links to avoid temporary IP blocks. This works best in conjunction with IP rotation (e.g., through a VPN). To crawl the `<n>`-th batch of 1000 links, run the following:
```bash
scrapy crawl <spider> -a batch_num=<n>
```


It is recommended that one does NOT rerun the spiders, as the raw scrapes are already available in `data/raw/` and running the spiders one by one takes a few weeks of continuous crawling. Moreover, it is highly likely that one or more of the data sources has changed their website structure since January 2025, which would break the existing CSS selector logic. Consequently, raw scraping may not be fully reproducible, but all raw and intermediate artifacts are archived, and the logic to transform those artifacts should be reproducible in its entirety.


### Cleaning

All data cleaning logic outside what is already embedded inside the Scrapy pipelines can be found inside `notebooks/cleaning/` as Jupyter notebooks organized by data source and should be executed in the order of filename prefix numbering. This ordering can be made somewhat arbitrary, however, as long as the logic for cleaning Tapology data is executed before that of Best Fight Odds data due to downstream dependencies. Running these notebooks will output all CSVs found in `data/clean/`, excluding the mapping tables (see "Record Linkage" for this).


### Record Linkage

All record linkage logic can be found inside `notebooks/matching/` as Jupyter notebooks and should be executed in the order of filename prefix numbering.


### Database Creation

1. Navigate to the `src/database/` folder from the repository root:
```bash
cd src/database
```
2. Run the following to initialize the database file and populate all tables using the CSVs in `data/clean/`:
```bash
uv run db_creator.py
```
3. To calculate database summary statistics, run the following:
```bash
uv run summary_stats.py
```


## Documentation

High-level overviews of every table and column in the database can be found in `data/` inside the `Data Dictionary.xlsx` Excel workbook.