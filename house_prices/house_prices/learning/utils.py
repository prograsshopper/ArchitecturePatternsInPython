from sklearn import linear_model, tree, ensemble


ml_method_dict = {
    'linear_regression': linear_model.LinearRegression,
    'decision_tree': tree.DecisionTreeRegressor,
    'random_forest': ensemble.RandomForestRegressor,
    'gradient_boost': ensemble.GradientBoostingRegressor
}