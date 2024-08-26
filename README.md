# NSE Bhavcopy Data Fetcher and Analyzer

This Python script fetches and analyzes the NSE (National Stock Exchange of India) Bhavcopy data for a given date. It downloads the data, extracts the relevant information, cleans it, and then performs basic analysis to determine key metrics such as the security with the maximum traded value, maximum traded quantity, and the maximum percentage change from open to close price.

## Features

- **Automated Data Fetching**: The script automatically downloads the NSE Bhavcopy data for a specified date.
- **Data Extraction**: The downloaded ZIP file is extracted, and the relevant CSV file is loaded into a pandas DataFrame.
- **Data Cleaning**: Unnecessary columns are dropped from the DataFrame to focus on essential metrics.
- **Analysis**: The script performs the following analyses:
  - Identifies the security with the maximum traded value.
  - Identifies the security with the maximum traded quantity.
  - Calculates and identifies the security with the maximum percentage change between open and close prices.

## Requirements

- Python 3.x
- Required Python libraries:
  - pandas
  - numpy
  - requests
  - zipfile

You can install the required Python libraries using pip:

```bash
pip install pandas numpy requests
```

## Usage

1. **Clone the Repository**: First, clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/nse-bhavcopy-analyzer.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd nse-bhavcopy-analyzer
   ```

3. **Run the Script**:

   Execute the script by running the following command in your terminal or command prompt:

   ```bash
   python nse_bhavcopy_analyzer.py
   ```

   The script will prompt you to enter a date in the format `DDMMM`. For example, if you want to fetch data for 5th March, you would enter `05MAR`.

4. **View the Results**:

   After the script completes its execution, it will display the following outputs in your console:
   - The full Bhavcopy DataFrame for the given date.
   - The security with the maximum traded value.
   - The security with the maximum traded quantity.
   - The security with the maximum percentage change between open and close prices.

## Example

Here’s an example of how to run the script:

```bash
Give Date 
05MAR
```

The script will download the Bhavcopy for 5th March 2021, extract the data, and then display the analysis results.

## Important Notes

- **File Path**: The script assumes that the extracted file will be located in `C:\Users\Parishrut\Desktop\`. Modify this path if your working directory is different.
- **Date Format**: Ensure that you enter the date in the `DDMMM` format (e.g., `05MAR` for 5th March).
- **Data Availability**: The script fetches data from the year 2021. Ensure that the date you enter corresponds to a date when the market was open.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

## Contact

For any questions or suggestions, please contact 

---

Replace placeholders like `your-username`, `nse_bhavcopy_analyzer.py`, and `Your Name` with the appropriate information. This README should provide clear instructions on how to use the script and contribute to the project.
