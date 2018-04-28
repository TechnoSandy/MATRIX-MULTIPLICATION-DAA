/**
 * 
 */
package com.daa.project;

/**
 * @author sandy
 *
 */
public class LargeNumberMultiplicationNaive {

	/**
	 * 
	 */

	public LargeNumberMultiplicationNaive() {
		// TODO Auto-generated constructor stub
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// Multiply two interger of long type

		double first =  Math.pow(2, 2);
		double second = Math.pow(2, 2);

		// long first = 9223372036854775807l;
		// long second =9223372036854775807l;

		System.out.println("First Number :" + first);
		System.out.println("Second Number :" + second);
		double sum = 0;
		double temp, Count = 0l;
		do {
			temp = second % 10;
			sum = (sum + (temp * Math.pow(10, Count) * first));
			second = second / 10;
			Count++;

			System.out.println("temp" + temp);
			System.out.println("Next Value " + temp * Math.pow(10, Count));
			System.out.println("sum" + sum);
			System.out.println("second" + second);

		} while (second > 0.0);

		System.out.printf("  %3.3E", sum);

	}

}
