# This file provides documentation related to the data directory, including information on expected data formats and examples.

## Data Directory Overview

The `data` directory is intended to store datasets that will be used by the application. It is crucial to ensure that the datasets conform to the expected formats for seamless processing and analysis.

## Expected Data Formats

1. **CSV Files**: 
   - Must have a header row with column names.
   - Each subsequent row should represent a record.
   - Example: `data/sample_data.csv`

2. **JSON Files**: 
   - Should be in a valid JSON format.
   - Can be either an array of objects or a single object.
   - Example: `data/sample_data.json`

3. **Excel Files**: 
   - Supported formats include `.xls` and `.xlsx`.
   - Must contain at least one sheet with data.
   - Example: `data/sample_data.xlsx`

## Examples

- **CSV Example**:
  ```
  name,age,city
  Alice,30,New York
  Bob,25,Los Angeles
  ```

- **JSON Example**:
  ```
  [
      {"name": "Alice", "age": 30, "city": "New York"},
      {"name": "Bob", "age": 25, "city": "Los Angeles"}
  ]
  ```

- **Excel Example**:
  - A spreadsheet with columns: `name`, `age`, `city`.

## Notes

- Ensure that the data files are placed in this directory before running the application.
- The application will automatically detect and process these files based on their formats.