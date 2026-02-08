# Telescope Catalog CLI

Portfolio-ready Python project for building, querying, and validating telescope bundles from OTA, mount, and eyepiece datasets.

## What This Project Does

- Loads telescope OTAs, mounts, and eyepieces from dataset files.
- Builds package combinations.
- Generates sorted reports.
- Supports binary-search lookups by OTA or mount type.
- Validates package compatibility (plate type, weight limit, eyepiece usability).

## Project Layout

- `telescope_catalog.py`: command-line entrypoint.
- `OTA.py`, `EP.py`, `Mount.py`: base domain models.
- `Package.py`: package aggregate + validation/sort behavior.
- `OpticalToolbox.py`: optical calculations and helper conversions.
- `Galilean.py`, `Newtonian.py`, `Dobsonian.py`, etc.: concrete subclasses.
- `otas.txt`, `eps.txt`, `mounts.txt`: sample data.
- `tests/test_catalog.py`: automated test suite.

## Run the App

Default report:

```bash
python3 telescope_catalog.py
```

Explicit report command:

```bash
python3 telescope_catalog.py report
```

Search:

```bash
python3 telescope_catalog.py search --ota-type M
python3 telescope_catalog.py search --mount-type D
python3 telescope_catalog.py search --ota-type N --mount-type T
```

Validate packages:

```bash
python3 telescope_catalog.py validate
```

Interactive menu mode:

```bash
python3 telescope_catalog.py menu
```

## Test Everything

Run automated tests:

```bash
python3 -m unittest discover -s tests -v
```

Quick manual smoke tests:

```bash
python3 telescope_catalog.py report
python3 telescope_catalog.py search --ota-type M
python3 telescope_catalog.py validate
```

## Suggested Git Setup

```bash
git init
git add .
git commit -m "Initial commit: telescope catalog CLI"
```
