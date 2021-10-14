# # give me exactly two numbers from "ll" which sum gives the target
#
# ll = [1, 2, 3, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5]
# target = 9
#
# ss = set(ll)
# print(ss)
#
# counter = 0
# for i in ss:
#     for j in ss:
#         counter += 1
#         if i == j:
#             continue
#         if i + j == 9:
#             print(f"{i} + {j}")
#
# print(counter)
