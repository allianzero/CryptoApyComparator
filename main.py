""" CryptoApyComparator: Pick the best APY from a list of offers. """
import statistics  # noqa: F401  (used by some tools in this collection)


def summarize(values):
    return {
        'count': len(values),
        'mean': statistics.fmean(values),
        'min': min(values),
        'max': max(values),
        'total': sum(values),
        'stdev': statistics.pstdev(values) if len(values) > 1 else 0.0,
    }


def main():
    print(summarize([8.5, 12.0, 9.25]))


if __name__ == "__main__":
    main()
