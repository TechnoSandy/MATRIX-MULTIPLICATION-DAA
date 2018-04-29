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
// NOT WORKING
public class LargeNumberMultiplicationGauss {

	/**
	 * 
	 */

	public static BigInteger firstNumber;
	public static BigInteger secondNumber;

	public LargeNumberMultiplicationGauss() {
		// TODO Auto-generated constructor stub
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner Scan = new Scanner(System.in);
		System.out.println("Enter the digit in decimal");

		int power_of_two = Scan.nextInt();

		BigInteger base;
		int exponent = power_of_two;
		base = new BigInteger("2");
		firstNumber = base.pow(exponent);
		secondNumber = base.pow(exponent);

		System.out.println("You have entered 2^" + power_of_two);
		System.out.println("First Number :" + firstNumber);
		System.out.println("Second Number :" + secondNumber);
		System.out.println(GaussMultiplication(firstNumber, secondNumber));

		Scan.close();

	}

	public static BigInteger GaussMultiplication(BigInteger firstNumber, BigInteger secondNumber) {

		int N = Math.max(firstNumber.bitLength(), secondNumber.bitLength());

		// If less than 9 we can directly multiply i.e we cannot further divide the
		// number in halves
		if (N <= 10) {

			return firstNumber.multiply(secondNumber);
		}
		// number of bits divided by 2, rounded up (Dividing the long value into two
		// halves)
		N = (N / 2) + (N % 2);

		// x = a + 2^N b, y = c + 2^N d
		// IMP NOTE : RtSHift = Divide and LtShift = Multiply
		// Reference: https://www.youtube.com/watch?v=JCbZayFr9RE&t=290s
		BigInteger B = firstNumber.shiftRight(N);
		BigInteger A = firstNumber.subtract(B.shiftLeft(N));
		BigInteger D = secondNumber.shiftRight(N);
		BigInteger C = secondNumber.subtract(D.shiftLeft(N));

		// compute sub-expressions
		BigInteger	AC = GaussMultiplication(A,C);
		BigInteger	AD = GaussMultiplication(A,D);
		BigInteger	BC = GaussMultiplication(B,C);
		BigInteger	BD = GaussMultiplication(B,D);
		
		return (AC.multiply((new BigInteger("10").pow(2*N))) ).add(AD.add(BC)).multiply(new BigInteger("10").pow(N)).add(BD);
	}

}
