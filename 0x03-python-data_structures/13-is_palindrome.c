#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to a pointer pointing the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *prev = NULL;
	listint_t *mid = NULL;
	listint_t *second_half = NULL;
	int is_palindrome = 1;

	/* an empt/single-node list is considered a palindrome */
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	/*use two pointers to find the middle of the list */
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		prev = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	if (fast_ptr != NULL)
	{
		mid = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	/* reverse the second half of the list */
	second_half = slow_ptr;
	prev->next = NULL;
	reverse_list(&second_half);
	/* compare teh first and reversed second half of the list */
	is_palindrome = compare_lists(*head, second_half);
	/* restore the original list */
	reverse_list(&second_half);
	if (mid != NULL)
	{
		prev->next = mid;
		mid->next = second_half;
	}
	else
		prev->next = second_half;
	return (is_palindrome);
}

/**
 * reverse_list - reverses a singly linked list
 * @head: double pointer to the head of the list
 */

void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * compare_lists - compares two linked lists for equality
 * @list1: pointer to the head of the first list
 * @list2: pointer to the head of the second list
 * Return: 1 if lists are equal, 0 otherwise
 */

int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);
		list1 = list1->next;
		list2 = list2->next;
	}
	return (list1 == NULL && list2 == NULL);
}
