from neural import Neural

nn = Neural(path_dataset='water_potability.csv')
nn.training()

z_0 = nn.inference([[10.22, 248.07, 28.74, 7.51, 3.93, 2.83, 13.78, 84.60, 2.67]])
z_1 = nn.inference([[6.28, 258.30, 13.77, 7.48, 3.28, 5.63, 16.46, 73.51, 4.10]])

print('Предсказание для не питьевой: ', z_0)
print('Предсказание для питьевой: ', z_1)
