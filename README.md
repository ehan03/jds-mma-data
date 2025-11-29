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

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

2. Create and activate the virtual environment by running the following from the root of the repository:
```bash
uv venv
source .venv/bin/activate     # macOS/Linux
# OR
.venv\Scripts\activate        # Windows
```

3. Install project dependencies by running:
```bash
uv sync
```


## Usage

TODO