/**
 * 
 */
package com.daa.project;

import java.util.Scanner;

/**
 * @author sandy
 *
 */
public class StrassenMultiplication {

	/**
	 * 
	 */
	public StrassenMultiplication() {
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

					System.out.println("Enter row and column Eg ( 2x2 / 4x4 / 6x6) Multiple of 2");
					System.out.println();
					System.out.print("ROW: ");
					// Take row input
					row = scan.nextInt();
					System.out.print("COLUMN: ");

					// Take Column Input
					column = scan.nextInt();
					System.out.println();

				} while (row != column || row % 2 != 0 );
				// While loop checks if row = column and it is of the form 2x2 / 4x4 / 6x6 i.e multiple of 2
				
				// Create Matrix with entered Values for row and column
				int[][] matrix1 = new int[row][column];
				// Calculating time to generate matrix
				long start = System.nanoTime();
				// Call matrix generator method to generate random matrix
				MatrixGenerator.generateMatrix(matrix1);
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

				scan.close();

	}

}
