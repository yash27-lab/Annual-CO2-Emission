# CO2 Emissions Prediction System with AWS Integration

## Project Overview
A machine learning-based system for predicting annual CO2 emissions across different countries using historical data (1750-2022). The project combines advanced modeling techniques with AWS cloud architecture for scalable deployment.

## Key Features
- Accurate CO2 emission predictions (89% accuracy)
- Advanced feature engineering for temporal patterns
- Multiple model implementations (Linear Regression, Random Forest, XGBoost)
- AWS Lambda integration attempt with complete architecture design

## Technical Stack
- Python 3.x
- Libraries: pandas, scikit-learn, XGBoost, seaborn
- AWS Services: Lambda, API Gateway, CloudWatch
- Data Source: Global Carbon Project & International Energy Agency

## Model Performance
- XGBoost (Final Model): R² Score: 0.89
- Gradient Boosting: R² Score: 0.87
- Random Forest: R² Score: 0.85

## Project Structure

```bash
project/
├── lambda_function.py
├── inference.py
├── model.pkl
├── requirements.txt
└── layer_dependencies/ 
```
## Future Improvements
- AWS SageMaker migration
- Automated retraining pipeline
- Enhanced monitoring system
- Additional feature engineering

## Prerequisites
- Python 3.x
- AWS Account
- Required Python packages (see requirements.txt)

## Getting Started
1. Clone the repository
2. Install dependencies
3. Configure AWS credentials
4. Run model training
5. Deploy using provided Lambda configuration

## Contributors
- Yash Negi
