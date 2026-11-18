"""Data check for Task A (which conference is this paper from?) on MustCite-Mini.

Loads the data with load_task_a() from mustcite.py, prints the number of examples
per venue (class) and per split, and writes samples.md with three examples of each venue.
"""
import pandas as pd

from mustcite import VENUES, SPLITS, load_task_a


def main():
    train, val, test = load_task_a()
    splits = dict(zip(SPLITS, (train, val, test)))

    # Examples per class and per split
    counts = pd.DataFrame({name: df.venue.value_counts() for name, df in splits.items()})
    counts = counts.reindex(VENUES)[list(SPLITS)]
    counts["total"] = counts.sum(axis=1)
    counts.loc["total"] = counts.sum()
    print("Papers per venue and split:")
    print(counts.to_string(), "\n")

    # Does every class appear in every split? What years does each split cover?
    for name, df in splits.items():
        missing = set(VENUES) - set(df.venue)
        years = f"{df.year.min()}-{df.year.max()}"
        print(f"{name}: {len(df)} papers, years {years}, missing venues: {sorted(missing) or 'none'}")

    # Samples: three examples of each venue, from the training split
    with open("samples.md", "w", encoding="utf-8") as f:
        f.write("# Samples from the training split (3 per venue)\n\n")
        for venue in VENUES:
            f.write(f"## {venue.upper()}\n\n")
            for _, row in train[train.venue == venue].sample(3, random_state=0).iterrows():
                abstract = row.abstract if len(row.abstract) <= 600 else row.abstract[:600] + "..."
                f.write(f"**{row.title}** ({row.year})\n\n{abstract}\n\nLabel: {venue} (index {row.label})\n\n")
    print("\nWrote samples.md")


if __name__ == "__main__":
    main()
