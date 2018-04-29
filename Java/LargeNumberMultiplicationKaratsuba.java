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
public class LargeNumberMultiplicationKaratsuba {

	/**
	 * 
	 */
	public static long first;
	public static long second;
	public static BigInteger firstNumber;
	public static BigInteger secondNumber;

	public LargeNumberMultiplicationKaratsuba() {

	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// Multiply two integer of long type
		// Maximum power of 2 is 32 for long Above that we need to use BigInteger to
		// Calculate
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
		if (first < (long) Math.pow(2, 32) && second < (long) Math.pow(2, 32) && first != 0 && second != 0) {

			System.out.println("You have entered 2^" + power_of_two);
			System.out.println("First Number :" + first);
			System.out.println("Second Number :" + second);
			System.out.println(karatsubaLong(first, second));
		}

		else {
			System.out.println("Order is very large we will calculate with BigInteger");
			System.out.println("You have entered 2^" + power_of_two);
			System.out.println("First Number :" + firstNumber);
			System.out.println("Second Number :" + secondNumber);

			System.out.println(karatsubaBigInteger(firstNumber, secondNumber));
		}
		Scan.close();

	}

	/**
	 * @param first
	 * @param second
	 * @return long
	 */
	// Reference for theory:https://www.youtube.com/watch?v=JCbZayFr9RE

	public static BigInteger karatsubaBigInteger(BigInteger first, BigInteger second) {

		int N = Math.max(first.bitLength(), second.bitLength());

		// If less than 9 we can directly multiply i.e we cannot further divide the
		// number in halves
		if (N <= 10) {

			return first.multiply(second);
		}
		// number of bits divided by 2, rounded up (Dividing the long value into two
		// halves)
		N = (N / 2) + (N % 2);

		// x = a + 2^N b, y = c + 2^N d
		// IMP NOTE : RtSHift = Divide and LtShift = Multiply
		// Reference: https://www.youtube.com/watch?v=JCbZayFr9RE&t=290s
		BigInteger B = first.shiftRight(N);
		BigInteger A = first.subtract(B.shiftLeft(N));
		BigInteger D = second.shiftRight(N);
		BigInteger C = second.subtract(D.shiftLeft(N));

		// compute sub-expressions
		BigInteger AC = karatsubaBigInteger(A, C);
		BigInteger BD = karatsubaBigInteger(B, D);
		BigInteger ABCD = karatsubaBigInteger(A.add(B), C.add(D));

		return AC.add(ABCD.subtract(AC).subtract(BD).shiftLeft(N)).add(BD.shiftLeft(2 * N));

	}

	public static long karatsubaLong(long first, long second) {

		// If less than 9 we can directly multiply
		if (first < 10 || second < 10) {
			return LargeNumberMultiplicationNaive.multiplyNaive(first, second);
		}
		double lengthOfNumber = Long.toString((Math.max(first, second))).length();
		// Check if the number is even length
		if (lengthOfNumber % 2 == 1)
			lengthOfNumber++;
		long A = (long) (first / Math.pow(10, (lengthOfNumber / 2)));

		long B = (long) (first % Math.pow(10, (lengthOfNumber / 2)));

		long C = (long) (second / Math.pow(10, (lengthOfNumber / 2)));

		long D = (long) (second % Math.pow(10, (lengthOfNumber / 2)));

		long AC = karatsubaLong(A, C);
		long BD = karatsubaLong(B, D);
		long ABCD = karatsubaLong(A + B, C + D);

		return ((long) ((AC * Math.pow(10, lengthOfNumber)) + ((ABCD - AC - BD) * Math.pow(10, (lengthOfNumber / 2)))
				+ BD));
	}

}
