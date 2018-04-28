package com.daa.project;

import java.util.Random;

/**
 * This Class generate Matrix of random row and columns
 * 
 * 
 */

public class MatrixGenerator {

	public MatrixGenerator() {
		
	}

	/**
	 * This matrix generator class generate matrix
	 * 
	 * @param matrix
	 * @return
	 */
	public static int[][] generateMatrix(int[][] matrix) {
		for (int x = 0; x < matrix.length; x++) {
			for (int Y = 0; Y < matrix[x].length; Y++) {
				matrix[x][Y] = (int) (Math.random() * 10);

			}

		}
		return matrix;
	}
	
	public static double[][] generateMatrixWithLargeNumbers(double[][] matrix) {
		for (int x = 0; x < matrix.length; x++) {
			for (int Y = 0; Y < matrix[x].length; Y++) {
				matrix[x][Y] = (double) Math.abs(new Random().nextLong());

			}

		}
		return matrix;
	}

}
