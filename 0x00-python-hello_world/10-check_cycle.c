#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *pp;
	listint_t *prev;

	pp = list;
	prev = list;

	while (list && pp && pp->next)
	{
		list = list->next;
		pp = pp->next->next;

		if (list == pp)
		{
			list = prev;
			prev = pp;
			while (1)
			{
				pp = prev;
				while (pp->next != list && pp->next != prev)
				{
					pp = pp->next;
				}
				if (pp->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
