from scipy import special

#gama functions and relational functions

x = [1, 5, 10]
print("gamma(x): ", special.gamma(x))
print("ln|gamma(x)|: ", special.gammaln(x))
print("beta(x): ", special.beta(x, 2))