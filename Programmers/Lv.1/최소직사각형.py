def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])
    return max(w) * max(h)

# javascript
# function solution(sizes) {
#     const w = [];
#     const h = [];
#     sizes.map(([s0, s1]) => {
#         if (s0 > s1){
#             w.push(s0);
#             h.push(s1);
#         } else {
#             h.push(s0);
#             w.push(s1);
#         }
#     })
#     return Math.max(...w) * Math.max(...h);
# }