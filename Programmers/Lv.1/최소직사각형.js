function solution(sizes) {
    const w = [];
    const h = [];
    sizes.map(([s0, s1]) => {
        if (s0 > s1){
            w.push(s0);
            h.push(s1);
        } else {
            h.push(s0);
            w.push(s1);
        }
    })
    return Math.max(...w) * Math.max(...h);
}