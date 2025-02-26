/*
 * Written by Lukas Rennhofer @2025
 * This file was written for the baselib of Spex
 * It is written from scratch for better control -
 * over the algorythm and its memory managment if needed
*/

#include "bits/stdc++.h"

/*
 * Swaps two elements of an array of integers
 * @param array: The array, which inherits the elemets @i and @j
 * @param i: Index of the 1st element
 * @param j: Index of the 2nd element
 */
void swap(int array[], int i, int j) {
    int temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}

/*
 * Rearrange elements so that: Elements less than pivot go to the left -
 * and elements greater than pivot go to the right.
 * @param array: The array, that needs to be searched
 * @param start: The start index of the section, that needs to be sorted
 * @param end: The end index of the section, that needs to be sorted
 */
int partition(int array[], int start, int end) {
    int pivot = array[end];
    int pIndex = start;

    for (int i = start; i < end; i++) {
        if (array[i] < pivot) {
            swap(array, i, pIndex);
            pIndex++;
        }
    }

    swap(array, pIndex, end);

    return pIndex;
}

/*
 * Quicksorts an array of integers in a ratio starting from @start until @end
 * @param array: The array, that needs to be sorted
 * @param start: The start index of the section, that needs to be sorted
 * @param end: The end index of the section, that needs to be sorted
 * Time Complexity:
 *   Best/Average: O(n log n) (good pivot)
 *   Worst: O(n*n) (bad pivot, sorted input with last element as pivot)
*/
void quicksortInt(int array[], int start, int end) {
    
    // array Case
    if (start >= end) {
        return;
    }

    int pivot = partition(array, start, end);
    quicksortInt(array, start, pivot - 1);
    quicksortInt(array, pivot + 1, end);
}