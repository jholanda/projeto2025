#/bin/bash
gera

for grau in {2..10}; do
    ./rq input.txt $grau && python ajuste_polinomial.py input.txt input.txt_grau$grau.txt;
done

