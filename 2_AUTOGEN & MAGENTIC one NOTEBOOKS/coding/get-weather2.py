import argparse
import sys
import json
from datetime import datetime
from pathlib import Path

import requests

def parse_args():
    p = argparse.ArgumentParser(
        description="Fetch current weather from OpenWeatherMap and save to a JSON file."
    )
    loc = p.add_mutually_exclusive_group(required=True)
    loc.add_argument(
        "-q", "--city", metavar="CITY",
        help="City name, e.g. 'London' or 'London,UK'"
    )
    loc.add_argument(
        "--lat", type=float,
        help="Latitude, e.g. 44.34"
    )
    p.add_argument(
        "--lon", type=float,
        help="Longitude, e.g. 10.99 (required if --lat is used)"
    )
    p.add_argument(
        "--apikey", required=True,
        help="Your OpenWeatherMap API key"
    )
    p.add_argument(
        "--units",
        choices=["standard", "metric", "imperial"],
        help="Units of measurement (default: standard)"
    )
    p.add_argument(
        "--lang",
        help="Language code for response (e.g. en, fr, es)"
    )
    args = p.parse_args()

    if args.lat is not None and args.lon is None:
        p.error("--lon is required when --lat is provided")
    return args

def build_params(args):
    params = {"appid": args.apikey}
    if args.city:
        params["q"] = args.city
    else:
        params["lat"] = args.lat
        params["lon"] = args.lon
    if args.units:
        params["units"] = args.units
    if args.lang:
        params["lang"] = args.lang
    return params

def main():
    args = parse_args()
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = build_params(args)

    try:
        resp = requests.get(base_url, params=params, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        data = resp.json()
    except ValueError:
        print("Failed to parse JSON response", file=sys.stderr)
        sys.exit(1)

    # Generate filename: weather_<location>_<UTC-timestamp>.json
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    if args.city:
        loc_tag = args.city.replace(" ", "_").replace(",", "")
    else:
        loc_tag = f"{args.lat}_{args.lon}"
    filename = f"weather_{loc_tag}_{ts}.json"
    outpath = Path.cwd() / filename

    try:
        outpath.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except OSError as e:
        print(f"Could not write file {outpath}: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Weather data saved to {outpath}")

if __name__ == "__main__":
    main()