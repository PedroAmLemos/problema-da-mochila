import signal
import random
from sys import setrecursionlimit
from contextlib import contextmanager


class TimeoutException(Exception):
    pass


@contextmanager
def time_limit(seconds):
    def signal_handler(*_):
        raise TimeoutException("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


def knapSack(capacidade, pesos, variaveis, n):
    global result
    if n == 0 or capacidade == 0:
        return 0
    if (pesos[n-1] > capacidade):
        return knapSack(capacidade, pesos, variaveis, n-1)
    else:
        result = max(variaveis[n-1] + knapSack(capacidade-pesos[n-1], pesos,
                     variaveis, n-1), knapSack(capacidade, pesos, variaveis,
                     n-1))
        return result


def knapsack2(wt, val, W, n):
    # base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    # choice diagram code
    if wt[n-1] <= W:
        t[n][W] = max(
            val[n-1] + knapsack2(
                wt, val, W-wt[n-1], n-1),
            knapsack2(wt, val, W, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapsack2(wt, val, W, n-1)
        return t[n][W]


global result
result = 0
setrecursionlimit(1000)
variaveis = []
pesos = []
n = 0
while n < 200:
    variavel = random.randint(10, 10000)
    if variavel not in variaveis:
        variaveis.append(variavel)
        n += 1
n = 0
while n < 200:
    variavel = random.randint(10, 10000)
    if variavel not in variaveis and variavel not in pesos:
        pesos.append(variavel)
        n += 1
somaPesos = sum(pesos)
capacidade = somaPesos if somaPesos > max(pesos) else somaPesos + max(pesos)
n = len(variaveis)
t = [[-1 for i in range(capacidade + 1)] for j in range(n + 1)]
try:
    with time_limit(300):
        knapSack(capacidade, pesos, variaveis, n)
except TimeoutException as _:
    print("Timed out!")
print(f'result:\t\t{result}')
print(f'n:\t\t{n}')
print(f'capacidade:\t{capacidade}')
try:
    with time_limit(300):
        result = knapsack2(pesos, variaveis, capacidade, n)
except TimeoutException as _:
    print("Timed out!")
print(f'result:\t\t{result}')
print(f'n:\t\t{n}')
print(f'capacidade:\t{capacidade}')
