import java.util.Arrays;

public class BubbleSort {
	
	//not optimized
	public static void bubbleSort(int [] unsorted_array) {
		int length_of_unsorted_array = unsorted_array.length;
		boolean swapped = true;
		
		while(swapped == true) {
			swapped = false;
			for(int i=1; i<length_of_unsorted_array; i++) {
				if(unsorted_array[i-1] > unsorted_array[i]) {
					swap(unsorted_array ,i-1, i);
					swapped = true;
					//System.out.println("after swap : "+Arrays.toString(unsorted_array));
				}	
			}
			//System.out.println(Arrays.toString(unsorted_array));
		}
	}
	
	//attempt 2 optimized. 
	public static void optimizedBubbleSort(int [] unsorted_array) {
		int length_of_unsorted_array = unsorted_array.length;
		boolean swapped = true;
		
		while(swapped == true) {
			swapped = false;
			for(int i=1; i<length_of_unsorted_array; i++) {
				if(unsorted_array[i-1] > unsorted_array[i]) {
					swap(unsorted_array ,i-1, i);
					swapped = true;
					//System.out.println("after swap : "+Arrays.toString(unsorted_array));
				}
			}
			length_of_unsorted_array--;
			//System.out.println(Arrays.toString(unsorted_array));
		}
	}

	//attempt 3 optimized. 
	public static void optimizedBubbleSort2(int [] unsorted_array) {
		int length_of_unsorted_array = unsorted_array.length;
		int swap_at=0;
		while(length_of_unsorted_array > 1) {
			swap_at = 0;
			for(int i=1; i<length_of_unsorted_array; i++) {
				if(unsorted_array[i-1] > unsorted_array[i]) {
					swap(unsorted_array ,i-1, i);
					swap_at = i;
				}
			}
			length_of_unsorted_array= swap_at;
		}
	}
	
	
	public static void swap( int [] unsorted_array,int big_value, int small_value) {
		int place_holder = unsorted_array[big_value];
		unsorted_array[big_value] = unsorted_array[small_value];
		unsorted_array[small_value] = place_holder;	
		//System.out.println("Swapped : "+array[big_value]+" with "+array[small_value]);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] actual = { 5, 1, 6, 2, 3, 4, 33, 45, 4, 123, 1, 1,4,1};
		
		System.out.println(Arrays.toString(actual));
		
		optimizedBubbleSort2(actual);
		
		System.out.println(Arrays.toString(actual));
	}

}
