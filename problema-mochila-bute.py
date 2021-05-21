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


def knapSack(W, wt, val):
    n = len(val)
    t = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif wt[i-1] <= j:
                t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]],  t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][W]


def brute_force(capacidade, pesos, variaveis, n):
    global result
    if n == 0 or capacidade == 0:
        return 0
    if (pesos[n-1] > capacidade):
        return brute_force(capacidade, pesos, variaveis, n-1)
    else:
        result = max(variaveis[n-1] + brute_force(capacidade-pesos[n-1], pesos,
                     variaveis, n-1), brute_force(capacidade, pesos, variaveis,
                     n-1))
        return result


def limitantes(wt, val, W, n):
    # base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    # choice diagram code
    if wt[n-1] <= W:
        t[n][W] = max(
            val[n-1] + limitantes(
                wt, val, W-wt[n-1], n-1),
            limitantes(wt, val, W, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = limitantes(wt, val, W, n-1)
        return t[n][W]


global result
result = 0
setrecursionlimit(1000)
variaveis = []
pesos = []
n = 0
while n < 1000:
    variavel = random.randint(1, 1000)
    variaveis.append(variavel)
    n += 1
n = 0
while n < 1000:
    variavel = random.randint(1, 3000)
    if variavel not in variaveis and variavel not in pesos:
        pesos.append(variavel)
        n += 1
somaPesos = sum(pesos)
capacidade = int(somaPesos/2) if somaPesos > max(pesos) else int(somaPesos/2) + max(pesos)
n = len(variaveis)
t = [[-1 for i in range(capacidade + 1)] for j in range(n + 1)]
try:
    with time_limit(7200):
        brute_force(capacidade, pesos, variaveis, n)
except TimeoutException as _:
    print("Timed out!")
print(f'result:\t\t{result}')
print(f'n:\t\t{n}')
print(f'capacidade:\t{capacidade}')
try:
    with time_limit(7200):
        result = knapSack(capacidade, pesos, variaveis)
except TimeoutException as _:
    print("Timed out!")
print(f'result:\t\t{result}')
print(f'n:\t\t{n}')
print(f'capacidade:\t{capacidade}')
