# Structural Engineering Calculations

## Overview
This Python script performs structural engineering calculations related to bolt connections, shear capacity, tension, and moment calculations. The script takes user inputs for various parameters and computes values based on engineering principles.

## Features
- Calculates shear and tensile capacity of bolts.
- Computes moment calculations.
- Reads data from an Excel file for further computations.
- User-friendly console-based interaction.

## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- `pandas` for handling Excel files
- `numpy` for numerical calculations

## Installation
1. Install Python 3 if not already installed.
2. Install the required dependencies using pip:
   ```sh
   pip install pandas numpy openpyxl
   ```
3. Ensure that the Excel file (`MC.xlsx`) is located at the correct path and contains the necessary data.

## Usage
1. Run the script using the terminal or command prompt:
   ```sh
   python script.py
   ```
2. Follow the on-screen prompts to enter required parameters.
3. The script will calculate and display the required structural values.

## Known Issues
- Ensure correct input format (numbers where expected).
- The file path for the Excel file may need to be updated to match your directory.

## Future Improvements
- Add GUI for better user experience.
- Implement error handling for invalid inputs.
- Automate data fetching from external sources.

## License
This project is open-source and available for modification 

