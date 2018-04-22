package com.daa.project;

import java.util.Scanner;

public class MatrixMultiplication {

	public MatrixMultiplication() {

	}

	public static void main(String[] args) {
		// Matrix row and column
		int row;
		int column;
		// Using scanner class to take console input
		Scanner scan = new Scanner(System.in);
		// Instruction to user
		do {

			System.out.println("Please row and column in integer format (Note: Number of rows = Number of columns)");
			System.out.println();
			System.out.print("ROW: ");
			// Take row input
			row = scan.nextInt();
			System.out.print("COLUMN: ");

			// Take Column Input
			column = scan.nextInt();
			System.out.println();

		} while (row != column);
		// Create Matrix with entered Values for row and column
		int[][] matrix1 = new int[row][column];

		// Calculating time to generate matrix
		long start = System.nanoTime();
		// Call matrix generator method to generate random matrix
		generateMatrix(matrix1);
		long stop = System.nanoTime();

		long totalTime = stop - start;

		// Printing returned generated matrix
		System.out.println("The random Matrix is generated for " + row + " rows and  " + column
				+ " columns \nand is printed as below");
		System.out.println();
		
		// Printing randomly generated matrix
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < column; j++) {
				System.out.printf("%-5d", matrix1[i][j]);
			}
			System.out.println();
		}

		System.out.println();
		System.out.println("Time to generate " + row + " X " + column + " Matrix in Nano Second is " + totalTime + " ns");

		/*
		 * Calculating the product of Matrix Normal Approch ( Traditional Way of
		 * Calculation for matrix i.e Using row column multiplication )Making copy of
		 * the generated matrix or duplicating it for matrix multiplication We are
		 * making shallow copy of the array since we are not modifying the original
		 * array its ok to clone the array for calculation purpose
		 */
		int[][] matrix2 = matrix1.clone();

		/*
		 * Result array will store the values of the multiplication i.e matrix1 X
		 * matrix2
		 */
		int[][] result = new int[row][column];
		
		long multiplication_start = System.nanoTime();
		matrixMultiplicationTraditional(row, column, matrix1, matrix2, result);
		long multiplication_end = System.nanoTime();
		long totalTime_Multiplication = multiplication_end - multiplication_start;

		// Print multiplication result
		System.out.println();
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < column; j++) {
				System.out.printf("%-5d", result[i][j]);
			}
			System.out.println();
		}
		System.out.println();
		System.out.println("Time to Multiply " + row + " X " + column + " Matrix in Nano Second is "
				+ totalTime_Multiplication + " ns");
		// Close the Scanner as it is no longer required to take any input
		scan.close();

	}

	/**
	 * This method use traditional way to multiply Matrix
	 * @param row
	 * @param column
	 * @param matrix1
	 * @param matrix2
	 * @param result
	 */
	public static void matrixMultiplicationTraditional(int row, int column, int[][] matrix1, int[][] matrix2,
			int[][] result) {
		int sum = 0;
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < column; j++) {
				/*
				 * m value depends on the number of column in the first matrix or rows in the
				 * second matrix https://www.youtube.com/watch?v=7kZDlUTct9k
				 */				
				for (int m = 0; m < column; m++) {
					sum = sum + matrix1[i][m] * matrix2[m][j];
				}
				result[i][j] = sum;
				sum = 0;

			}

		}
	}

	/**
	 * Takes 2D empty matrix to fill values in rows and column and return the
	 * generated matrix
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

}
