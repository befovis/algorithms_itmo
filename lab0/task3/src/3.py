import time, tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
f = open("../../task1/txtf/input.txt")
n = int(f.readline())
f.close()
mas = [0,1]
for i in range(2, n+1):
    mas.append((mas[-1] + mas[-2]) % 10)
f = open('../../task1/txtf/output.txt', 'w')
f.write(str(mas[n]))
f.close()
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
tracemalloc.stop()