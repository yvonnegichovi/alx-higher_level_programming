#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * *insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the pointer to the head of the list
 * @number: the number to be insertr into the linked list
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	current = *head;
	prev = NULL;
	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	if (prev == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		new->next = current;
		prev->next = new;
	}
	return (new);
}
