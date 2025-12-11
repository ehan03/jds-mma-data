# standard library imports
import os
import sqlite3

# third party imports
import pandas as pd

# local imports


def calc_db_summary_stats() -> None:
    data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data")
    db_path = os.path.join(os.path.dirname(__file__), data_dir, "ufc.db")
    source_name_map = {
        "bestfightodds": "Best Fight Odds",
        "betmma": "Bet MMA",
        "espn": "ESPN",
        "fightmatrix": "Fight Matrix",
        "fightoddsio": "FightOdds.io",
        "mmadecisions": "MMA Decisions",
        "sherdog": "Sherdog",
        "tapology": "Tapology",
        "ufcstats": "UFC Stats",
        "wikipedia": "Wikipedia",
    }

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get list of tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]

    summary = []
    for table in tables:
        # Count rows
        cursor.execute(f"SELECT COUNT(*) FROM {table};")
        row_count = cursor.fetchone()[0]

        summary.append(
            {
                "table": table,
                "n_rows": row_count,
            }
        )
    conn.close()

    # Create dataframe
    df_summary = pd.DataFrame(summary)
    df_summary["group_source"] = df_summary["table"].apply(
        lambda x: "Mapping Tables"
        if x.endswith("_MAPPING")
        else source_name_map[x.split("_")[0]]
    )

    # Group and aggregate
    grouped = (
        df_summary.groupby("group_source")
        .agg(n_tables=("table", "count"), total_rows=("n_rows", "sum"))
        .reset_index()
    )
    total_rows = df_summary["n_rows"].sum()
    grouped["pct_of_db"] = grouped["total_rows"] / total_rows * 100

    print(grouped)
    print(f"Total Rows in DB: {total_rows}")


if __name__ == "__main__":
    calc_db_summary_stats()
