DELTA_T = 0.1

time_steps = [x * DELTA_T for x in range(1, 501)]
w_lst = [x/2 for x in time_steps]

print(time_steps)
print(w_lst)