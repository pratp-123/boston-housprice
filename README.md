### boston-house price prediction

### Tools required

1. [render](https://render.com)
2. [Github Account](https://github.com)
3. [VSCodeIDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)


### Setup steps  
```bash
git clone https://github.com/pratp-123/boston-housprice.git
cd boston-housprice
python3 -m venv venv         # or use conda
source venv/bin/activate     # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## libraries and tools
![Project Architecture](images/libraries.png)

## spread and skewness of each numerical feature
- Several predictors require scaling or transformation due to skewness.

- The normal distribution of RM and the negative correlation of LSTAT and CRIM with price confirm the linear and socioeconomic relationships in the dataset.

- Understanding these patterns guided effective feature engineering and model tuning in this project.
![spread and skewness of each numerical feature](images/skewness.png)
You’ll see whether features like RM (rooms per dwelling) or LSTAT (lower status population %) are normally distributed or skewed.


## Relationship Between Key Features and Target

- 🔹  Feature vs Price Relationships (Multi-Plot Visualization)
🏠 (a) RM vs Price (Average Number of Rooms)

A clear positive correlation — as the number of rooms (RM) increases, the house price also increases.

Indicates that larger homes tend to have higher market values.

- 💰 (b) LSTAT vs Price (Lower-Status Population Percentage)
Shows a strong negative correlation — as LSTAT increases, house price decreases.
Suggests that wealthier neighborhoods (low LSTAT) have higher-priced homes.

- 📏 (c) PTRATIO vs Price (Pupil-Teacher Ratio)
Weak to moderate negative relationship — higher student-to-teacher ratios slightly lower home prices.
Implies that better educational quality (lower PTRATIO) can positively impact property value.

- 🚗 (d) DIS vs Price (Distance to Employment Centers)
Weak correlation — houses closer to employment centers (lower DIS) often have slightly higher prices, but effect varies.
Suggests other features may dominate price determination.

- 🚨 (e) CRIM vs Price (Per Capita Crime Rate)
Strong negative correlation — areas with higher crime rates (CRIM) tend to have lower home prices.
Confirms that safety is a key determinant of housing value.
![Relationship Between Key Features and Target](images/price%20vs%20feature.png)




### scatter of predicted and actual data points
📊 Insights from Visualizations
🔹 1️⃣ Actual vs Predicted Prices (Scatter Plot)

- The scatter plot shows Actual (x-axis) vs Predicted (y-axis) house prices.

- Most points lie close to the diagonal line, indicating that predictions are generally accurate.

 A few deviations suggest minor underfitting/overfitting, but overall, the model captures the relationship well.

- This confirms the model’s strong predictive performance, likely reflected in a high R² score.

- The consistent trend along the diagonal shows that the Random Forest Regressor effectively learned the mapping between features and price.

  
![scatter of predicted and actual data points](images/predected_scatter.png)

### Directory
```
Directory structure:
└── pratp-123-boston-housprice/
    ├── README.md
    ├── app.py
    ├── Dockerfile
    ├── LICENSE
    ├── Procfile
    ├── requirements.txt
    ├── scaling.pkl
    ├── templates/
    │   └── index.html
    └── .github/
        └── workflows/
            └── main.yaml
```

### 🎓 Key Learnings

- Gained hands-on experience with the end-to-end Machine Learning workflow — starting from Exploratory Data Analysis (EDA) using pandas, matplotlib, and seaborn to understand dataset patterns, and analyze feature correlations.

- Learned effective data preprocessing techniques including handling missing values, outlier treatment, and feature scaling using StandardScaler to prepare clean, normalized data for modeling.

- Applied feature engineering by selecting important variables through correlation and feature importance analysis, and creating derived or polynomial features to capture complex relationships.

- Implemented multiple regression algorithms such as Linear Regression, Decision Tree, Random Forest, and Gradient Boosting using scikit-learn, and improved their performance with k-fold cross-validation to ensure model generalization.

- Performed hyperparameter tuning using GridSearchCV and RandomizedSearchCV to optimize model parameters and select the best-performing regressor.

- Evaluated models using key metrics like R² Score, MAE, MSE, and RMSE, and visualized results through residual plots, predicted vs actual graphs, and feature importance charts for deeper interpretation.

- Automated the entire process using GitHub Actions (CI/CD), enabling automatic testing, building, and deployment of the model through Dockerized pipelines.

- Successfully deployed the Flask-based application on Render.com, integrating the Render API and Service ID for seamless continuous deployment.

- Strengthened understanding of model lifecycle management, version control using Git & GitHub, and real-world deployment of ML models for production use.



