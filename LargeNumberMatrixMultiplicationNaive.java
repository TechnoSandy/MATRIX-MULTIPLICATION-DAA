/**
 * 
 */
package com.daa.project;

import java.util.Scanner;

/**
 * @author sandy
 *
 */
public class LargeNumberMatrixMultiplicationNaive {

	/**
	 * 
	 */
	public LargeNumberMatrixMultiplicationNaive() {
		// TODO Auto-generated constructor stub
	}

	/**
	 * @param args
	 */
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
				double[][] matrix = new double[row][column];
				MatrixGenerator.generateMatrixWithLargeNumbers(matrix);
				
				// Printing randomly generated matrix
				for (int i = 0; i < row; i++) {
					for (int j = 0; j < column; j++) {
						//System.out.printf("%-30f", matrix[i][j]);
						System.out.printf("  %3.3E", matrix[i][j]);
					}
					System.out.println();
				}

				System.out.println();
				//Formating output 
				//https://stackoverflow.com/questions/2944822/format-double-value-in-scientific-notation?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
				double[][] newMatrix = matrix.clone();
				double[][] result = new double[row][column];
				NaiveMultiplication(row, column, matrix, newMatrix, result);
				// Print multiplication result
				System.out.println();
				for (int i = 0; i < row; i++) {
					for (int j = 0; j < column; j++) {
						System.out.printf(" %16.8E", result[i][j]);
					}
					System.out.println();
				}
				System.out.println();
				scan.close();
				

	}
	private static void NaiveMultiplication(int row, int column, double[][] matrix, double[][] newMatrix, double[][] result) {
		double sum = 0;
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < column; j++) {
				/*
				 * m value depends on the number of column in the first matrix or rows in the
				 * second matrix https://www.youtube.com/watch?v=7kZDlUTct9k
				 */				
				for (int m = 0; m < column; m++) {
					sum = sum + matrix[i][m] * newMatrix[m][j];
				}
				result[i][j] = sum;
				sum = 0;

			}

		}
		
	}

	
}
