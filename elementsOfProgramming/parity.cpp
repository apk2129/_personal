template <Template T>
void dutch_flag_partition(vector<T> &A, const int &pivot_index)
{
    T pivot = A[pivot_index]

    int smaller = 0, equal = 0, larger= A.size()-1;

    // [ 33 4 *5* 2 55 10]
    //  ^ ^           ^
    // small/equal    larger


    while( equal <= larger){

        if (A[equal] < pivot){

        }
        else if (A[equal] == pilot){
            ++equal;
        }
        else{
            // A[pivot] > pivot
            // swap(A[equal],A[larger--]);/
        }
    }

}
