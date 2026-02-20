# train_churn_model.py
from utils import load_data_from_sql, feature_engineering
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.combine import SMOTETomek
from xgboost import XGBClassifier
import joblib

#Define feature lists
numeric_features = [
    'customer_calls',
    'total_mins',
    'total_charge',
    'account_length'
]

categorical_features = [
    'state',
    'intl_plan',
    'service_call_bin',
    'pay_as_you_go_intl'
]


#Build preprocessing + model pipeline
numeric_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', numeric_pipeline, numeric_features),
    ('cat', categorical_pipeline, categorical_features)
])

model_pipeline = ImbPipeline([
    ('preprocessor', preprocessor),
    ('smote', SMOTETomek(random_state=42)),
    ('model', XGBClassifier(
        eval_metric='logloss',
        random_state=42
    ))
])

param_grid = {
    'model__n_estimators': [200, 300],
    'model__max_depth': [6, 7, 8],
    'model__learning_rate': [0.05, 0.1],
    'model__subsample': [0.7, 1.0],
    'model__colsample_bytree': [0.7, 1.0],
    'model__gamma': [0, 0.1, 0.2]
}

search = RandomizedSearchCV(
    estimator=model_pipeline,
    param_distributions=param_grid,
    n_iter=20,
    scoring='f1',
    cv=5,
    n_jobs=-1,
    random_state=42,
    verbose=1
)

# Load data
df = load_data_from_sql()
df = feature_engineering(df)

df['churn'] = df['churn'].astype(int)

# Target
y = df['churn']
X = df.drop(columns=['churn'])

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Train pipeline (already built in Step 3 earlier)
search.fit(X_train, y_train)

best_model = search.best_estimator_

# Save trained pipeline
joblib.dump(search.best_estimator_, "churn_pipeline.pkl")

