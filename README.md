# Flying CO2 Emittion Calculator

## Purpose
The `aviationCO2` project calculates the fuel consumption and CO2 emissions per passenger for different aircraft types based on the flying time. This tool helps to understand the environmental impact of air travel.

## Requirements
- Python 3.8 or higher

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/aviationCO2.git
    cd aviationCO2
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the script:
    ```sh
    python aviationCO2.py
    ```

2. Enter the flying time in hours when prompted. The script will calculate and display the fuel consumption and CO2 emissions per passenger for the following aircraft types:
    - B737-800
    - A320-200
    - B787-9
    - B777-300ER

3. The output will be displayed in a table format showing the fuel burned and CO2 emissions per passenger for each aircraft type.

## Example
```sh
Enter the time flying in hours: 5
Table: Fuel Burned and CO2 Emissions per Passenger for Different Aircrafts
----------------------------------------------------------------------
   Aircraft  |  Fuel (kg/passenger)  |  CO2 (kg/passenger)
----------------------------------------------------------------------
  B737-800   |  68.8                 |  217.4
  A320-200   |  67.5                 |  213.3
  B787-9     |  94.6                 |  298.9
  B777-300ER |  101.9                |  321.9
----------------------------------------------------------------------
