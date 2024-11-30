import java.util.Arrays;

public class SelectionSort {

	public static void selectionSort(int [] unsorted_array) {
		int minimum_index;
		for (int i=0; i<unsorted_array.length; i++) {
			minimum_index = getMinimumIndex(unsorted_array, i);
			if(minimum_index != i) {
				swap(unsorted_array, i, minimum_index);
			}
		}
	}
	
	public static int getMinimumIndex(int [] unsorted_array, int start_index) {
		int minimum = unsorted_array[start_index];
		int minimum_index = start_index;
		for(int i=start_index; i<unsorted_array.length; i++) {
			if(minimum > unsorted_array[i]) {
				minimum = unsorted_array[i];
				minimum_index = i;
			}
		}
		return minimum_index;
	}
	
	
	public static void swap( int [] unsorted_array,int big_value, int small_value) {
		int place_holder = unsorted_array[big_value];
		unsorted_array[big_value] = unsorted_array[small_value];
		unsorted_array[small_value] = place_holder;	
	}

	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] actual = { 5,2,33, 1, 6, 2, 3, 4, 33, 45, 4, 123, 1, 1,1 };
		
		System.out.println(Arrays.toString(actual));
		selectionSort(actual);
		System.out.println(Arrays.toString(actual));
		
		//System.out.println(getMinimumIndex(actual,0));
	}

}
