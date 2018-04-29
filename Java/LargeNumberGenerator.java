package com.daa.project;

import java.math.BigInteger;
import java.util.Random;

public class LargeNumberGenerator {

	public LargeNumberGenerator() {

	}

	/**
	 * This method Genarates large number required for multiplication
	 * 
	 * @return
	 */
	public static BigInteger largeNumberGenerator() {

		// (2^1024-1) = 2¹⁰²⁴ =
		// 1.79769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536e+308
		// is the maximum length
		// Example: (2^4-1) = 15 is the maximum length of the number
		// Ref:https://www.quickprogrammingtips.com/java/creating-a-random-biginteger-in-java.html
		// Ref:https://dzone.com/articles/random-number-generation-in-java
		BigInteger bi = new BigInteger(1024, new Random());

		return bi;
	}

	public static long generateLong() {
		long l;
		do {
			l = new Random().nextLong();
		} while (l <= 0);
		return l;

	}
	
	
	
	public static void main(String[] args) {
		System.out.println("largeNumberGenerator() : "+largeNumberGenerator());
		System.out.println("generateLong() : "+generateLong());
	}
}
