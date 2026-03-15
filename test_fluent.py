import sklearn
from sklearn.linear_model import Ridge
model = Ridge()
params = model.get_params()
print(params['solver']) # Output: 0.5


thing = sklearn.metrics.check_scoring(Ridge())
print(thing , type(thing))