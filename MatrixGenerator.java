package com.daa.project;

import java.util.Scanner;

public class MatrixGenerator {

	public MatrixGenerator() {

	}

	public static void main(String[] args) {
		// Using scanner class to take console input
		Scanner scan = new Scanner(System.in);
		// Instruction to user
		System.out.println("Please row and collumn in integer format");
		System.out.println();
		System.out.print("ROW: ");
		// Take row input
		int row = scan.nextInt();
		System.out.print("COLUMN: ");

		// Take Column Input
		int column = scan.nextInt();
		System.out.println();
		// Create Matrix with entered Values for row and column
		int[][] matrix = new int[row][column];

		// Calculating time to generate matrix
		long start = System.nanoTime();

		generateMatrix(matrix);
		long stop = System.nanoTime();

		long totalTime = stop - start;
		System.out.println();
		System.out.println("Time to generate Matrix in Nano Second\t " + totalTime + " ns");

		scan.close();

	}

	/**
	 * Takes 2D empty matrix to fill values in rows and column
	 * 
	 * @param matrix
	 */
	public static void generateMatrix(int[][] matrix) {
		for (int x = 0; x < matrix.length; x++) {
			for (int Y = 0; Y < matrix[x].length; Y++) {
				matrix[x][Y] = (int) (Math.random() * 10);
				System.out.printf("%-5d", matrix[x][Y]);
			}
			System.out.println();
			
		}
	}

}
