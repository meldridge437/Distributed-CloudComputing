#include <stdio.h>
#include <time.h> 
#include <mpi.h>

int main(int argc, char *argv[]) {
	int rank,size;
	MPI_Init(&argc,&argv);
	
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	
	double start = MPI_Wtime();
	printf("Hello, Matthew from #%d\n!",rank);
	double end = MPI_Wtime();
	MPI_Finalize();
	return 0;
}
