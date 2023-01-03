#include "lists.h"

/**
 * insert_node - inserts a new node at a
 * a given position in a list
 * @head: head of a list
 * @number: index of the position in the list
 * Return: the address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *h;
	listint_t *prev;
	listint_t next;

	h = *head;
	next = h;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		prev = h;
		h = h->next;
	}

	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = h;

		if (h == *head)
			*head = new;
		else
			prev->next = new;
	}

	return (new);
}
