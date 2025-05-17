FC = gfortran
FCFLAGS = -g -ffpe-trap=zero,invalid,overflow,underflow
LDFLAGS = -llapack -lblas

.PHONY: all clean

all: rq gera

rq:
	$(FC) $(FCFLAGS) $(LDFLAGS) -o rq src/residuos_quadraticos.f90

gera:
	$(FC) $(FCFLAGS) -o gera src/gera_input.f90

clean:
	$(RM) rq gera out/**.*

