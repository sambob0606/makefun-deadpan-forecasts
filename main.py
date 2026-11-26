import os

LINE = "Port Sable: 68 degrees, drizzle until noon, then fog so thick the 3 p.m. ferry will navigate by horn and apology."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
