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


def sort(variaveis, pesos):
    a = (zip(variaveis, pesos))
    a = sorted(a, reverse=True, key=lambda item: (item[0]/item[1]))
    variaveis = [x for x, _ in a]
    pesos = [y for _, y in a]
    return variaveis, pesos


def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]


global result
result = 0
setrecursionlimit(10000)
variaveis = []
pesos = []
n = 0
while n < 1000:
    variavel = random.randint(1, 3000)
    variaveis.append(variavel)
    n += 1
n = 0
while n < 1000:
    variavel = random.randint(1, 3000)
    pesos.append(variavel)
    n += 1
somaPesos = int(sum(pesos)/2)
if somaPesos > max(pesos):
    capacidade = somaPesos
else:
    capacidade = somaPesos + max(pesos)
n = len(variaveis)
a = zip(variaveis, pesos)
variaveis, pesos = sort(variaveis, pesos)
try:
    with time_limit(5):
        brute_force(capacidade, pesos, variaveis, n)
except TimeoutException as _:
    print("Timed out!")
print(f'result:\t\t{result}')
print(f'n:\t\t{n}')
print(f'capacidade:\t{capacidade}')
print(knapSack(capacidade, pesos, variaveis, n))
