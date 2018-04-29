/**
 * 
 */
package com.daa.project;

import java.math.BigInteger;
import java.util.Scanner;

/**
 * @author sandy
 *
 */
public class LargeNumberMultiplicationNaive {

	/**
	 * 
	 */
	public static long first;
	public static long second;
	public static BigInteger firstNumber;
	public static BigInteger secondNumber;

	public LargeNumberMultiplicationNaive() {
		// TODO Auto-generated constructor stub
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// Multiply two integer of long type
		// Maximum power of 2 is 32 for long Above that we need to use BigInteger to
		// calculate multiplication
		Scanner Scan = new Scanner(System.in);
		System.out.println("Enter the digit in decimal");
		int power_of_two = Scan.nextInt();
		if (power_of_two < 32) {
			first = (long) Math.pow(2, power_of_two);
			second = (long) Math.pow(2, power_of_two);
		} else {
			BigInteger base;
			int exponent = power_of_two;
			base = new BigInteger("2");
			firstNumber = base.pow(exponent);
			secondNumber = base.pow(exponent);

		}

		// long first = 9223372036854775807l;
		// long second =9223372036854775807l;

		if (first < (long) Math.pow(2, 32) && second < (long) Math.pow(2, 32) && first != 0 && second != 0) {
			System.out.println("You have entered 2^" + power_of_two);
			System.out.println("First Number :" + first);
			System.out.println("Second Number :" + second);
			System.out.println("Multiplication : "+multiplyNaive(first, second));
		}

		else {
			System.out.println("Order is very large we will calculate with BigInteger");
			System.out.println("You have entered 2^" + power_of_two);
			System.out.println("First Number :"+firstNumber);
			System.out.println("Second Number :"+secondNumber);
			System.out.println("Multiplication :"+firstNumber.multiply(secondNumber));
		}
		Scan.close();

	}

	/**
	 * @param first
	 * @param second
	 * @return
	 */
	public static long multiplyNaive(long first, long second) {
		long product = 0;
		long temp, Count = 0;
		do {
			temp = second % 10;
			product = (long) (product + (temp * Math.pow(10, Count) * first));
			second = second / 10;
			Count++;
		} while (second > 0);
		return product;
	}

}
