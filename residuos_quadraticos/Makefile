FC = gfortran
FCFLAGS = -g -ffpe-trap=zero,invalid,overflow,underflow
LDFLAGS = -llapack -lblas

.PHONY: all clean

all: init rq gera

init:
	@mkdir -p build
	@cp plot.py build/
	@echo "Diretório build criado e arquivo copiado"

rq:
	@echo "Compilando residuos_quadraticos..."
	@$(FC) $(FCFLAGS) $(LDFLAGS) -o build/rq src/residuos_quadraticos.f90

gera:
	@echo "Compilando gera_input..."
	@$(FC) $(FCFLAGS) -o build/gera src/gera_input.f90

clean:
	@echo "Removendo arquivos gerados..."
	@$(RM) -r build


