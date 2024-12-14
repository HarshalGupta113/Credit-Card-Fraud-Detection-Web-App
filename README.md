# Credit Card Fraud Detection Web App

This repository hosts a web application for detecting credit card fraud. Built using modern web technologies and machine learning, the app provides a seamless platform for analyzing transactions to identify potential fraud.

## Features

- **Machine Learning Integration**: Leverages a trained anomaly detection model to evaluate transaction data.
- **Interactive Dashboard**: Displays predictions and analytics in a user-friendly interface.
- **Batch Processing**: Supports multiple transaction evaluations at once.
- **Streamlit Framework**: Uses Streamlit for rapid deployment and an intuitive user experience.

## Requirements

To run this application, you need:

- Python 3.8 or later
- The following Python libraries:
  - pandas
  - numpy
  - scikit-learn
  - joblib
  - streamlit

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/HarshalGupta113/Credit-Card-Fraud-Detection-Web-App.git
   cd Credit-Card-Fraud-Detection-Web-App
   ```

2. Run the application:

   ```bash
   streamlit run app.py
   ```

3. Open your browser and navigate to the local server link provided by Streamlit.

## Usage

1. Upload a CSV file containing transaction data, or input transaction details manually.
2. Click "Analyze" to check for potential fraudulent transactions.
3. Review the results in the dashboard, which includes:
   - Fraud prediction for each transaction.
   - Key statistics and visualizations of the dataset.

## Contributing

Contributions are encouraged! Feel free to fork the repository, make changes, and submit a pull request. You can also open issues to suggest enhancements or report bugs.

## Acknowledgments

- Based on the [Credit Card Fraud Detection dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).
- Thanks to the open-source community for their tools and support.

