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
	 * 
	 *         x=5678 y=1234
	 * 
	 *         a=56,b=78
	 * 
	 *         c=12,d=34
	 * 
	 *         step 0 = m = n/2 + n%2
	 * 
	 *         step 1 = a*c
	 * 
	 *         step 2 = b*d
	 * 
	 *         step 3 = (a + b)*(c + d)
	 * 
	 *         step 4 = 3) - 2) - 1)
	 * 
	 *         step 5 = 1)*Math.pow(10, m*2) + 2) + 4)*Math.pow(10, m)
	 * 
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
		BigInteger b = first.shiftRight(N);
		BigInteger a = first.subtract(b.shiftLeft(N));
		BigInteger d = second.shiftRight(N);
		BigInteger c = second.subtract(d.shiftLeft(N));

		// compute sub-expressions
		BigInteger ac = karatsubaBigInteger(a, c);
		BigInteger bd = karatsubaBigInteger(b, d);
		BigInteger abcd = karatsubaBigInteger(a.add(b), c.add(d));

		return ac.add(abcd.subtract(ac).subtract(bd).shiftLeft(N)).add(bd.shiftLeft(2 * N));

	}

	public static long karatsubaLong(long first, long second) {

		// If less than 9 we can directly multiply
		if (first < 10 || second < 10)
			return first * second;
		double max_length = Long.toString((Math.max(first, second))).length();
		if (max_length % 2 == 1)
			max_length++;
		long a = (long) (first / Math.pow(10, (max_length / 2)));

		long b = (long) (first % Math.pow(10, (max_length / 2)));

		long c = (long) (second / Math.pow(10, (max_length / 2)));

		long d = (long) (second % Math.pow(10, (max_length / 2)));

		long first_half = karatsubaLong(a, c);
		long middle_half = karatsubaLong(b, d);
		long last_half = karatsubaLong(a + b, c + d);

		return ((long) ((first_half * Math.pow(10, max_length))
				+ ((last_half - first_half - middle_half) * Math.pow(10, (max_length / 2))) + middle_half));
	}

}
