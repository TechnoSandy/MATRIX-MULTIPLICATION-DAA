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

	public static void main(String[] args) {
		int[][] matrix1 = new int[10][10];
		double[][] matrix2 = new double[10][10];
		
	
		MatrixGenerator.generateMatrix(matrix1);
		// Printing randomly generated matrix
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				System.out.printf("%-5d", matrix1[i][j]);
			}
			System.out.println();
		}
		System.out.println();
		MatrixGenerator.generateMatrixWithLargeNumbers(matrix2);
		// Printing randomly generated matrix
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				System.out.printf(" %3.3E ", matrix2[i][j]);
			}
			System.out.println();
		}
	}

}
