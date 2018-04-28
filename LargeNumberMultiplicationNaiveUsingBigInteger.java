/**
 * 
 */
package com.daa.project;

import java.math.BigInteger;

/**
 * @author sandy
 *
 */
public class LargeNumberMultiplicationNaiveUsingBigInteger {

	/**
	 * 
	 */
	public LargeNumberMultiplicationNaiveUsingBigInteger() {

	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// BigInter is used because requirement is the digit of the number can be upto a million digits each
		// which can be only represented by BigInteger in java
		multiplyBigIntegers();

	}

	/**
	 * 
	 */
	public static void multiplyBigIntegers() {
		BigInteger bi = LargeNumberGenerator.largeNumberGenerator();
		BigInteger newBi = LargeNumberGenerator.largeNumberGenerator();
		BigInteger Multiplication_Result = bi.multiply(newBi);
		System.out.println("Big integer one  \n" + bi);
		System.out.println("");
		System.out.println("Big integer two  \n" + newBi);
		System.out.println("");
		System.out.println("Multiplication Result  \n" + Multiplication_Result);
	}

}
