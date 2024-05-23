Sure! Here's the updated README with the script named `world-partners.py`.

# CIA World Factbook Data Viewer

This Python script, `world-partners.py`, reads data from a JSON file containing information from the CIA World Factbook. It allows users to input a country name and retrieves information about the country's imported and exported commodities and their top trading partners.

## Prerequisites

- Python 3.x
- JSON file of the CIA World Factbook (`factbook.json`)

## Installation

1. Ensure you have Python 3.x installed on your system. Download it from [python.org](https://www.python.org/).
2. Obtain the JSON file of the CIA World Factbook and name it `factbook.json`.

## Usage

1. **Place the JSON file**: Ensure the `factbook.json` file is in the same directory as the script.

2. **Run the script**:
    ```bash
    python world-partners.py
    ```

3. **Enter the country name**: When prompted, enter the name of the country you wish to query (use lowercase letters).

4. **View the results**: The script will display the imported commodities, import trading partners, exported commodities, and export trading partners for the specified country.

## Script Details

### Imports

```python
import json
```

### Loading the Data

```python
with open('factbook.json', 'r') as blue:
    data = json.load(blue)
```

### User Input

```python
z = str(raw_input("ENTER COUNTRY: "))
```

### Display Imported Commodities

```python
print("Imported Commodities")
print("*" * 20)

for imported in data['countries'][z]['data']['economy']['imports']['commodities']['by_commodity']:
    print(imported)

print("*" * 20)
```

### Display Import Trading Partners

```python
print("""
The Import Trading Partners for %s are:
""" % (z.title()))

for i in range(4):
    print(data['countries'][z]['data']['economy']['imports']['partners']['by_country'][i]['name'])

print("-" * 10)
```

### Display Exported Commodities

```python
print("Exported Commodities")
print("*" * 20)

for exported in data['countries'][z]['data']['economy']['exports']['commodities']['by_commodity']:
    print(exported)

print("*" * 20)
```

### Display Export Trading Partners

```python
print("""
The Export Trading Partners for %s are:
""" % (z.title()))

for i in range(4):
    print(data['countries'][z]['data']['economy']['exports']['partners']['by_country'][i]['name'])
```

## Notes

- Ensure the country name entered matches the format in the JSON file (usually lowercase).
- The script prints the top 4 trading partners for both imports and exports. Modify the `range(4)` if more or fewer partners are needed.

## License

This project is licensed under the MIT License.

## Acknowledgements

Data is sourced from the CIA World Factbook.

---

