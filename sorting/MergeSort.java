import java.util.Arrays;

public class MergeSort {


	
	public static void mergeSort(int [] array, int length_of_array) {
		// if length of array < 2. return;
		if(length_of_array<2) {
			return;
		}
		
		// divide array in two equal parts: left_array, right_array, using and int mid (midpoint)
		int mid_point = length_of_array/2;
		int left_array[] = new int[mid_point];
		int right_array[] = new int[length_of_array - mid_point];
		
		//fill left array
		for (int i=0; i<mid_point; i++) {
			left_array[i] = array[i]; 
		}
		
		
		//fill right array
		for(int i=mid_point; i<length_of_array; i++) {
			right_array[i-mid_point] = array[i];
		}
		
		//call mergeSort on both left_array and right_array
		mergeSort(left_array, mid_point);
		mergeSort(right_array, length_of_array-mid_point);
		// call merge method
		
		//merge();		
		merge(array, left_array, right_array, mid_point, length_of_array-mid_point);
	}
	
	public static void merge(int [] array, int [] left_array, int [] right_array, int left_array_length, int right_array_length) {
		int pivot_left_array = 0;
		int pivot_right_array =0;
		int pivot_array=0;
		
		//check if both left and right have length left to compre first.
		while( (pivot_left_array<left_array_length) && (pivot_right_array<right_array_length) ) {
			
			//while left is small put left in array. otherwise put right.
			if(left_array[pivot_left_array] <= right_array[pivot_right_array] ) {
				array[pivot_array++]=left_array[pivot_left_array++];
			}
			else {
				array[pivot_array++]=right_array[pivot_right_array++];
			}
		}
		
		//check if left array has any elements left. put them in array
		while(pivot_left_array<left_array_length) {
			array[pivot_array++]=left_array[pivot_left_array++];
		}
		
		//check if right array has any elements left. put them in array.
		while(pivot_right_array<right_array_length) {
			array[pivot_array++]=right_array[pivot_right_array++];
		}
		//System.out.println("This is working"+ Arrays.toString(array));
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] actual = { 5, 1, 6, 2, 3, 4, 33, 45, 4, 123};
		
		System.out.println(Arrays.toString(actual));
		
		mergeSort(actual, actual.length);
		
		System.out.println(Arrays.toString(actual));
		
	}
}
