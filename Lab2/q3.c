#include <stdio.h>
#include <stdlib.h>
#include <time.h> 
#include <mpi.h>
#define NP 10000000

int main(int argc, char *argv[]) {
	int vect1[NP];
	unsigned long int i, n=(unsigned long int)NP;
	double start, end;
	unsigned long int totsum,locsum =0;
	int rank,size;
	MPI_Init(&argc,&argv);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	for (i=rank; i<n; i+=size) { vect1[i] = i+1; }
	
	start = MPI_Wtime();
	for (i=rank; i<n; i+=size) { locsum += (unsigned long)vect1[i]; }
	MPI_Reduce(&locsum,&totsum,1,MPI_DOUBLE,MPI_SUM,0,MPI_COMM_WORLD);
	MPI_Barrier(MPI_COMM_WORLD);
	end = MPI_Wtime();
	
	printf("Local Sum on P#%d is %d.\n",rank,locsum);
	if (rank==0){
		double t = (end-start);
		printf("the total sum is %d.\n",totsum);
		printf("Time Elapsed is %f secs.\n",t);
	}
	MPI_Finalize();
	return 0;
}
